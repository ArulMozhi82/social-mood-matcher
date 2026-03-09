class CharacterLimiter:
    def __init__(self):
        self.limits = {
            'Twitter/X': 280,
            'Instagram': 2200,
            'Facebook': 63206
        }

    def limit_text(self, caption: str, hashtags: list, platform: str) -> str:
        """
        Combine caption and hashtags, apply character limit for the platform.
        Truncate hashtags first if over limit.
        """
        limit = self.limits.get(platform, 280)  # Default to Twitter
        hashtag_str = ' ' + ' '.join(hashtags)
        full_text = caption + hashtag_str

        if len(full_text) <= limit:
            return full_text

        # Truncate hashtags
        remaining = limit - len(caption + ' ')
        truncated_hashtags = []
        for tag in hashtags:
            if remaining > len(tag) + 1:  # +1 for space
                truncated_hashtags.append(tag)
                remaining -= len(tag) + 1
            else:
                break

        return caption + ' ' + ' '.join(truncated_hashtags)