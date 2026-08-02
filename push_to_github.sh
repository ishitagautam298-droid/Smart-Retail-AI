#!/bin/bash
set -e

TOKEN="$1"

if [ -z "$TOKEN" ]; then
  echo "Usage: ./push_to_github.sh <YOUR_GITHUB_PERSONAL_ACCESS_TOKEN>"
  echo ""
  echo "To get a GitHub Personal Access Token (PAT):"
  echo "1. Go to https://github.com/settings/tokens"
  echo "2. Click 'Generate new token (classic)'"
  echo "3. Check 'repo' scope and click Generate"
  echo "4. Run: ./push_to_github.sh ghp_xxxx"
  exit 1
fi

REPO_NAME="Smart-Retail-AI"
USER_NAME="ishitagautam298-droid"

echo "Creating GitHub repository '$REPO_NAME'..."
curl -s -X POST -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github.v3+json" -d "{\"name\": \"$REPO_NAME\", \"description\": \"AI-Powered Smart Retail & Customer Intelligence Platform (5 Modules: Image Classification, Facial Biometrics, Sentiment Analysis, Chatbot & FastAPI Backend)\"}" https://api.github.com/user/repos > /dev/null || true

echo "Setting git remote..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://${TOKEN}@github.com/${USER_NAME}/${REPO_NAME}.git"

echo "Pushing main branch to GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ Successfully uploaded $REPO_NAME to GitHub!"
echo "🔗 Repository URL: https://github.com/${USER_NAME}/${REPO_NAME}"
