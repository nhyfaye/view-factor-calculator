from PIL import Image
import os

# Set the directory where the images are located
directory = 'lib'

# Create a list of the image filenames
files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.png')]

# Create a new blank image that can hold the grid of images
result = Image.new("RGB", (800, 600), (255, 255, 255))

# Calculate the size of each individual image in the grid
image_width = result.width // 4
image_height = result.height // 3

# Loop through the list of image filenames and add each image to the grid
for index, file in enumerate(files):
    # Load the image using Pillow
    img = Image.open(file)

    # Resize the image to fit in the grid
    img = img.resize((image_width, image_height))

    # Calculate the x and y position of the current image in the grid
    x = (index % 4) * image_width
    y = (index // 4) * image_height

    # Paste the current image onto the blank image in the correct position
    result.paste(img, (x, y))

# Display the final grid of images
result.show()
