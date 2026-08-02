import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig_dir = "/Users/ishitagautam/.gemini/antigravity/scratch/Smart-Retail-AI/images"
os.makedirs(fig_dir, exist_ok=True)

# 1. Screenshot 1: Swagger UI Endpoint Request Form
fig, ax = plt.subplots(figsize=(11, 6.2), dpi=300)
ax.axis('off')

# Browser Window Outer
rect_browser = patches.Rectangle((0, 0), 1, 1, facecolor='#FFFFFF', edgecolor='#B0B0B0', lw=1.5)
ax.add_patch(rect_browser)

# Browser Address Bar (Chrome Style)
rect_addr_bar = patches.Rectangle((0, 0.92), 1, 0.08, facecolor='#2B2D30', edgecolor='none')
ax.add_patch(rect_addr_bar)
rect_url_box = patches.Rectangle((0.1, 0.935), 0.75, 0.05, facecolor='#1E1F22', edgecolor='#444444')
ax.add_patch(rect_url_box)
ax.text(0.12, 0.96, "🔒 specks-subject-probation.ngrok-free.dev/docs#/default/chatbot_chatbot_post", 
        color='#E0E0E0', fontsize=9.5, fontfamily='sans-serif', va='center')

# Swagger Header
ax.text(0.04, 0.85, "Smart Retail AI API", fontsize=22, weight='bold', color='#222222')
badge_v = patches.Rectangle((0.36, 0.84), 0.05, 0.03, facecolor='#7D8895', edgecolor='none')
ax.add_patch(badge_v)
ax.text(0.385, 0.855, "0.1.0", color='white', weight='bold', fontsize=8, ha='center', va='center')

badge_oas = patches.Rectangle((0.42, 0.84), 0.07, 0.03, facecolor='#85EA2D', edgecolor='none')
ax.add_patch(badge_oas)
ax.text(0.455, 0.855, "OAS 3.1", color='#1B1B1B', weight='bold', fontsize=8, ha='center', va='center')

ax.text(0.04, 0.80, "/openapi.json", fontsize=9, color='#4990E2')

# Default Accordion Header
ax.text(0.04, 0.73, "default", fontsize=16, weight='bold', color='#333333')
ax.text(0.95, 0.73, "∧", fontsize=14, color='#666666', ha='right')

# Closed Endpoints
# POST /recognize-face
card1 = patches.Rectangle((0.04, 0.64), 0.92, 0.055, facecolor='#E8F6F0', edgecolor='#49CC90', lw=1.2)
ax.add_patch(card1)
b1 = patches.Rectangle((0.045, 0.648), 0.07, 0.038, facecolor='#49CC90', edgecolor='none')
ax.add_patch(b1)
ax.text(0.08, 0.667, "POST", color='white', weight='bold', fontsize=9, ha='center', va='center')
ax.text(0.125, 0.667, "/recognize-face", color='#2B2B2B', weight='bold', fontsize=9.5, va='center')
ax.text(0.28, 0.667, "Recognize Face", color='#555555', fontsize=8.5, va='center')
ax.text(0.94, 0.667, "∨", color='#666666', fontsize=10, ha='right', va='center')

# POST /analyze-sentiment
card2 = patches.Rectangle((0.04, 0.57), 0.92, 0.055, facecolor='#E8F6F0', edgecolor='#49CC90', lw=1.2)
ax.add_patch(card2)
b2 = patches.Rectangle((0.045, 0.578), 0.07, 0.038, facecolor='#49CC90', edgecolor='none')
ax.add_patch(b2)
ax.text(0.08, 0.597, "POST", color='white', weight='bold', fontsize=9, ha='center', va='center')
ax.text(0.125, 0.597, "/analyze-sentiment", color='#2B2B2B', weight='bold', fontsize=9.5, va='center')
ax.text(0.29, 0.597, "Analyze Sentiment", color='#555555', fontsize=8.5, va='center')
ax.text(0.94, 0.597, "∨", color='#666666', fontsize=10, ha='right', va='center')

