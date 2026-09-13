import os
from PIL import Image

# Create the data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create a simple blank image and save it as sample.jpg inside the data folder
img = Image.new('RGB', (200, 200), color = 'blue')
img.save('data/sample.jpg')
print("sample.jpg created successfully inside the data folder!")