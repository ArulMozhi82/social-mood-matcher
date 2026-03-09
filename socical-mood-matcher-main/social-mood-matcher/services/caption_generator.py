class CaptionGenerator:
    def __init__(self):
        self.templates = {
            'casual': {
                'cozy': "Just chilling with this {caption}. So comfy! ☕",
                'aesthetic': "This {caption} is giving major vibes ✨",
                'playful': "Having fun with this {caption}! 🎉",
                'luxury': "Living that luxury life with this {caption} 💎",
                'peaceful': "Finding peace in this {caption} 🌿",
                'energetic': "Full of energy with this {caption}! ⚡"
            },
            'aesthetic': {
                'cozy': "Soft whispers of warmth in this {caption}. Cozy dreams. 🕯️",
                'aesthetic': "Aesthetic perfection in every detail of this {caption}. 🌸",
                'playful': "Playful elegance captured in this {caption}. 🎨",
                'luxury': "Timeless luxury embodied in this {caption}. 👑",
                'peaceful': "Serene beauty in this {caption}. Tranquil moments. 🌊",
                'energetic': "Vibrant energy flowing through this {caption}. 🌟"
            },
            'professional': {
                'cozy': "Embracing comfort in this {caption}. A moment of relaxation.",
                'aesthetic': "Appreciating the artistry in this {caption}.",
                'playful': "Capturing joy in this {caption}.",
                'luxury': "Exuding sophistication in this {caption}.",
                'peaceful': "Finding tranquility in this {caption}.",
                'energetic': "Energized by this {caption}."
            },
            'playful': {
                'cozy': "Snug as a bug with this {caption}! 🐛",
                'aesthetic': "Vibe check: aesthetic AF with this {caption}! 😎",
                'playful': "Let's play! This {caption} is calling my name! 🎈",
                'luxury': "Fancy pants alert! This {caption} is luxe! 🤑",
                'peaceful': "Chill vibes only with this {caption}. 🧘",
                'energetic': "Zoom zoom! This {caption} has me pumped! 🚀"
            }
        }

    def generate_captions(self, caption: str, mood: str, styles: list = None) -> dict:
        """
        Generate captions in different styles based on mood.
        """
        if styles is None:
            styles = ['casual', 'aesthetic', 'professional', 'playful']

        generated = {}
        for style in styles:
            template = self.templates.get(style, {}).get(mood, "Enjoying this {caption}!")
            generated[style] = template.format(caption=caption.lower())

        return generated