import json
import os

class HashtagEngine:
    def __init__(self, data_path: str = "data/hashtags.json"):
        self.data_path = data_path
        self.hashtags = self.load_hashtags()

    def load_hashtags(self) -> dict:
        """Load hashtags from JSON file."""
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                return json.load(f)
        return {}

    def generate_hashtags(self, mood: str, num_hashtags: int = 5) -> list:
        """
        Generate hashtags based on detected mood.
        """
        if mood in self.hashtags:
            tags = self.hashtags[mood]
            return tags[:num_hashtags]  # Return up to num_hashtags
        # Fallback to aesthetic or random
        fallback = self.hashtags.get('aesthetic', [])
        return fallback[:num_hashtags]