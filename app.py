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
    # Get image URL from the form
    url = request.form['image_url']

    # Load image
    image = Image.open(requests.get(url, stream=True).raw)

    # Inference
    depth = pipe(image)["depth"]

    # Convert depth image to base64
    depth_base64 = image_to_base64(depth)

    # Display image with depth
    return render_template('result.html', image_url=url, depth_base64=depth_base64)

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

if __name__ == "__main__":
    app.run(debug=True)
