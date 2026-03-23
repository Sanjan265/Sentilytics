import yfinance as yf
from datetime import datetime, timedelta

def get_recent_stock_data(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        
        # We fetch 1 month and then take last 7 available days to handle weekends
        hist = stock.history(period="1mo")
        if hist.empty:
            return {"dates": [], "prices": [], "current_price": 0}
            
        dates = hist.index.strftime('%Y-%m-%d').tolist()[-7:]
        prices = hist['Close'].round(2).tolist()[-7:]
        
        return {
            "dates": dates,
            "prices": prices,
            "current_price": prices[-1] if prices else 0
        }
    except Exception as e:
        print(f"Error fetching stock data for {ticker}: {e}")
        return {"dates": [], "prices": [], "current_price": 0}
