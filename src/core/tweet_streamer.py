import tweepy


class TweetStreamer(tweepy.StreamListener):
    def on_status(self, status):
        return status
