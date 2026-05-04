import os
import gdown
from tensorflow.keras.models import load_model

MODEL_PATH = "app/model/model.h5"

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/drive/home?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto"
    gdown.download(url, MODEL_PATH, quiet=False)
