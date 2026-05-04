# 🧠 Image Classification System (VGG16 + FastAPI + Streamlit)

## 📌 Description

This project is a Deep Learning system for medical image classification that detects chest X-ray images and classifies them into:

* Normal
* Viral Pneumonia
* COVID-19

The model is built using **Transfer Learning (VGG16)** and deployed in two ways:

* REST API using FastAPI
* Interactive Web App using Streamlit

---

## 🚀 Features

* Upload medical images for prediction
* Real-time classification
* JSON API response (FastAPI)
* Interactive UI (Streamlit)
* Clean and modular architecture

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* VGG16 (Transfer Learning)
* FastAPI
* Streamlit
* NumPy
* Scikit-learn

---

## 📡 Live Demo

**URL:**

```
https://covid-19-production-6f9b.up.railway.app/docs

<img width="1907" height="950" alt="image" src="https://github.com/user-attachments/assets/d4d52cb7-d969-467a-b6cb-b0ff6195219d" />


```

**Endpoint:**

```
POST /predict
```

### 📥 Input

* Image file (multipart/form-data)

### 📤 Response

```json
{
  "class_id": 2,
  "class_name": "COVID-19"
}
```

---

## 🎨 Streamlit App

**URL:**

```
http://localhost:8501

<img width="1600" height="804" alt="image" src="https://github.com/user-attachments/assets/1bde84c4-57be-4996-92a5-8a0a77ff4015" />

```
---

## 📁 Dataset

Dataset used from Kaggle:

👉 [https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset](https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset)

⚠️ Not included in repository due to size.

---

### Features:

* Upload X-ray image
* View prediction instantly
* Display confidence score

---

## 📁 Project Structure

```text
Image-Classification-API/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── model/
│   │   ├── model.h5
│   │   └── loader.py
│   │
│   ├── utils/
│   │   ├── preprocess.py
│   │   └── predict.py
│
├── notebooks/
│   ├── covid 19.ipynb
|
├── training/
│   ├── dataset_loader.py
|   |__evaluation.py
|   |__train.py
|
├── requirements.txt
|__ Streamlit Covid19 Classification App.py
└── run.py
```

---

## ⚡ How to Run

### Flask API

```bash
uvicorn api:app --reload
```

### Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 💡 Notes

* Model trained using VGG16 transfer learning
* Input image resized to 224x224
* Supports RGB chest X-ray images
"# Covid-19" 
"# Covid-19" 
