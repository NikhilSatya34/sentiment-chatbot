import streamlit as st
from chatbot import SentimentAwareChatbot
import json
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Sentiment-Aware Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .sentiment-positive {
        color: #28a745;
        font-weight: bold;
    }
    .sentiment-negative {
        color: #dc3545;
        font-weight: bold;
    }
    .sentiment-neutral {
        color: #6c757d;
        font-weight: bold;
    }
    .metric-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = SentimentAwareChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "sentiment_stats" not in st.session_state:
    st.session_state.sentiment_stats = {"positive": 0, "negative": 0, "neutral": 0}


# Sidebar
with st.sidebar:
    st.title("📊 Chat Statistics")
    
    # Display stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("😊 Positive", st.session_state.sentiment_stats["positive"])
    with col2:
        st.metric("😞 Negative", st.session_state.sentiment_stats["negative"])
    with col3:
        st.metric("😐 Neutral", st.session_state.sentiment_stats["neutral"])
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", key="clear_history"):
        st.session_state.messages = []
        st.session_state.sentiment_stats = {"positive": 0, "negative": 0, "neutral": 0}
        st.session_state.chatbot.clear_history()
        st.success("Chat history cleared!")
    
    st.divider()
    
    # About section
    st.markdown("""
    ### About This Chatbot
    
    This is a **Sentiment-Aware Chatbot** that:
    - 🎯 Detects your emotional tone
    - 💭 Analyzes sentiment (Positive/Negative/Neutral)
    - 💬 Responds with appropriate tone
    - 📊 Tracks conversation statistics
    
    **Technology Used:**
    - 🤖 Google Gemini API
    - 🔍 TextBlob Sentiment Analysis
    - 🌐 Streamlit Framework
    """)


# Main content
st.title("🤖 Sentiment-Aware Chatbot")
st.markdown("*A chatbot that understands your emotions and responds accordingly*")

# Display chat history
st.subheader("💬 Conversation")

if not st.session_state.messages:
    st.info("👋 Start a conversation! The bot will detect your sentiment and respond appropriately.")
else:
    for message in st.session_state.messages:
        # User message
        with st.container():
            col1, col2 = st.columns([1, 9])
            with col1:
                st.write("👤")
            with col2:
                st.markdown(f"**You:** {message['user_message']}")
            
            # Sentiment info
            sentiment = message['sentiment']
            col1, col2, col3 = st.columns([2, 2, 2])
            with col1:
                sentiment_emoji = {
                    'Positive 😊': '😊',
                    'Negative 😞': '😞',
                    'Neutral 😐': '😐'
                }
                st.caption(f"{sentiment_emoji.get(sentiment['label'], '🤔')} {sentiment['label']}")
            with col2:
                st.caption(f"📊 Confidence: {sentiment['confidence']}%")
            with col3:
                st.caption(f"💬 Tone: {message.get('response_tone', 'helpful')}")
        
        # Bot response
        with st.container():
            col1, col2 = st.columns([1, 9])
            with col1:
                st.write("🤖")
            with col2:
                st.markdown(f"**Bot:** {message['bot_response']}")
        
        st.divider()


# Input area
st.subheader("✍️ Your Message")
user_input = st.text_input(
    "Type your message here:",
    placeholder="Tell me how you feel...",
    label_visibility="collapsed"
)

# Send button and advanced options in columns
col1, col2 = st.columns([5, 1])

with col1:
    if st.button("📤 Send Message", key="send", use_container_width=True):
        if user_input.strip():
            with st.spinner("🤔 Analyzing sentiment and generating response..."):
                # Get response from chatbot
                response = st.session_state.chatbot.chat(user_input)
                
                # Store in session state
                st.session_state.messages.append({
                    'user_message': user_input,
                    'sentiment': response['sentiment'],
                    'bot_response': response['bot_response'],
                    'response_tone': response['response_tone'],
                    'timestamp': datetime.now().isoformat()
                })
                
                # Update statistics
                sentiment_key = response['sentiment']['label_key']
                st.session_state.sentiment_stats[sentiment_key] += 1
            
            st.rerun()
        else:
            st.warning("Please enter a message!")

with col2:
    if st.button("⚙️", key="settings", help="Settings"):
        st.write("Settings coming soon!")


# Footer with metrics
st.divider()
st.subheader("📈 Session Metrics")

col1, col2, col3, col4 = st.columns(4)

total_messages = len(st.session_state.messages)
if total_messages > 0:
    positive_pct = (st.session_state.sentiment_stats["positive"] / total_messages) * 100
    negative_pct = (st.session_state.sentiment_stats["negative"] / total_messages) * 100
    neutral_pct = (st.session_state.sentiment_stats["neutral"] / total_messages) * 100
else:
    positive_pct = negative_pct = neutral_pct = 0

with col1:
    st.metric("📝 Total Messages", total_messages)
with col2:
    st.metric("😊 Positive %", f"{positive_pct:.1f}%")
with col3:
    st.metric("😞 Negative %", f"{negative_pct:.1f}%")
with col4:
    st.metric("😐 Neutral %", f"{neutral_pct:.1f}%")


# Instructions
with st.expander("📖 How to Use"):
    st.markdown("""
    1. **Type a message** in the input box
    2. **Click "Send Message"** or press Enter
    3. The bot will:
       - 🎯 Detect your sentiment (happy, sad, neutral)
       - 💭 Analyze the emotional tone
       - 💬 Respond with an appropriate tone
    4. **View statistics** in the sidebar
    5. **Clear history** to start fresh
    
    ### Example Messages to Try:
    - "I love this! It's amazing!" (Positive)
    - "I'm so frustrated with this!" (Negative)
    - "What time is the meeting?" (Neutral)
    """)
