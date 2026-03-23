import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import logging

# Ensure the VADER lexicon package is downloaded on the internal system
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

def analyze_sentiment(posts):
    # Analyzes genuine sentiment across Reddit posts using VADER machine learning
    if not posts:
        return 0.0
        
    try:
        analyzer = SentimentIntensityAnalyzer()
        compound_scores = []
        
        for post in posts:
            # Skip empty entries
            if not post.strip():
                continue
                
            # polarity_scores returns dict: {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
            vs = analyzer.polarity_scores(post)
            compound_scores.append(vs['compound'])
            
        if not compound_scores:
            return 0.0
            
        # Calculate the mathematical average sentiment across all collected mentions
        avg_score = sum(compound_scores) / len(compound_scores)
        
        # Round to 2 decimal places for UI
        return round(avg_score, 2)
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        return 0.0
