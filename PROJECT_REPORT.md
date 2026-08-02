# 📊 COMPREHENSIVE PROJECT REPORT
## AI-Powered Smart Retail & Customer Intelligence Platform

**Author**: Ishita Gautam  
**Date**: August 2026  
**System Architecture**: Multi-Modal Artificial Intelligence Platform (Computer Vision, NLP, Biometrics & REST Microservices)

---

## Executive Summary

Modern physical retail environments face growing challenges from e-commerce platforms, particularly regarding personalized customer experiences, instant service resolution, and real-time inventory intelligence. The **Smart Retail & Customer Intelligence Platform** bridges this gap by deploying artificial intelligence models directly into physical retail workflows.

The platform integrates five core technical pillars:
1. **Product Image Classification**: Automated visual sorting of apparel items using a Convolutional Neural Network (CNN) trained on Fashion-MNIST.
2. **Biometric Customer Recognition**: Facial identification and visit logging using 128-dimensional deep feature embeddings from OpenCV and `face_recognition`.
3. **Sentiment Intelligence**: Natural Language Processing (NLP) over ~23,000 retail reviews using TF-IDF feature extraction and Logistic Regression.
4. **Conversational Support Bot**: Intent classification engine linking user queries with automated retail resolution tags.
5. **Microservice API Architecture**: High-performance RESTful API built on FastAPI to expose model inference endpoints asynchronously to mobile, web, and IoT POS terminals.

---

## 1. Module 1: Product Image Classification (CNN)

### 1.1 Problem Statement
Manual tagging and visual entry of incoming clothing inventory is labor-intensive and prone to human error. Automated image classification enables instant item identification.

### 1.2 Dataset & Preprocessing
- **Dataset**: Fashion-MNIST (70,000 grayscale images, 28x28 pixels, 10 categories).
- **Classes**: T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot.
- **Normalization**: Pixel values scaled from `[0, 255]` to `[0.0, 1.0]`. Reshaped to `(28, 28, 1)` for 2D convolutional layers.

### 1.3 Model Topology & Hyperparameters
- **Input Layer**: `(28, 28, 1)`
- **Conv2D Layer 1**: 32 filters, 3x3 kernel, ReLU activation
- **MaxPooling2D Layer 1**: 2x2 pool size
- **Conv2D Layer 2**: 64 filters, 3x3 kernel, ReLU activation
- **MaxPooling2D Layer 2**: 2x2 pool size
- **Flatten Layer**
- **Dense Layer**: 128 units, ReLU activation, Dropout(0.2)
- **Output Layer**: 10 units, Softmax activation
- **Optimizer**: Adam (`learning_rate=0.001`)
- **Loss Function**: Sparse Categorical Crossentropy

### 1.4 Results & Metrics
- **Training Accuracy**: ~92.4%
- **Validation/Test Accuracy**: ~89.6%
- **Model Size**: 2.7 MB (`product_classifier.keras`)

---

## 2. Module 2: Facial Recognition & Customer Visit Intelligence

### 2.1 Problem Statement
Retail stores often lack historical recognition of returning VIP customers, preventing staff from providing tailored recommendations upon store entry.

### 2.2 Methodology & Pipeline
1. **Face Detection**: Histogram of Oriented Gradients (HOG) + OpenCV Haar Cascades to locate human faces in video/image feeds.
2. **Feature Extraction**: Deep Metric Learning via ResNet-style neural network generating 128-dimensional facial embedding vectors per face.
3. **Database Building**: Pre-computation and serialization of target customer embeddings into a persistent dictionary structure (`face_db.pkl`).
4. **Matching Logic**: Euclidean distance calculation between input face embedding and database records with a strict matching tolerance (`threshold = 0.6`).
5. **Analytics Logging**: Automated recording of customer visit timestamps, visit frequency counts, and returning vs. new visitor flags saved to `customer_visits.csv`.

---

## 3. Module 3: Customer Sentiment Analysis (NLP)

### 3.1 Problem Statement
Retailers receive thousands of text reviews. Manually analyzing feedback to identify customer dissatisfaction is inefficient.

### 3.2 Dataset & Pipeline
- **Dataset**: Women's Clothing E-Commerce Reviews dataset (23,486 reviews).
- **Text Cleaning**: Lowercasing, removal of punctuation, special characters, and stop words.
- **Labeling Logic**: Star rating mapping ($\ge 4$ stars = Positive, $\le 2$ stars = Negative, 3 stars = Neutral).
- **Vectorization**: TF-IDF (Term Frequency - Inverse Document Frequency) max features = 5,000, n-gram range `(1, 2)`.
- **Classification Model**: Logistic Regression (`max_iter=1000`).

### 3.3 Evaluation Metrics
- **Accuracy**: ~88.5%
- **Precision (Positive Sentiment)**: 0.91
- **Recall (Positive Sentiment)**: 0.94
- **Serialized Artifacts**: `sentiment_model.pkl` (120 KB), `vectorizer.pkl` (183 KB).

---

## 4. Module 4: Intelligent Support Chatbot

### 4.1 Problem Statement
Common retail inquiries (e.g., store hours, order status, return policies) consume significant customer support agent bandwidth.

### 4.2 Pipeline
- **Intents Definition**: `intents.json` mapping intent tags (`track_order`, `return_policy`, `store_hours`, `product_inquiry`) to example user training queries.
- **Encoding**: `LabelEncoder` maps textual intent classes to integers.
- **Model**: Logistic Regression / Linear Support Vector Classifier over TF-IDF vector representations of user queries.
- **Inference**: Predicts intent tag from user input message, enabling immediate response retrieval.

---

## 5. Module 5: FastAPI Microservice & Backend Architecture

### 5.1 Architecture Design
The backend is structured as a asynchronous RESTful service using **FastAPI** and **Uvicorn**:
- Async file handling for image uploads (`UploadFile`).
- Pydantic data validation for JSON text payloads.
- Modular loading of pre-trained pickle and Keras model weights at server startup.

### 5.2 Endpoints Specification
- `GET /`: Status check and service discovery.
- `GET /health`: Model availability and health status.
- `POST /recognize-face`: Multipart form-data image upload $\rightarrow$ Customer ID and status.
- `POST /analyze-sentiment`: JSON text payload $\rightarrow$ Predicted sentiment tag.
- `POST /chatbot`: JSON chat message $\rightarrow$ Predicted intent classification tag.

---

## 6. Ethical & Responsible AI Considerations

Processing human biometrics in public commercial spaces requires strict compliance with privacy standards (such as GDPR, CCPA, and BIPA):
1. **Consent & Transparency**: Facial recognition should operate on an opt-in basis for VIP programs.
2. **Embedding Storage**: Raw facial images are discarded immediately after feature extraction; only non-invertible numerical embeddings are stored.
3. **Fairness**: Training datasets for facial recognition must encompass balanced demographic representations to eliminate algorithmic bias.

---

## 7. Conclusion & Future Roadmap

The **Smart Retail & Customer Intelligence Platform** demonstrates how multi-modal AI models can be seamlessly unified into an integrated, operational microservices system.

### Recommended Next Steps:
1. **Edge AI Deployment**: Port facial detection and CNN models to edge devices (e.g., Raspberry Pi 4 / NVIDIA Jetson Nano) for zero-latency camera stream processing.
2. **Recommendation Engine**: Combine customer recognition data with purchase history to generate real-time product recommendations on digital store signage.
3. **Containerization**: Package the FastAPI microservice into a Docker container for cloud scaling on Kubernetes or AWS ECS.
