from core.tweet_streamer import TweetStreamer
from core.twitter_api import TwitterApi
from data.data_lake import DataLake

import tweepy

if __name__ == "__main__":
    twitter_api = TwitterApi.get_api()
    data_lake = DataLake()
    tweet_streamer = TweetStreamer(data_lake, twitter_api)

    stream_listener = tweepy.Stream(auth = twitter_api.auth, listener=tweet_streamer)

    print(stream_listener.filter(track=['put', 'your filters', 'here']))
