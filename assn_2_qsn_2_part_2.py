from PIL import Image

def sum_red_pixels(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get the width and height of the image
    width, height = img.size

    # Initialize sum of red pixel values
    red_sum = 0

    # Iterate through each pixel and add the red component to the sum
    for x in range(width):
        for y in range(height):
            # Get the red component of the pixel
            red_value = img.getpixel((x, y))[0]  # [0] corresponds to the red component

            # Add the red component to the sum
            red_sum += red_value

    return red_sum

# Path to the image (replace with your image path)
image_path = "Chapter1_edited.jpg"

# Call the function to calculate the sum of red pixels
red_pixel_sum = sum_red_pixels(image_path)

# Display the sum of red pixel values
print("Sum of red pixel values:", red_pixel_sum)
