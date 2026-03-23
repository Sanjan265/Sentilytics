import praw
import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "sentiment_predictor:v1.0")
    )

def fetch_subreddit_posts(subreddit_name="wallstreetbets", limit=100, time_filter="day"):
    """
    Fetches top posts from a subreddit.
    """
    try:
        reddit = get_reddit_instance()
        subreddit = reddit.subreddit(subreddit_name)
        posts = []
        
        for submission in subreddit.top(time_filter=time_filter, limit=limit):
            # Only consider text posts or posts with significant titles
            posts.append({
                "id": submission.id,
                "title": submission.title,
                "text": submission.selftext,
                "score": submission.score,
                "num_comments": submission.num_comments,
                "created_utc": datetime.utcfromtimestamp(submission.created_utc).isoformat(),
                "url": submission.url
            })
            
        return pd.DataFrame(posts)
    except Exception as e:
        print(f"Error fetching from Reddit: {e}")
        return pd.DataFrame()
        
if __name__ == "__main__":
    df = fetch_subreddit_posts(limit=10)
    print(f"Fetched {len(df)} posts.")
    print(df.head())
