from textblob import TextBlob

class SentimentAnalyzer:
    """
    Analyzes sentiment of text using TextBlob
    Returns: sentiment label (Positive/Negative/Neutral) and confidence score
    """
    
    def __init__(self):
        """Initialize the sentiment analyzer"""
        self.sentiment_labels = {
            'positive': 'Positive 😊',
            'negative': 'Negative 😞',
            'neutral': 'Neutral 😐'
        }
    
    def analyze(self, text):
        """
        Analyze sentiment of given text
        
        Args:
            text (str): User message to analyze
            
        Returns:
            dict: {
                'label': 'Positive/Negative/Neutral',
                'polarity': float (-1 to 1),
                'subjectivity': float (0 to 1),
                'confidence': float (0 to 100)
            }
        """
        # Create TextBlob object
        blob = TextBlob(text)
        
        # Get polarity (-1 to 1)
        polarity = blob.sentiment.polarity
        
        # Get subjectivity (0 to 1)
        subjectivity = blob.sentiment.subjectivity
        
        # Determine sentiment label based on polarity
        if polarity > 0.1:
            label = 'positive'
            # Confidence = how strong is the positive sentiment
            confidence = abs(polarity) * 100
        elif polarity < -0.1:
            label = 'negative'
            # Confidence = how strong is the negative sentiment
            confidence = abs(polarity) * 100
        else:
            label = 'neutral'
            confidence = (1 - subjectivity) * 100
        
        return {
            'label': self.sentiment_labels[label],
            'label_key': label,
            'polarity': round(polarity, 2),
            'subjectivity': round(subjectivity, 2),
            'confidence': round(confidence, 2)
        }
    
    def get_response_tone(self, sentiment_label):
        """
        Get suggested response tone based on sentiment
        
        Args:
            sentiment_label (str): 'positive', 'negative', or 'neutral'
            
        Returns:
            str: Suggested tone for the response
        """
        tones = {
            'positive': 'friendly and enthusiastic',
            'negative': 'empathetic and supportive',
            'neutral': 'helpful and informative'
        }
        return tones.get(sentiment_label, 'helpful')


# Example Usage
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    
    # Test messages
    test_messages = [
        "I love this! It's amazing!",
        "This is terrible, I hate it",
        "What time is the meeting?"
    ]
    
    print("=" * 60)
    print("SENTIMENT ANALYSIS TEST")
    print("=" * 60)
    
    for message in test_messages:
        result = analyzer.analyze(message)
        print(f"\nMessage: {message}")
        print(f"Sentiment: {result['label']}")
        print(f"Polarity: {result['polarity']} (range: -1 to 1)")
        print(f"Confidence: {result['confidence']}%")
        print(f"Response Tone: {analyzer.get_response_tone(result['label_key'])}")
        print("-" * 60)
