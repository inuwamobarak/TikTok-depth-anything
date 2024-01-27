from flask import Flask, render_template, request
from PIL import Image
from transformers import pipeline
import requests
from io import BytesIO

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

    # Display image with depth
    return render_template('result.html', image_url=url, depth=depth)

if __name__ == "__main__":
    app.run(debug=True)