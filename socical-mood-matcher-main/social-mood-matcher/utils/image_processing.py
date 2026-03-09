from PIL import Image
import numpy as np

class ImageProcessor:
    def __init__(self):
        pass

    def process_image(self, image: Image.Image) -> Image.Image:
        """
        Process uploaded image: resize if too large, convert to RGB.
        """
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Resize if too large (e.g., max 512x512 for efficiency)
        max_size = 512
        if image.width > max_size or image.height > max_size:
            image.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)

        return image

    def image_to_array(self, image: Image.Image) -> np.ndarray:
        """
        Convert PIL image to numpy array for model input.
        """
        return np.array(image)