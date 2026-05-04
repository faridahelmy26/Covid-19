import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "model.h5")

CLASS_NAMES = ['Normal', 'Viral Pneumonia', 'COVID']