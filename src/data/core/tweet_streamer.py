import os
import tweepy

from data.core.twitter_api import TwitterApi
from data.data_lake import DataLake


class TweetStreamer(tweepy.Stream):
    def __init__(self, data_lake: DataLake, api=None):
        twitter_api = TwitterApi()

        consumer_key, consumer_secret, access_token, access_secret = twitter_api.get_api_credentials().values()

        super().__init__(consumer_key, consumer_secret, access_token, access_secret)
        self.__data_lake = data_lake

    def on_status(self, status):
        self.__data_lake.insert(status._json)