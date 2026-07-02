# 🚀 QUICK START GUIDE - Week 1: Sentiment Analysis Chatbot

## ⏱️ 5-Minute Quick Start

### Step 1: Get API Key (2 minutes)
1. Go to: https://aistudio.google.com/app/apikeys
2. Click "Create API Key"
3. Copy the key

### Step 2: Setup Project (2 minutes)
```bash
# Clone/create folder
mkdir sentiment-chatbot
cd sentiment-chatbot

# Create virtual environment
python -m venv venv

# Activate it
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate

# Install libraries
pip install -r requirements.txt
```

### Step 3: Configure API Key (1 minute)
Create `.env` file with:
```
GEMINI_API_KEY=your_api_key_here
```

### Step 4: Run Application
```bash
streamlit run app.py
```

✅ Open browser to: http://localhost:8501

---

## 📋 File Checklist

Before running, ensure you have:
- [ ] `sentiment_analysis.py` - Sentiment detector
- [ ] `chatbot.py` - Gemini chatbot
- [ ] `app.py` - Streamlit UI
- [ ] `requirements.txt` - Dependencies
- [ ] `.env` - API key (YOU CREATE THIS)
- [ ] `README.md` - Documentation
- [ ] `.env.example` - Template

---

## 🧪 Test Each Component

### Test 1: Sentiment Analysis (Standalone)
```bash
python sentiment_analysis.py
```
**Expected Output:**
```
Message: I love this! It's amazing!
Sentiment: Positive 😊
Polarity: 0.85 (range: -1 to 1)
Confidence: 85%
Response Tone: friendly and enthusiastic
```

### Test 2: Chatbot (With Gemini)
```bash
python chatbot.py
```
**Expected Output:**
```
Message: I love this! It's amazing!
😊 Sentiment Detected: Positive 😊
📊 Confidence: 85%
💬 Response Tone: friendly and enthusiastic

🤖 Bot: [Gemini's enthusiastic response here]
```

### Test 3: Web Interface
```bash
streamlit run app.py
```
**Expected:**
- Opens at http://localhost:8501
- Chat interface ready
- Type test messages
- See sentiment detected
- See bot response

---

## 💡 Test Messages to Try

### Positive Sentiment
```
"I absolutely love this! It's amazing and wonderful!"
```

### Negative Sentiment
```
"This is terrible! I'm very frustrated with this product!"
```

### Neutral Sentiment
```
"Can you help me with my account balance?"
```

---

## 🎯 What Each File Does

| File | Purpose | Status |
|------|---------|--------|
| `sentiment_analysis.py` | Detects sentiment using TextBlob | ✅ Core |
| `chatbot.py` | Integrates Gemini API | ✅ Core |
| `app.py` | Web interface with Streamlit | ✅ UI |
| `requirements.txt` | Python dependencies | ✅ Config |
| `README.md` | Full documentation | ✅ Docs |
| `.env` | API key (YOU CREATE) | ⚠️ Important |
| `.env.example` | Template for .env | ✅ Template |

---

## 🔧 Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Test sentiment analyzer
python sentiment_analysis.py

# Test chatbot
python chatbot.py

# Run web app
streamlit run app.py

# Deactivate virtual environment
deactivate

# Update dependencies
pip install -r requirements.txt --upgrade
```

---

## ⚠️ Common Issues & Fixes

### "GEMINI_API_KEY not found"
```
❌ Problem: .env file missing or API key incorrect
✅ Solution: Create .env with your actual API key
```

### "Module not found: textblob"
```
❌ Problem: Dependencies not installed
✅ Solution: pip install -r requirements.txt
```

### "TextBlob corpora missing"
```
❌ Problem: Sentiment analysis data not downloaded
✅ Solution: python -m textblob.download_corpora
```

### "Port 8501 already in use"
```
❌ Problem: Another Streamlit app running
✅ Solution: streamlit run app.py --server.port 8502
```

---

## 📊 Week 1 Summary

### Completed Tasks
- ✅ Day 1-2: Setup & Environment configuration
- ✅ Day 3: Sentiment analysis module
- ✅ Day 4-5: Chatbot integration with Gemini
- ✅ Day 6: Streamlit web interface
- ✅ Day 7: Testing & Documentation

### Code Statistics
- **Lines of Code:** ~700
- **Functions:** 15+
- **Features:** 8
- **Test Cases:** 3+

### Ready for Submission
All Week 1 code is ready for GitHub upload!

---

## 📦 Next Steps

1. **Complete Week 1:** Test everything thoroughly
2. **Create GitHub repo:** Upload all files (except .env)
3. **Update README:** Add your results & metrics
4. **Document metrics:** Sentiment accuracy, response quality
5. **Prepare for Week 2:** Medical Q&A Chatbot

---

## 🎓 Learning Outcomes

By completing Week 1, you'll understand:
- ✅ Sentiment analysis with TextBlob
- ✅ LLM API integration (Gemini)
- ✅ Sentiment-aware prompting
- ✅ Streamlit for web interfaces
- ✅ Python project structure
- ✅ Environment configuration

---

## 📞 Need Help?

**Email:** training@elevanceskills.com

Include:
- Error message (if any)
- Python version: `python --version`
- Steps you took
- Screenshot of the issue

