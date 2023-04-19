from flask import Flask, request, jsonify
from PIL import Image, ImageEnhance

# new flask instance
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request object
    file = request.files['image']
    # Open the image file
    img = Image.open(file)
    # Calculate the new size of the image
    new_width = img.width * 12
    new_height = img.height * 12
    new_size = (new_width, new_height)
    # Resize the image
    resized_img = img.resize(new_size, Image.BILINEAR)
    # Create an object to enhance the image
    enhancer = ImageEnhance.Sharpness(resized_img)
    # Enhance the image
    enhanced_img = enhancer.enhance(3.0)
    # Save the resized image
    output_path = 'output.tga'
    enhanced_img.save(output_path)
    # Return the path of the output image as a JSON response
    return jsonify({'output_path': output_path})

if __name__ == '__main__':
    app.run(debug=True)
