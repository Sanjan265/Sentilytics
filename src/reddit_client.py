import httpx
import logging

class RedditClient:
    def __init__(self):
        # We use a standard browser-like User Agent to access Reddit's public JSON endpoints 
        # without triggering their rate limits or requiring Developer API Apps.
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Sentilytics/1.0"
        }
        self.base_url = "https://www.reddit.com/search.json"

    def get_recent_mentions(self, ticker: str):
        # Search all of Reddit for recent mentions of this ticker
        params = {
            "q": ticker,
            "sort": "new",
            "t": "week",     # past week
            "limit": 100     # maximum posts per page
        }
        
        try:
            with httpx.Client() as client:
                response = client.get(self.base_url, headers=self.headers, params=params, timeout=10.0)
                
            if response.status_code == 200:
                data = response.json()
                posts = []
                for child in data.get("data", {}).get("children", []):
                    post_data = child.get("data", {})
                    
                    # Combine the post title and body text
                    title = post_data.get("title", "")
                    body = post_data.get("selftext", "")
                    
                    if title or body:
                        posts.append(f"{title} {body}")
                        
                return posts
            else:
                logging.error(f"Reddit returned status code {response.status_code}")
                return []
        except Exception as e:
            logging.error(f"Error fetching Reddit data: {e}")
            return []
