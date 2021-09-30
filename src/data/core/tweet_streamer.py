import tweepy

from data.data_lake import DataLake


class TweetStreamer(tweepy.Stream):
    ...
    # def __init__(self, data_lake: DataLake, api=None):
    #     super().__init__(api)
    #     self.__data_lake = data_lake

    # def on_status(self, status):
    #     self.__data_lake.insert(status._json)