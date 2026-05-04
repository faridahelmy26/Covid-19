import os
import gdown
from tensorflow.keras.models import load_model

MODEL_PATH = "app/model/model.h5"

def load_trained_model():
    if not os.path.exists(MODEL_PATH):
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        file_id = "17dxS2gRw2Gw1mt6-1bindlL7GsvQBuvd"
        url = f"https://drive.google.com/uc?id={file_id}&export=download"
        gdown.download(url, MODEL_PATH, quiet=False)
    
    return load_model(MODEL_PATH)
