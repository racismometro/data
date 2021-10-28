import os

from tweepy.api import API


class TwitterApi():

    def get_api_credentials(self):
        API_KEY = os.getenv('API_KEY')
        API_SECRET = os.getenv('API_SECRET')
        ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
        ACCESS_SECRET = os.getenv('ACCESS_SECRET')

        return {
            'consumer_key': API_KEY,
            'consumer_secret': API_SECRET,
            'access_token': ACCESS_TOKEN,
            'acess_secret': ACCESS_SECRET
        }
