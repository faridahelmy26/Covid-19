import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# =========================
# Load Model
# =========================
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(r"E:\faculty\projects\Ai Project\Covid19\Covid19\app\model\model.h5")
    return model

model = load_model()

# =========================
# Classes
# =========================
classes = ['Normal', 'Viral Pneumonia', 'Covid']

# =========================
# UI
# =========================
st.title("🫁 COVID-19 X-Ray Classification App")
st.write("Upload a chest X-ray image and the model will predict the class.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # preprocess
    img = image.resize((224, 224))
    img_array = np.array(img)

    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # prediction
    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.write("---")
    st.subheader(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}")
