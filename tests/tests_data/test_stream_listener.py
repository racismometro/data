from data.core.tweet_streamer import TweetStreamer
from mock import patch

import json

@patch('data.data_lake.DataLake')
def test_should_return_exact_data_from_stream(data_lake_mock):
    raw_data = {
        'text': 'this is a mock tweet',
        'in_reply_to_status_id': 1223
    }
    raw_data_json = json.dumps(raw_data)
    
    tweet_streamer = TweetStreamer(data_lake_mock)

    tweet_streamer.on_data(raw_data_json)

    data_lake_mock.insert.assert_called_with(raw_data)