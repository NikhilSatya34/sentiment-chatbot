"""
Day 4-5: Sentiment-Aware Gemini Chatbot
Integrates Gemini API with sentiment analysis
Bot responds differently based on user's sentiment
"""

import google.generativeai as genai
from sentiment_analysis import SentimentAnalyzer
import os
from dotenv import load_dotenv

env_path = r"D:\internship_tasks\task - 1\.env"

load_dotenv(env_path)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file!")

# Configure Gemini API
genai.configure(api_key=API_KEY)


class SentimentAwareChatbot:
    """
    A chatbot that detects user sentiment and responds appropriately
    """
    
    def __init__(self):
        """Initialize the chatbot and sentiment analyzer"""
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")        
        self.analyzer = SentimentAnalyzer()
        self.chat_history = []
        
        # System prompts for different sentiments
        self.system_prompts = {
            'positive': """You are a friendly and enthusiastic customer support chatbot. 
The user seems happy! Respond with warmth and enthusiasm. 
Keep your response concise and helpful. Match their positive energy! 😊""",
            
            'negative': """You are an empathetic and supportive customer support chatbot.
The user seems unhappy or frustrated. 
Respond with genuine empathy, acknowledge their feelings, and offer helpful solutions.
Be supportive and understanding. 💙""",
            
            'neutral': """You are a helpful and professional customer support chatbot.
The user has a neutral tone. 
Provide clear, informative, and professional assistance.
Be helpful and straightforward. 📋"""
        }
    
    def get_sentiment_aware_prompt(self, user_message, sentiment_info):
        """
        Create a prompt that considers sentiment
        
        Args:
            user_message (str): The user's message
            sentiment_info (dict): Sentiment analysis result
            
        Returns:
            str: Combined prompt with sentiment context
        """
        sentiment_key = sentiment_info['label_key']
        base_prompt = self.system_prompts[sentiment_key]
        
        # Add sentiment info for the model
        full_prompt = f"""{base_prompt}

User's message: {user_message}

Detected sentiment: {sentiment_info['label']} (Confidence: {sentiment_info['confidence']}%)

Respond to the user's message while keeping their emotional state in mind."""
        
        return full_prompt
    
    def chat(self, user_message):
        """
        Send message to Gemini and get sentiment-aware response
        
        Args:
            user_message (str): User's input message
            
        Returns:
            dict: {
                'user_message': str,
                'sentiment': dict,
                'bot_response': str,
                'response_tone': str
            }
        """
        # Analyze sentiment
        sentiment_info = self.analyzer.analyze(user_message)
        
        # Create sentiment-aware prompt
        prompt = self.get_sentiment_aware_prompt(user_message, sentiment_info)
        
        try:
            # Get response from Gemini
            response = self.model.generate_content(prompt)
            bot_response = response.text
        except Exception as e:
            bot_response = f"⚠️ Error: {str(e)}"
        
        # Store in history
        self.chat_history.append({
            'user': user_message,
            'sentiment': sentiment_info['label'],
            'bot': bot_response
        })
        
        return {
            'user_message': user_message,
            'sentiment': sentiment_info,
            'bot_response': bot_response,
            'response_tone': self.analyzer.get_response_tone(sentiment_info['label_key'])
        }
    
    def get_history(self):
        """Get conversation history"""
        return self.chat_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.chat_history = []


# Example usage
if __name__ == "__main__":
    print("🤖 Sentiment-Aware Chatbot Started!\n")
    print("=" * 70)
    
    chatbot = SentimentAwareChatbot()
    
    # Test messages with different sentiments
    test_messages = [
        "I absolutely love your service! It's fantastic!",
        "I'm really frustrated with this product, it doesn't work at all",
        "Can you help me with my account?"
    ]
    
    for message in test_messages:
        print(f"\n👤 User: {message}")
        print("-" * 70)
        
        result = chatbot.chat(message)
        
        print(f"😊 Sentiment Detected: {result['sentiment']['label']}")
        print(f"📊 Confidence: {result['sentiment']['confidence']}%")
        print(f"💬 Response Tone: {result['response_tone']}")
        print(f"\n🤖 Bot: {result['bot_response']}")
        print("=" * 70)
    
    print(f"\n✅ Conversation History ({len(chatbot.get_history())} messages)")
    for i, msg in enumerate(chatbot.get_history(), 1):
        print(f"{i}. User sentiment: {msg['sentiment']}")
