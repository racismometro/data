import os
import tweepy

from dotenv import load_dotenv
from data.data_lake import DataLake

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

def extract(data_lake: DataLake):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    search_query = '(racismo AND sofri) OR (discriminação AND sofri)'
    # words_list = ['racismo', 'sofri', 'discriminação'] in case we use stream to fetch tweets

    # there is a search_full_archive as well but it needs an environment to be set
    new_tweets = api.search( q=search_query,
                             until='2021-09-01',
                             result_type = 'recent',
                             lang = 'pt' )
    
    documents = []

    for tweet in new_tweets:
        tweet_json = tweet._json

        if tweet.truncated == True:
            extended_tweet = api.get_status(tweet.id, tweet_mode='extended')
            tweet_json['text'] = extended_tweet.full_text

        documents.append(tweet_json)
        
    data_lake.pour(documents)