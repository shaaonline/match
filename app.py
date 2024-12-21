
from flask import Flask, render_template, request, jsonify
import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_images():
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({"error": "Both images are required"}), 400

    # Read images from request
    image1 = cv2.imdecode(np.frombuffer(request.files['image1'].read(), np.uint8), cv2.IMREAD_COLOR)
    image2 = cv2.imdecode(np.frombuffer(request.files['image2'].read(), np.uint8), cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Compute SSIM
    score, diff = ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype("uint8")

    # Save the result image
    _, thresh = cv2.threshold(diff, 128, 255, cv2.THRESH_BINARY_INV)
    result_path = "static/result.png"
    cv2.imwrite(result_path, thresh)

    return jsonify({"score": score, "result": result_path})

if __name__ == "__main__":
    app.run(debug=True)
