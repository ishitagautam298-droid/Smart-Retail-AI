import io
import os
import pickle
import numpy as np
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Try loading optional ML libraries gracefully
try:
    import face_recognition
    HAS_FACE_REC = True
except ImportError:
    HAS_FACE_REC = False

try:
    import tensorflow as tf
    HAS_TF = True
except ImportError:
    HAS_TF = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

app = FastAPI(
    title="Smart Retail & Customer Intelligence API",
    description="Multi-modal AI backend providing face recognition, product image classification, sentiment analysis, and conversational AI intent recognition.",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Models
face_database = {}
sentiment_model = None
sentiment_vectorizer = None
chatbot_model = None
chatbot_vectorizer = None
label_encoder = None
product_model = None

# Load Face DB
face_db_path = os.path.join(MODEL_DIR, "face_db.pkl")
if os.path.exists(face_db_path):
    with open(face_db_path, "rb") as f:
        face_database = pickle.load(f)

# Load Sentiment Model & Vectorizer
sent_path = os.path.join(MODEL_DIR, "sentiment_model.pkl")
vec_path = os.path.join(MODEL_DIR, "vectorizer.pkl")
if os.path.exists(sent_path) and os.path.exists(vec_path):
    with open(sent_path, "rb") as f:
        sentiment_model = pickle.load(f)
    with open(vec_path, "rb") as f:
        sentiment_vectorizer = pickle.load(f)

# Load Chatbot Model, Vectorizer & Label Encoder
cb_model_path = os.path.join(MODEL_DIR, "chatbot_model.pkl")
cb_vec_path = os.path.join(MODEL_DIR, "chatbot_vectorizer.pkl")
lbl_enc_path = os.path.join(MODEL_DIR, "label_encoder.pkl")
if os.path.exists(cb_model_path) and os.path.exists(cb_vec_path) and os.path.exists(lbl_enc_path):
    with open(cb_model_path, "rb") as f:
        chatbot_model = pickle.load(f)
    with open(cb_vec_path, "rb") as f:
        chatbot_vectorizer = pickle.load(f)
    with open(lbl_enc_path, "rb") as f:
        label_encoder = pickle.load(f)

# Load Keras Product Classifier Model
product_model_path = os.path.join(MODEL_DIR, "product_classifier.keras")
if HAS_TF and os.path.exists(product_model_path):
    product_model = tf.keras.models.load_model(product_model_path)

# Pydantic Schemas
class TextRequest(BaseModel):
    text: str

class ChatRequest(BaseModel):
    message: str

FASHION_CLASSES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

@app.get("/")
def root():
    return {
        "status": "online",
        "system": "AI-Powered Smart Retail & Customer Intelligence Platform",
        "endpoints": [
            "/health",
            "/recognize-face",
            "/analyze-sentiment",
            "/chatbot",
            "/classify-product"
        ]
    }

@app.get("/health")
def health():
    return {
        "face_recognition_active": HAS_FACE_REC and bool(face_database),
        "sentiment_analysis_active": sentiment_model is not None,
        "chatbot_active": chatbot_model is not None,
        "product_classifier_active": product_model is not None
    }

@app.post("/recognize-face")
async def recognize_face(file: UploadFile = File(...)):
    if not HAS_FACE_REC:
        raise HTTPException(status_code=501, detail="face_recognition library not installed on server.")
    if not face_database:
        raise HTTPException(status_code=404, detail="Face database is empty or missing.")

    image_bytes = await file.read()
    image = face_recognition.load_image_file(io.BytesIO(image_bytes))
    faces = face_recognition.face_encodings(image)

    if len(faces) == 0:
        return {"status": "No face detected", "customer_id": None, "name": "Unknown"}

    uploaded_encoding = faces[0]
    for customer_id, data in face_database.items():
        matches = face_recognition.compare_faces(data["encodings"], uploaded_encoding, tolerance=0.6)
        if True in matches:
            return {
                "status": "Returning customer",
                "customer_id": customer_id,
                "name": data["name"]
            }

    return {
        "status": "New customer",
        "customer_id": None,
        "name": "Unknown"
    }

@app.post("/analyze-sentiment")
def analyze_sentiment(request: TextRequest):
    if sentiment_model is None or sentiment_vectorizer is None:
        raise HTTPException(status_code=503, detail="Sentiment analysis model not loaded.")

    transformed = sentiment_vectorizer.transform([request.text])
    prediction = sentiment_model.predict(transformed)[0]
    return {
        "text": request.text,
        "sentiment": str(prediction)
    }

@app.post("/chatbot")
def chatbot(request: ChatRequest):
    if chatbot_model is None or chatbot_vectorizer is None or label_encoder is None:
        raise HTTPException(status_code=503, detail="Chatbot model not loaded.")

    transformed = chatbot_vectorizer.transform([request.message])
    pred = chatbot_model.predict(transformed)
    intent = label_encoder.inverse_transform(pred)[0]

    return {
        "message": request.message,
        "intent": intent
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