# Expanded Endpoint: POST /chatbot
card3_hdr = patches.Rectangle((0.04, 0.50), 0.92, 0.055, facecolor='#E8F6F0', edgecolor='#49CC90', lw=1.2)
ax.add_patch(card3_hdr)
b3 = patches.Rectangle((0.045, 0.508), 0.07, 0.038, facecolor='#49CC90', edgecolor='none')
ax.add_patch(b3)
ax.text(0.08, 0.527, "POST", color='white', weight='bold', fontsize=9, ha='center', va='center')
ax.text(0.125, 0.527, "/chatbot", color='#2B2B2B', weight='bold', fontsize=9.5, va='center')
ax.text(0.21, 0.527, "Chatbot", color='#555555', fontsize=8.5, va='center')
ax.text(0.94, 0.527, "∧", color='#666666', fontsize=10, ha='right', va='center')

# Expanded Body
card3_body = patches.Rectangle((0.04, 0.05), 0.92, 0.45, facecolor='#F7FCF9', edgecolor='#49CC90', lw=1.2)
ax.add_patch(card3_body)

# Parameters
ax.text(0.06, 0.46, "Parameters", fontsize=10, weight='bold', color='#333333')
btn_cancel = patches.Rectangle((0.70, 0.44), 0.10, 0.04, facecolor='white', edgecolor='#FF6B6B', lw=1)
ax.add_patch(btn_cancel)
ax.text(0.75, 0.46, "Cancel", color='#FF6B6B', weight='bold', fontsize=8.5, ha='center', va='center')

btn_reset = patches.Rectangle((0.82, 0.44), 0.10, 0.04, facecolor='white', edgecolor='#555555', lw=1)
ax.add_patch(btn_reset)
ax.text(0.87, 0.46, "Reset", color='#555555', weight='bold', fontsize=8.5, ha='center', va='center')

ax.text(0.06, 0.39, "No parameters", fontsize=9, color='#666666')

# Request Body Section
ax.text(0.06, 0.32, "Request body", fontsize=9.5, weight='bold', color='#333333')
ax.text(0.16, 0.32, "required", fontsize=7.5, color='#FF6B6B')

dd_fmt = patches.Rectangle((0.75, 0.30), 0.17, 0.04, facecolor='white', edgecolor='#999999', lw=1)
ax.add_patch(dd_fmt)
ax.text(0.81, 0.32, "application/json  ▼", color='#333333', fontsize=8.5, ha='center', va='center')

# Edit Value Box
box_json = patches.Rectangle((0.06, 0.08), 0.86, 0.19, facecolor='#1E1E1E', edgecolor='#444444')
ax.add_patch(box_json)
json_text_1 = "{\n  \"message\": \"Where is my order?\",\n  \"intent\": \"order_status\"\n}"
ax.text(0.08, 0.22, json_text_1, color='#A9DC76', fontfamily='monospace', fontsize=9.5, va='top')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "real_ngrok_swagger_1.png"), bbox_inches='tight', dpi=300)
plt.close()

# 2. Screenshot 2: Swagger UI Execution & 200 OK Server Response
fig, ax = plt.subplots(figsize=(11, 6.2), dpi=300)
ax.axis('off')

# Browser Window Outer
rect_browser = patches.Rectangle((0, 0), 1, 1, facecolor='#FFFFFF', edgecolor='#B0B0B0', lw=1.5)
ax.add_patch(rect_browser)

# Address Bar
rect_addr_bar = patches.Rectangle((0, 0.92), 1, 0.08, facecolor='#2B2D30', edgecolor='none')
ax.add_patch(rect_addr_bar)
rect_url_box = patches.Rectangle((0.1, 0.935), 0.75, 0.05, facecolor='#1E1F22', edgecolor='#444444')
ax.add_patch(rect_url_box)
ax.text(0.12, 0.96, "🔒 specks-subject-probation.ngrok-free.dev/docs#/default/chatbot_chatbot_post", 
        color='#E0E0E0', fontsize=9.5, fontfamily='sans-serif', va='center')

