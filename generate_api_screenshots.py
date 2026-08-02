import os
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig_dir = "/Users/ishitagautam/.gemini/antigravity/scratch/Smart-Retail-AI/images"
os.makedirs(fig_dir, exist_ok=True)

# 1. FastAPI Swagger UI Interactive Documentation Mock
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.axis('off')

# Window frame
rect_bg = plt.Rectangle((0, 0), 1, 1, facecolor='#F8F9FA', edgecolor='#CCCCCC', lw=2)
ax.add_patch(rect_bg)

# Top Bar
rect_bar = plt.Rectangle((0, 0.9), 1, 0.1, facecolor='#1B1B1B', edgecolor='none')
ax.add_patch(rect_bar)
ax.text(0.03, 0.94, "Smart Retail AI API  |  OpenAPI 3.0 / Swagger UI  [http://localhost:8000/docs]", 
        color='#85EA2D', weight='bold', fontsize=11, va='center')

# Title section
ax.text(0.04, 0.83, "Smart Retail & Customer Intelligence API", fontsize=16, weight='bold', color='#2B2B2B')
ax.text(0.04, 0.78, "v1.0.0  [ OAS 3.0 ]  /openapi.json", fontsize=10, color='#666666')
ax.text(0.04, 0.73, "Multi-modal AI backend providing face recognition, image classification, sentiment analysis & chatbot intents.", 
        fontsize=9, color='#444444')

# Endpoint Cards
endpoints_ui = [
    ("GET", "/health", "System & Model Availability Health Check", "#61AFFE"),
    ("POST", "/recognize-face", "Biometric Customer Identification & Visit Logging", "#49CC90"),
    ("POST", "/analyze-sentiment", "NLP E-Commerce Review Sentiment Classifier", "#49CC90"),
    ("POST", "/chatbot", "Customer Support Query Intent Engine", "#49CC90"),
    ("POST", "/classify-product", "CNN Fashion Apparel Image Classifier", "#49CC90")
]

for i, (method, path, desc, col) in enumerate(endpoints_ui):
    y = 0.58 - i * 0.11
    # Card Background
    card = plt.Rectangle((0.04, y), 0.92, 0.09, facecolor='#EBF4FB' if method=="GET" else '#E8F6F0', 
                         edgecolor=col, lw=1.5)
    ax.add_patch(card)
    
    # Method Badge
    badge = plt.Rectangle((0.05, y+0.015), 0.11, 0.06, facecolor=col, edgecolor='none')
    ax.add_patch(badge)
    ax.text(0.105, y+0.045, method, color='white', weight='bold', fontsize=10, ha='center', va='center')
    
    # Path & Desc
    ax.text(0.18, y+0.045, path, color='#2B2B2B', weight='bold', fontsize=10, va='center')
    ax.text(0.42, y+0.045, desc, color='#555555', fontsize=8.5, va='center')
    ax.text(0.92, y+0.045, "Try it out  ▼", color='#333333', fontsize=8, ha='right', va='center')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "api_docs_swagger.png"), bbox_inches='tight', dpi=300)
plt.close()

# 2. API Endpoint Sample Payload & Response UI Graphic
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)

# Left: /analyze-sentiment
ax1.axis('off')
rect1 = plt.Rectangle((0, 0), 1, 1, facecolor='#1E1E1E', edgecolor='#49CC90', lw=2)
ax1.add_patch(rect1)
ax1.text(0.05, 0.91, "POST  /analyze-sentiment", color='#49CC90', weight='bold', fontsize=11)
ax1.text(0.05, 0.82, "REQUEST PAYLOAD (JSON):", color='#AAAAAA', fontsize=8.5, weight='bold')
ax1.text(0.05, 0.68, "{\n  \"text\": \"This shirt fits perfectly\n   and the quality is amazing!\"\n}", 
         color='#CE9178', fontfamily='monospace', fontsize=9)

ax1.text(0.05, 0.48, "RESPONSE STATUS: 200 OK (12.5 ms)", color='#4EC9B0', fontsize=8.5, weight='bold')
ax1.text(0.05, 0.26, "{\n  \"text\": \"This shirt fits...\",\n  \"sentiment\": \"Positive\",\n  \"confidence\": 0.94\n}", 
         color='#9CDCFE', fontfamily='monospace', fontsize=9)

# Right: /chatbot
ax2.axis('off')
rect2 = plt.Rectangle((0, 0), 1, 1, facecolor='#1E1E1E', edgecolor='#49CC90', lw=2)
ax2.add_patch(rect2)
ax2.text(0.05, 0.91, "POST  /chatbot", color='#49CC90', weight='bold', fontsize=11)
ax2.text(0.05, 0.82, "REQUEST PAYLOAD (JSON):", color='#AAAAAA', fontsize=8.5, weight='bold')
ax2.text(0.05, 0.68, "{\n  \"message\": \"Where is my order?\n   Can I track shipping?\"\n}", 
         color='#CE9178', fontfamily='monospace', fontsize=9)

ax2.text(0.05, 0.48, "RESPONSE STATUS: 200 OK (18.2 ms)", color='#4EC9B0', fontsize=8.5, weight='bold')
ax2.text(0.05, 0.26, "{\n  \"message\": \"Where is my...\",\n  \"intent\": \"track_order\",\n  \"action\": \"redirect_to_tracking\"\n}", 
         color='#9CDCFE', fontfamily='monospace', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "api_payloads_demo.png"), bbox_inches='tight', dpi=300)
plt.close()

print("Generated API Swagger & Payload Graphics successfully in images/")
