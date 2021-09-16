import os
import tweepy

class TwitterApi():

    @staticmethod
    def get_api() -> tweepy.API:
        API_KEY = os.getenv('API_KEY')
        API_SECRET = os.getenv('API_SECRET')
        ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
        ACCESS_SECRET = os.getenv('ACCESS_SECRET')

        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        
        return tweepy.API(auth)