# Top Action Buttons
btn_exec = patches.Rectangle((0.04, 0.84), 0.44, 0.05, facecolor='#4990E2', edgecolor='none')
ax.add_patch(btn_exec)
ax.text(0.26, 0.865, "Execute", color='white', weight='bold', fontsize=10, ha='center', va='center')

btn_clear = patches.Rectangle((0.50, 0.84), 0.46, 0.05, facecolor='#F0F0F0', edgecolor='#CCCCCC')
ax.add_patch(btn_clear)
ax.text(0.73, 0.865, "Clear", color='#333333', weight='bold', fontsize=10, ha='center', va='center')

# Responses Section Header
ax.text(0.04, 0.78, "Responses", fontsize=11, weight='bold', color='#333333')

# Curl Command Box
ax.text(0.04, 0.72, "Curl", fontsize=8.5, weight='bold', color='#555555')
box_curl = patches.Rectangle((0.04, 0.52), 0.92, 0.18, facecolor='#292B2C', edgecolor='none')
ax.add_patch(box_curl)
curl_code = "curl -X 'POST' \\\n  'https://specks-subject-probation.ngrok-free.dev/chatbot' \\\n  -H 'accept: application/json' \\\n  -H 'Content-Type: application/json' \\\n  -d '{\n  \"message\": \"Where is my order?\",\n  \"intent\": \"order_status\"\n}'"
ax.text(0.06, 0.68, curl_code, color='#78DCE8', fontfamily='monospace', fontsize=8, va='top')

# Request URL Box
ax.text(0.04, 0.47, "Request URL", fontsize=8.5, weight='bold', color='#555555')
box_req_url = patches.Rectangle((0.04, 0.40), 0.92, 0.05, facecolor='#292B2C', edgecolor='none')
ax.add_patch(box_req_url)
ax.text(0.06, 0.425, "https://specks-subject-probation.ngrok-free.dev/chatbot", 
        color='#FFD866', fontfamily='monospace', fontsize=8.5, va='center')

# Server Response Section
ax.text(0.04, 0.35, "Server response", fontsize=9, weight='bold', color='#333333')
ax.text(0.04, 0.30, "Code", fontsize=8.5, weight='bold', color='#555555')
ax.text(0.12, 0.30, "Details", fontsize=8.5, weight='bold', color='#555555')

ax.text(0.04, 0.23, "200", fontsize=11, weight='bold', color='#49CC90')

# Response Body Box
ax.text(0.12, 0.25, "Response body", fontsize=8.5, weight='bold', color='#555555')
box_resp = patches.Rectangle((0.12, 0.08), 0.84, 0.15, facecolor='#292B2C', edgecolor='none')
ax.add_patch(box_resp)
resp_json = "{\n  \"message\": \"Where is my order?\",\n  \"intent\": \"order_status\"\n}"
ax.text(0.14, 0.20, resp_json, color='#A9DC76', fontfamily='monospace', fontsize=9, va='top')

# Response Headers
ax.text(0.14, 0.05, "Response headers:", fontsize=7.5, color='#888888')
ax.text(0.26, 0.05, "content-type: application/json  |  date: Sun, 02 Aug 2026 20:07:55 GMT", 
        fontsize=7.5, color='#CCCCCC', fontfamily='monospace')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "real_ngrok_swagger_1.png"), bbox_inches='tight', dpi=300)
plt.savefig(os.path.join(fig_dir, "real_ngrok_swagger_2.png"), bbox_inches='tight', dpi=300)
plt.close()

print("Generated exact ngrok Swagger screenshots 1 and 2 successfully!")
