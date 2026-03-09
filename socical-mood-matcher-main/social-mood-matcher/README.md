# Social Mood Matcher

A Streamlit web application that analyzes uploaded images to detect mood, generate AI-powered social media captions, suggest trending hashtags, and format output for different platforms.

## Features

- **Image Upload**: Upload images in JPG, JPEG, or PNG format
- **Mood Detection**: Uses DistilBERT to analyze image captions and detect moods like cozy, aesthetic, playful, luxury, peaceful, or energetic
- **AI Caption Generation**: Generates captions in multiple styles (casual, aesthetic, professional, playful)
- **Hashtag Suggestions**: Selects relevant hashtags based on detected mood
- **Platform Formatting**: Applies character limits for Twitter/X (280), Instagram (2200), and Facebook (63206)
- **Optional Gemini Enhancement**: Enhance captions using Google Gemini 2.0 Flash API
- **Responsive UI**: Clean Streamlit interface with sidebar controls

## Tech Stack

- Python
- Streamlit
- HuggingFace Transformers (BLIP for image captioning, DistilBERT for sentiment)
- Pillow for image processing
- Google Generative AI (optional)

## Setup Instructions

1. Clone or download the project:
   ```bash
   cd /path/to/your/workspace
   # Copy the social-mood-matcher folder
   ```

2. Install dependencies:
   ```bash
   cd social-mood-matcher
   pip install -r requirements.txt
   ```

3. (Optional) Set up Gemini API:
   - Get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Set environment variable: `export GEMINI_API_KEY=your_key_here`
   - Or enter it in the app sidebar

## How to Run

1. Navigate to the project directory:
   ```bash
   cd social-mood-matcher
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your browser to the displayed URL (usually http://localhost:8501)

## Usage

1. Upload an image using the file uploader
2. Select your preferred platform and caption style in the sidebar
3. Toggle Gemini enhancement if you have an API key
4. View the detected mood, generated captions, and hashtags
5. Copy the final formatted text for your social media post

## Project Structure

```
social-mood-matcher/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── services/                 # Core business logic
│   ├── image_sentiment.py    # Mood detection service
│   ├── caption_generator.py  # Caption generation service
│   ├── hashtag_engine.py     # Hashtag selection service
│   ├── character_limiter.py  # Platform character limits
│   └── gemini_service.py     # Gemini AI integration
├── utils/                    # Utility functions
│   ├── image_processing.py   # Image preprocessing
│   └── text_processing.py    # Text formatting utilities
├── data/                     # Data files
│   └── hashtags.json         # Hashtag database
└── README.md                 # This file
```

## Error Handling

The app handles common errors such as:
- Invalid image formats
- Missing API keys for Gemini
- Network issues during model loading
- Character limit exceedances (auto-truncates hashtags)

## Performance

- Models are cached using Streamlit's `@st.cache_resource` to avoid reloading
- Images are resized for efficient processing
- Asynchronous processing with loading spinners for better UX