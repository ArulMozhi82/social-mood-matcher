import streamlit as st
from PIL import Image
import os
import sys

# Add current directory to path for imports
sys.path.append(os.path.dirname(__file__))

from services.image_sentiment import ImageSentimentAnalyzer
from services.caption_generator import CaptionGenerator
from services.hashtag_engine import HashtagEngine
from services.character_limiter import CharacterLimiter
from services.gemini_service import GeminiService
from utils.image_processing import ImageProcessor
from utils.text_processing import TextProcessor

# Cache models
@st.cache_resource
def load_blip_model():
    from transformers import pipeline
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

@st.cache_resource
def load_sentiment_analyzer():
    return ImageSentimentAnalyzer()

@st.cache_resource
def load_caption_generator():
    return CaptionGenerator()

@st.cache_resource
def load_hashtag_engine():
    return HashtagEngine()

@st.cache_resource
def load_character_limiter():
    return CharacterLimiter()

@st.cache_resource
def load_gemini_service():
    return GeminiService()

@st.cache_resource
def load_image_processor():
    return ImageProcessor()

@st.cache_resource
def load_text_processor():
    return TextProcessor()

def main():
    st.title("🎨 Social Mood Matcher")
    st.markdown("Upload an image to detect mood, generate captions, and get trending hashtags!")

    # Load services
    blip_pipeline = load_blip_model()
    sentiment_analyzer = load_sentiment_analyzer()
    caption_generator = load_caption_generator()
    hashtag_engine = load_hashtag_engine()
    character_limiter = load_character_limiter()
    gemini_service = load_gemini_service()
    image_processor = load_image_processor()
    text_processor = load_text_processor()

    # Sidebar
    st.sidebar.header("Settings")
    platform = st.sidebar.selectbox("Platform", ["Twitter/X", "Instagram", "Facebook"])
    style = st.sidebar.selectbox("Caption Style", ["casual", "aesthetic", "professional", "playful"])
    use_gemini = st.sidebar.checkbox("Enhance with Gemini (requires API key)")
    gemini_key = st.sidebar.text_input("Gemini API Key", type="password") if use_gemini else None
    if gemini_key:
        gemini_service.api_key = gemini_key

    # Main page
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Process image
        processed_image = image_processor.process_image(image)

        # Step 1: Generate caption
        with st.spinner("Generating image caption..."):
            caption_result = blip_pipeline(processed_image)
            raw_caption = caption_result[0]['generated_text']
            cleaned_caption = text_processor.clean_caption(raw_caption)

        # Step 2: Detect mood
        with st.spinner("Detecting mood..."):
            mood = sentiment_analyzer.detect_mood(cleaned_caption)

        # Step 3: Generate captions
        with st.spinner("Generating captions..."):
            captions = caption_generator.generate_captions(cleaned_caption, mood)

        # Step 4: Generate hashtags
        with st.spinner("Generating hashtags..."):
            hashtags = hashtag_engine.generate_hashtags(mood)

        # Step 5: Enhance with Gemini if enabled
        if use_gemini and gemini_service.api_key:
            with st.spinner("Enhancing caption with Gemini..."):
                captions[style] = gemini_service.enhance_caption(captions[style], mood)

        # Display results
        st.header("Results")
        st.subheader(f"Detected Mood: {mood.capitalize()}")

        st.subheader("Generated Captions")
        selected_caption = captions.get(style, captions['casual'])
        st.write(f"**{style.capitalize()}:** {selected_caption}")

        st.subheader("Suggested Hashtags")
        st.write(" ".join(hashtags))

        # Final export
        st.subheader("Final Export Text")
        final_text = character_limiter.limit_text(selected_caption, hashtags, platform)
        st.text_area("Copy this text:", final_text, height=100)

        st.info(f"Character count: {len(final_text)} / {character_limiter.limits[platform]} for {platform}")

if __name__ == "__main__":
    main()