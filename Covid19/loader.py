import os
import gdown
from tensorflow.keras.models import load_model

MODEL_PATH = "app/model/model.h5"

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/file/d/17dxS2gRw2Gw1mt6-1bindlL7GsvQBuvd/view?usp=sharing"
    gdown.download(url, MODEL_PATH, quiet=False)
