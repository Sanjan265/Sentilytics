from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

from src.reddit_client import RedditClient
from src.sentiment import analyze_sentiment
from src.stock_data import get_recent_stock_data
from src.predictor import generate_prediction

reddit_client = RedditClient()

app = FastAPI(title="Reddit Sentiment Stock Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/status")
async def get_status():
    return {"status": "online", "message": "Backend is running successfully."}

@app.get("/api/predict")
async def predict_stock(ticker: str):
    ticker = ticker.upper()
    
    # 1. Get real stock data (yfinance)
    stock_data = get_recent_stock_data(ticker)
    
    # 2. Get mock reddit data
    posts = reddit_client.get_recent_mentions(ticker)
    mentions = len(posts)
    
    # 3. Get mock sentiment
    sentiment_score = analyze_sentiment(posts)
    
    # 4. Generate prediction
    pred_data = generate_prediction(sentiment_score, mentions, stock_data)
    
    return {
        "ticker": ticker,
        "prediction": pred_data["prediction"],
        "confidence": pred_data["confidence"],
        "sentiment_score": sentiment_score,
        "recent_mentions": mentions,
        "historical_dates": stock_data["dates"],
        "historical_prices": stock_data["prices"]
    }

# Mount frontend files at the root
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
