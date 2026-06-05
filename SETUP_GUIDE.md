# Week 1: Sentiment Analysis Chatbot - Setup Guide

## Step 1: Create Project Folder
```bash
mkdir sentiment-chatbot
cd sentiment-chatbot
```

## Step 2: Create Virtual Environment (Optional but recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

## Step 3: Install Required Libraries
```bash
pip install google-generativeai
pip install textblob
pip install python-dotenv
pip install streamlit
```

## Step 4: Get Gemini API Key
1. Go to: https://aistudio.google.com/app/apikeys
2. Click "Create API Key"
3. Copy the key
4. Create a `.env` file in your project:
```
GEMINI_API_KEY=your_api_key_here
```

## Project Structure
```
sentiment-chatbot/
├── .env
├── sentiment_analysis.py
├── chatbot.py
├── app.py (Streamlit UI)
├── requirements.txt
└── README.md
```

## Requirements.txt Content
```
google-generativeai==0.3.0
textblob==0.17.1
python-dotenv==1.0.0
streamlit==1.28.0
```

## Quick Test (to verify setup)
```bash
python -c "import google.generativeai as genai; print('✅ Gemini API installed!')"
python -c "from textblob import TextBlob; print('✅ TextBlob installed!')"
```

If both print ✅, you're ready to go!
