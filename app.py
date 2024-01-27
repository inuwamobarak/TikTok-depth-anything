from flask import Flask, render_template, request
from PIL import Image
from transformers import pipeline
import requests
from io import BytesIO
import base64

app = Flask(__name__)

# Load pipeline
pipe = pipeline(task="depth-estimation", model="LiheYoung/depth-anything-small-hf")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimate_depth', methods=['POST'])
def estimate_depth():
    # Get selected input type (url or upload)
    input_type = request.form.get('input_type', 'url')

    url = None  # Initialize url variable
    original_image_base64 = None  # Initialize original_image_base64 variable

    if input_type == 'url':
        # Get image URL from the form
        url = request.form.get('image_url', '')

        # Check if the URL is provided
        if not url:
            return "Please provide an Image URL."
    elif input_type == 'upload':
        # Get uploaded file
        uploaded_file = request.files.get('file_upload')

        # Check if a file is uploaded
        if not uploaded_file:
            return "Please upload an image."

        # Read the image from the file
        original_image = Image.open(uploaded_file)

        # Convert original image to base64
        original_image_base64 = image_to_base64(original_image)
    else:
        return "Invalid input type"

    if input_type == 'url':
        # Load image
        image = Image.open(requests.get(url, stream=True).raw)
    elif input_type == 'upload':
        image = original_image

    # Inference
    depth = pipe(image)["depth"]

    # Convert depth image to base64
    depth_base64 = image_to_base64(depth)

    # Display image with depth
    return render_template('result.html', input_type=input_type, image_url=url,
                           original_image_base64=original_image_base64, depth_base64=depth_base64)

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

if __name__ == "__main__":
    app.run(debug=True)
