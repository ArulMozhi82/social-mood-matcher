from transformers import pipeline

class ImageSentimentAnalyzer:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def detect_mood(self, caption: str) -> str:
        """
        Detect mood from image caption using sentiment analysis.
        Maps sentiment to predefined moods.
        """
        result = self.sentiment_pipeline(caption)[0]
        label = result['label']  # POSITIVE or NEGATIVE
        confidence = result['score']

        # Map sentiment to moods
        mood_mapping = {
            'POSITIVE': ['energetic', 'playful', 'luxury'],
            'NEGATIVE': ['cozy', 'peaceful', 'aesthetic']
        }

        import random
        moods = mood_mapping.get(label, ['aesthetic'])
        return random.choice(moods)  # Randomly select one for variety