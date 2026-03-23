# 📈 Sentilytics - Market Sentiment Analyzer

Sentilytics is a full-stack, real-time web application that predicts short-term stock movements by correlating live market data with social media sentiment from Reddit. 

## ✨ Features
- **Real-Time Data Ingestion:** Safely scrapes live, public text posts from Reddit dynamically across investing subreddits.
- **Machine Learning Sentiment Analysis:** Uses NLTK's **VADER Lexicon** to process unstructured social media text (slang, emojis, etc.) and generate accurate polarity scores.
- **Financial Data Integration:** Automatically pulls a 7-day historical price time-series window using Python's `yfinance` library.
- **Dynamic Visualization:** Uses vanilla JavaScript and **Chart.js** to map historical financial data concurrently with predicted sentiment metrics to an interactive graphical chart.
- **RESTful Architecture:** Built on a lightning-fast **FastAPI** backend that natively serves the unified frontend application.

## 🛠️ Technology Stack
- **Backend:** Python, FastAPI, Uvicorn
- **Data Engineering:** HTTPx, yfinance
- **Machine Learning (NLP):** NLTK (Natural Language Toolkit)
- **Frontend:** HTML, Vanilla CSS, JavaScript, Chart.js

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9+ installed on your machine.

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sanjan265/Sentilytics.git
   cd Sentilytics
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the backend server:**
   ```bash
   python -m uvicorn src.main:app --port 8000 --reload
   ```

5. **View the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000`

## 🧠 Why Build This?
This was engineered to overcome standard third-party rate limits and walled-garden APIs (specifically the closed Reddit Developer API) by implementing direct, secure public-endpoint web scraping pipelines. It stands as an end-to-end example of bypassing data silos to construct robust machine-learning-driven analytics dashboards.
