class TextProcessor:
    def __init__(self):
        pass

    def clean_caption(self, caption: str) -> str:
        """
        Clean and format the generated caption.
        """
        # Remove extra spaces, capitalize first letter
        caption = ' '.join(caption.split())
        return caption.capitalize()

    def format_hashtags(self, hashtags: list) -> str:
        """
        Format hashtags as a string.
        """
        return ' '.join(hashtags)