def generate_prediction(sentiment_score: float, mentions: int, stock_data: dict):
    # Basic heuristic prediction logic based on sentiment and mentions
    if sentiment_score > 0.2:
        prediction = "BULLISH"
    elif sentiment_score < -0.2:
        prediction = "BEARISH"
    else:
        prediction = "NEUTRAL"
        
    # Calculate a mock confidence percentage based on parameters
    confidence = min(0.98, 0.5 + (abs(sentiment_score) * 0.4) + (mentions / 3000))
    
    return {
        "prediction": prediction,
        "confidence": round(confidence, 2) # up to two decimal places
    }
