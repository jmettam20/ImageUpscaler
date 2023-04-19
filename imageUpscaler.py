from PIL import Image, ImageEnhance

# Open the image file
img = Image.open('/Users/joshmettam/Documents/Programming/test.tga')

# Calculate the new size of the image
new_width = img.width * 12
new_height = img.height * 12
new_size = (new_width, new_height)

# Resize the image
resized_img = img.resize(new_size, Image.BILINEAR)

# Create an object to enhance the image
enhancer = ImageEnhance.Sharpness(img)

# Enhance the image
enhanced_img = enhancer.enhance(3.0)

# Save the resized image
enhanced_img.save('/Users/joshmettam/Documents/Programming/output.tga')