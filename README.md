# Twitter Sentiment Analysis

This project performs sentiment analysis on Twitter data, focusing on user comments (replies) to a given tweet. It uses TextBlob for polarity-based sentiment analysis and HuggingFace's transformers for sentiment classification based on a pre-trained language model.

## Features
- Fetches and analyzes sentiments of Twitter comments.
- Provides both rule-based sentiment analysis (via TextBlob) and model-based sentiment classification (via HuggingFace's cardiffnlp/twitter-roberta-base-sentiment-latest).
- Displays the overall sentiment result as a bar chart.
- Handles the authentication process to access Twitter data.

## Installation
### Prerequisites
- Python 3.x
- Twitter API credentials (Bearer Token, API keys)
- Install the required libraries using the following command:

```pip install -r requirements.txt```

## Libraries used:
- requests: For sending HTTP requests to Twitter API.
- matplotlib: For plotting sentiment results.
- TextBlob: For basic sentiment analysis.
- tweepy: For interacting with the Twitter API.
- transformers: For advanced sentiment classification.
- nltk: For natural language processing tasks.

## Requirements File:

- pandas==2.1.0
- scikit-learn==1.3.0
- datasets==2.8.0
- nltk==3.8.1

## Usage
### 1. Set Up Twitter API Credentials

Before running the project, you need to set up your Twitter API credentials in main.py and utilities.py (if not using mock data for testing purposes).

### 2. Run the Project

After configuring the credentials, run the main script using:

```python main.py```

#### This will:

- Fetch a tweet and its comments.
- Analyze the sentiment of the comments.
- Display a bar chart representing the sentiment distribution.

## File Overview
#### main.py
This is the entry point of the project. It includes:

- Simulating a Twitter tweet and comments for testing.
- Utilizing HuggingFace's sentiment-analysis model to classify comments as positive, neutral, or negative.
- Plotting the overall sentiment using matplotlib.

#### utilities.py
This file contains helper functions:

- get_tweet_v2: Fetches a tweet using the Twitter API.
- mock_get_tweet_v2: Simulates a tweet for testing.
- get_tweets: Fetches tweets based on a search query.
- analyze_tweet: Analyzes the sentiment of a tweet.
- fetch_comments: Fetches replies to a tweet.
- analyze_twitter_comments: Analyzes the sentiment of Twitter comments.
- plot_sentiments: Plots the sentiment results using a bar chart.

#### requirements.txt
Contains the required libraries for the project.

#### API Key Setup
In order to fetch real-time tweets and replies, you need to configure your Twitter API keys:

1. Go to Twitter Developer Portal.
2. Create a new application and generate the API keys and tokens.
3. Replace the placeholder values in the utilities.py with your actual API credentials:

api_key = 'your_api_key'

api_key_secret = 'your_api_secret'

access_token = 'your_access_token'

access_token_secret = 'your_access_token_secret'

### Alternatively, set these as environment variables in your system or use the os module to access them securely.

#### Example Output
Upon running the project, you'll see the sentiment analysis results displayed as a bar chart:

- Positive: Number of positive comments.
- Negative: Number of negative comments.
- Neutral: Number of neutral comments.

Additionally, the overall sentiment (positive, negative, or neutral) is displayed above the chart.

Example Bar Chart:

|  Positive  |  Negative  |  Neutral  |

|     5      |     2      |     3     |
#### Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.
