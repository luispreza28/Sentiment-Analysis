from utilities import analyze_twitter_comments, plot_sentiments, get_tweet_v2, mock_get_tweet_v2, calculate_overall_sentiment
import os
import tweepy
from unittest.mock import patch
from transformers import pipeline


# os.environ['TWITTER_BEARER_TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAP12vQEAAAAA2lxRNQejqdJJMm8gvyCRVKureBY%3D8TmPHHrKC8LB7SiRoW5FJuwNmCbGBHrZJqZCb3J9EHpYNw9kxk'
# TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')


def main():
    # """API keys"""
    # api_key = 'api_key'
    # api_key_secret = 'api_secret_key'
    #
    # """Access token"""
    # access_token = 'access_token'
    # access_token_secret = 'access_secret_token'
    #
    # """Authenticate with twitter"""
    # auth = tweepy.OAuthHandler(api_key, api_key_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth)

    """CODE BELOW IS MENAT FOR TEST TWEETS"""
    # Create a test tweet
    # test_tweet = api.update_status('This is a test tweet for sentiment analysis')

    # Get tweet id
    tweet_id = '1234567890'

    # Simulate the response data for the test tweet
    tweet_data = mock_get_tweet_v2(tweet_id, None)

    # Access tweet content and username
    tweet_text = tweet_data['data']['text']
    username = tweet_data['includes']['users'][0]['username']

    # Simulate replies
    replies = [
        "I think this is great!",
        "Not a fan of this tweet.",
        "It's okay, could be better.",
    ]

    # Analyze the sentiment of the replies
    sentiment_analysis = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

    results = []
    for reply in replies:
        results.append(sentiment_analysis(reply))
        print(sentiment_analysis(reply))
    plot_sentiments(results)


if __name__ == '__main__':
    main()
