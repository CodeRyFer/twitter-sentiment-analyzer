import tweepy
from textblob import TextBlob
from dotenv import load_dotenv
import os

# Twitter API v2 credentials
load_dotenv()
bearer_token = os.environ.get('BEARER_TOKEN')

# Create a Tweepy client for API v2
client = tweepy.Client(bearer_token=bearer_token)

query = 'Trump'
response = client.search_recent_tweets(query=query, max_results=10)
public_tweets = response.data if response.data else []

for i, tweet in enumerate(public_tweets, 1):
    print(f"Tweet #{i}:")
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(f"Sentiment: polarity={analysis.polarity:.2f}, subjectivity={analysis.subjectivity:.2f}")
    print("-" * 40)
