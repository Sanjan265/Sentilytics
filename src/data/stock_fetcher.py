import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_stock_data(ticker="AAPL", period="1mo", interval="1d"):
    """
    Fetches historical stock data using yfinance.
    """
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period, interval=interval)
        
        if df.empty:
            return pd.DataFrame()
            
        # Reset index to make Date a column instead of index
        df = df.reset_index()
        
        # Ensure date format is consistent, robustly checking for timezone awareness
        if df['Date'].dt.tz is not None:
            df['Date'] = df['Date'].dt.tz_convert(None)
            
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        
        return df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    except Exception as e:
        print(f"Error fetching stock data for {ticker}: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df = fetch_stock_data("AAPL", period="5d")
    print(f"Fetched {len(df)} days of data.")
    print(df.head())
