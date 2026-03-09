import google.generativeai as genai
import os

class GeminiService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')

    def enhance_caption(self, caption: str, mood: str) -> str:
        """
        Enhance caption using Gemini if API key is available.
        """
        if not self.api_key:
            return caption

        try:
            prompt = f"Enhance this social media caption to be more engaging for a {mood} mood: {caption}"
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Gemini enhancement failed: {e}")
            return caption