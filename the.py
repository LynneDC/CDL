from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 225, 225
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Load a font (adjust the path accordingly)
font = ImageFont.load_default()

# Set text and position
text = "THE CHURCH"
text_width, text_height = draw.textsize(text, font)
text_position = ((width - text_width) // 2, (height - text_height) // 2)

# Draw the text on the image
draw.text(text_position, text, font=font, fill="black")

# Save or display the image
image.save("the_church_image.png")
image.show()
