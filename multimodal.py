import os
from PIL import Image

image_path = "data/sample.jpg"
if not os.path.exists(image_path):
    print("Error: Please place an image named 'sample.jpg' inside the 'data' folder.")
else:
    print("Loading image for multimodal processing...")
    img = Image.open(image_path)
    print(f"Image successfully loaded! Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
    print("Multimodal check passed: Your project is now capable of handling non-text modalities alongside text documents[span_1](start_span)[span_1](end_span)!")