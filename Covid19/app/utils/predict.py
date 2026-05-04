import numpy as np
from app.config import CLASS_NAMES

def predict_image(model, img_array):
    preds = model.predict(img_array)
    class_id = np.argmax(preds, axis=1)[0]
    class_name = CLASS_NAMES[class_id]
    return class_id, class_name