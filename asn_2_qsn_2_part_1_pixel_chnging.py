from PIL import Image

# Open the image
image = Image.open('chapter1.jpg')

# Get the pixel values
pixels = image.load()

# Iterate over the pixels
for x in range(image.width):
    for y in range(image.height):
        # Add the generated number to the original pixel values
        r, g, b = pixels[x, y]
        pixels[x, y] = (r + 75, g + 75, b + 75)

# Save the image
image.save('Chapter1_edited.jpg')
