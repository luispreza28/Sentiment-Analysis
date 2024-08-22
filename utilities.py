import requests
import matplotlib.pyplot as plt
from textblob import TextBlob
import tweepy


"""Download additional data for nltk"""
# nltk.download('all')

"""API keys"""
api_key = 'vOCgIHyyWilrnYtuXdTmoH00n'
api_key_secret = 'c2SE4cV9FoFQaL9XAE77xFGKE5RvDbFO1Rxl6frspEWsJ19xIX'

"""Access token"""
access_token = '1765955334622121985-M30xCjDT0Jj6mLN5NNk9DyyzrNvlez'
access_token_secret = 'JOK7hwaQzkurRV3MgcggqH0r1wOlKIwZoYFbXxFxNbVkf'

"""Authenticate with twitter"""
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)



def mock_get_tweet_v2(tweet_id, bearer_token):
    # Simulated response data
    return {
        'data': {
            'text': "This is a test tweet for sentiment analysis.",
            'id': tweet_id
        },
        'includes': {
            'users': [
                {
                    'username': 'test_user'
                }
            ]
        }
    }


def get_tweet_v2(tweet_id, bearer_token):
    url = f"https://api.twitter.com/2/tweets"
    params = {
        'ids': tweet_id,
        'tweet.fields': 'created_at',
        'expansions': 'author_id',
        'user.fields': 'created_at'
    }
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}, {response.text}")

    return response.json()

# Create headers
def create_headers(bearer_token):
    headers = {'Authorization': f"Bearer {bearer_token}"}
    return headers


# Get tweets
def get_tweets(bearer_token, query, max_results=10):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    headers = create_headers(bearer_token)
    params = {
        'query': query,
        'tweet.fields': 'created_at,text,author_id',
        'expansions': 'author_id',
        'user.fields': 'username',
        'max_results': max_results,
    }
    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code}, {response.text}")

    tweet_data = response.json()

    return tweet_data


# Analyze tweet
def analyze_tweet(tweets_data):
    tweets = [tweet['text'] for tweet in tweets_data['data']]
    results = [sentiment_analysis(tweet) for tweet in tweets]
    return results


# Fetch comments
def fetch_comments(api, tweet_id, username):
    replies = []
    for tweet in tweepy.Cursor(api.search_tweets, q=f'to:{username}', since_id=tweet_id, tweet_mode='extended').items():
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id_str == tweet_id:
                replies.append(tweet.full_text)
    return replies


# Get Sentiment Analysis
def sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    print(f"Text: {text}, sentiment score: {sentiment}")

    if sentiment > .2:
        return 'Positive'
    elif sentiment < -.2:
        return 'Negative'
    else:
        return 'Neutral'


# Analyze twitter comments
def analyze_twitter_comments(api, tweet_id, username):
    comments = fetch_comments(api, tweet_id, username)
    sentiments = {'Positive': 0, 'Negative': 0, 'Neutral': 0}

    for comment in comments:
        sentiment = sentiment_analysis(comment)
        sentiments[sentiment] += 1

    return sentiments


# Plot sentiment analysis

def plot_sentiments(results):
    sentiments = {'Positive': 0, 'Negative': 0, 'Neutral': 0}

    for result in results:
        label = result[0]['label']
        if label == 'positive':  # Check if the label is positive
            sentiments['Positive'] += 1
        elif label == 'negative':  # Check if the label is negative
            sentiments['Negative'] += 1
        elif label == 'neutral':  # Check if the label is neutral
            sentiments['Neutral'] += 1

    # Calculate the overall sentiment
    total_score = sentiments['Positive'] - sentiments['Negative']
    if total_score > 0:
        overall_sentiment = "Positive"
    elif total_score < 0:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"

    labels = sentiments.keys()
    values = sentiments.values()

    plt.bar(labels, values)
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Comments')
    plt.title('Sentiment Analysis of Twitter Comments')

    # Add overall sentiment as a text annotation
    plt.text(0.5, 1.09, f"Overall Sentiment: {overall_sentiment}",
             horizontalalignment='center', verticalalignment='center',
             fontsize=12, color='blue', weight='bold', transform=plt.gca().transAxes)
    plt.show()


def calculate_overall_sentiment(results):
    total_score = 0

    for result in results:
        label = result[0]['label']
        if label == 'positive':
            total_score += 1
        elif label == 'negative':
            total_score -= 1

    if total_score > 0:
        return 'Overall Sentiment: Positive'
    elif total_score < 0:
        return 'Overall Sentiment: Negative'
    else:
        return 'Overall Sentiment: Neutral'
