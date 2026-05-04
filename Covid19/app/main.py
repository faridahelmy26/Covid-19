from fastapi import FastAPI, File, UploadFile
import shutil
import os

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from loader import load_trained_model
from app.utils.preprocess import preprocess_image
from app.utils.predict import predict_image

app = FastAPI(title="Image Classification API")

model = load_trained_model()

UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "🚀 FastAPI Image Classification API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    img_array = preprocess_image(file_path)
    class_id, class_name = predict_image(model, img_array)

    return {
        "class_id": int(class_id),
        "class_name": class_name
    }
