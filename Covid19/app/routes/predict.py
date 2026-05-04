import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

from app.model.loader import load_trained_model
from app.utils.preprocess import preprocess_image
from app.utils.predict import predict_image
from app.config import UPLOAD_FOLDER

predict_bp = Blueprint('predict', __name__)

# load model once
model = load_trained_model()

@predict_bp.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    img_array = preprocess_image(filepath)
    class_id, class_name = predict_image(model, img_array)

    return jsonify({
        "class_id": int(class_id),
        "class_name": class_name
    })