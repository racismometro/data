from core.tweet_streamer import TweetStreamer
from mock import patch
import tweepy


# @patch()
def test_should_return_exact_data_from_stream():
    raw_data = {
        'text': 'this is a mock tweet',
        'in_reply_to_status_id': '1223'
    }
    tweet_streamer = TweetStreamer()

    assert tweet_streamer.on_data(raw_data) == raw_data