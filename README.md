# 🛍️ AI-Powered Smart Retail & Customer Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12%2B-FF6F00.svg)](https://www.tensorflow.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.2%2B-F7931E.svg)](https://scikit-learn.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.7%2B-5C3EE8.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end multi-modal Artificial Intelligence system designed to revolutionize retail experiences. The platform seamlessly integrates **Computer Vision**, **Natural Language Processing (NLP)**, **Facial Biometric Intelligence**, and **RESTful Microservices** to provide personalized customer recognition, automated product tagging, sentiment tracking, and conversational AI support.

---

## 🌟 Key Highlights & Modules

```
                               ┌────────────────────────────────────────────────┐
                               │   Smart Retail AI System Architecture          │
                               └───────────────────────┬────────────────────────┘
                                                       │
         ┌───────────────────────┬─────────────────────┼─────────────────────┬──────────────────────┐
         │                       │                     │                     │                      │
┌────────▼────────┐    ┌─────────▼─────────┐ ┌─────────▼─────────┐ ┌──────────▼──────────┐ ┌─────────▼─────────┐
│ Module 1:       │    │ Module 2:         │ │ Module 3:         │ │ Module 4:          │ │ Module 5:         │
│ Product Image   │    │ Facial Recognition│ │ Customer          │ │ Support Chatbot    │ │ FastAPI Micro-    │
│ Classification  │    │ & Visit Logging   │ │ Sentiment Analysis│ │ Intent Engine      │ │ Service Backend   │
└─────────────────┘    └───────────────────┘ └───────────────────┘ └────────────────────┘ └───────────────────┘
```

### 1. 👕 Product Image Classification (CNN)
- **Architecture**: Deep Convolutional Neural Network (CNN) built with Keras & TensorFlow.
- **Dataset**: Fashion-MNIST (60,000 training images across 10 apparel categories).
- **Functionality**: Automatically categorizes retail inventory items (T-shirts, Dresses, Shoes, Bags, etc.) from raw image feeds to streamline inventory management and visual search.

### 2. 👤 Facial Recognition & VIP Customer Intelligence
- **Engine**: OpenCV + 128-dimensional facial embedding vectors using HOG & deep metric learning.
- **Dataset**: Labeled Faces in the Wild (LFW) & custom customer face database.
- **Functionality**: Detects customer entry in real-time, matches biometrics against historical records, differentiates returning VIPs from new visitors, and logs visit metrics into customer analytics tables.

### 3. 💬 Customer Sentiment Analysis
- **Pipeline**: Text Preprocessing, TF-IDF Vectorization, Logistic Regression Classifier.
- **Dataset**: Women's E-Commerce Clothing Reviews (~23,000 real customer reviews).
- **Functionality**: Analyzes customer review text, extracts emotional tone (Positive, Negative, Neutral), and generates clean metrics to help retailers address customer pain points quickly.

### 4. 🤖 Conversational AI Retail Support Chatbot
- **Engine**: Intent Classifier leveraging NLP Vectorization & Scikit-Learn Label Encoding.
- **Knowledge Base**: Structured JSON intents covering store policies, order tracking, returns, and product availability.
- **Functionality**: Understands user query intents and routes responses autonomously to resolve customer inquiries 24/7.

### 5. ⚡ FastAPI Microservices & REST Engine
- **Framework**: FastAPI + Uvicorn + Pydantic + Async I/O.
- **Endpoints**: Exposes lightweight REST endpoints (`/recognize-face`, `/analyze-sentiment`, `/chatbot`, `/classify-product`).
- **Deployment**: Configured for local execution as well as cloud deployment via Ngrok / Docker containerization.

---

## 📁 Repository Structure

```
Smart-Retail-AI/
├── notebooks/                                # Jupyter Notebooks (End-to-End Workflows)
│   ├── 01_Product_Image_Classification.ipynb # CNN Model Training & Evaluation
│   ├── 02_Face_Recognition.ipynb            # Facial Detection & Customer DB Creation
│   ├── 03_Sentiment_Analysis.ipynb           # NLP Review Sentiment Classification
│   ├── 04_Chatbot_Module.ipynb               # Intent Classification Engine
│   └── 05_FastAPI_Backend.ipynb              # API Integration & Server Setup
├── models/                                   # Serialized Pre-trained Artifacts
│   ├── product_classifier.keras              # Saved CNN model
│   ├── face_db.pkl                           # Customer biometrics database
│   ├── sentiment_model.pkl                   # Sentiment Logistic Regression model
│   ├── vectorizer.pkl                        # TF-IDF Vectorizer for reviews
│   ├── chatbot_model.pkl                     # Chatbot intent model
│   ├── chatbot_vectorizer.pkl                # Chatbot TF-IDF Vectorizer
│   └── label_encoder.pkl                     # Intent label encoder
├── datasets/                                 # Raw & Preprocessed Datasets
│   ├── Womens Clothing E-Commerce Reviews.csv# Review sentiment data
│   ├── intents.json                          # Chatbot intents dataset
│   └── customer_faces/                       # Face recognition samples
├── outputs/                                  # Log outputs & analytics tables
│   ├── clean_reviews.csv                     # Processed text dataset
│   ├── customer_visits.csv                   # Live visit log records
│   └── customer_mapping.csv                  # Customer ID mapping
├── app.py                                    # Standalone FastAPI Production Server
├── PROJECT_REPORT.md                         # Detailed Comprehensive Technical Report
├── requirements.txt                          # Python dependencies
└── .gitignore                                # Version control ignore file
```

---

## 🚀 Quickstart & Setup Guide

### 1. Prerequisites
Ensure Python 3.9+ is installed on your system.

```bash
git clone https://github.com/ishitagautam298-droid/Smart-Retail-AI.git
cd Smart-Retail-AI
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Launch FastAPI Backend Service
```bash
python3 app.py
# Or using Uvicorn directly:
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Access the interactive API documentation at: **`http://localhost:8000/docs`**

---

## 🔌 REST API Endpoints Overview

| Method | Endpoint | Description | Input Payload | Output |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | API Status & Health Check | None | System status JSON |
| `POST` | `/recognize-face` | Identifies customer face from image | Image file upload | `{ "status": "Returning customer", "customer_id": "CUST_001", "name": "Serena" }` |
| `POST` | `/analyze-sentiment` | Predicts review sentiment | `{ "text": "Great quality shirt!" }` | `{ "text": "...", "sentiment": "Positive" }` |
| `POST` | `/chatbot` | Classifies support intent | `{ "message": "Where is my order?" }` | `{ "message": "...", "intent": "track_order" }` |

---

## 🛡️ Ethical AI, Privacy & Security

Biometric processing and AI customer tracking require strict adherence to ethical guidelines:
1. **User Consent**: Facial data must only be collected with explicit user opt-in in store settings.
2. **Data Minimization**: Raw facial images are discarded after processing; only 128-d numerical embedding vectors are stored securely.
3. **Bias Mitigation**: Models are evaluated across diverse demographic datasets to avoid recognition disparities.
4. **Data Security**: Stored pickle files and databases are encrypted and protected against unauthorized access.

---

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Developed with ❤️ by **Ishita Gautam**.
