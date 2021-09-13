from os import truncate
import tweepy

from mock import patch

from core.tweet_extractor import TweetExtractor
from core.twitter_api import TwitterApi
from data.data_lake import DataLake
from tweepy.models import SearchResults
from tweepy.models import Status

twitter_api = TwitterApi.get_api()
data_lake = DataLake()
tweet_extractor = TweetExtractor(twitter_api, data_lake)

def test_should_return_something_on_twitter_api_search():
    result = tweet_extractor.extract()
    assert result != None
    assert type(result) == list

#O que eu quero mockar -> função search() da classe API do módulo tweepy
@patch("tweepy.API.search")
@patch("tweepy.API.get_status")
@patch("tweepy.models.Status")
def test_should_untrucated_truncated_tweets(status_mock, get_status_mock, search_mock): # search_mock é o nome arbitrário que dei a função mockada
    # mocks de retorno
    tweets = [
        {
            "id" : 1,
            "tweet" : "tweet example 1 incompl...",
            "truncated" : True
        },
        {
            "id" : 1,
            "tweet" : "tweet example 2 complete!",
            "truncated" : False
        }
    ]

    json = {
        "search_metadata": {
            "refresh_url" : "dummy",
            "completed_in" : "dummy",
            "query" : "dummy",
            "count" : "dummy",
            "next_results" : "dummy"
        },
        "statuses" : tweets
    }

    status_mock.full_text = "tweet example 1 incomplete is now complete"
    search_mock.return_value = SearchResults.parse(twitter_api, json)
    get_status_mock.return_value = status_mock

    result = tweet_extractor.extract()
    print(result)
    
    assert result[0]["truncated"] is False
    assert result[0]["tweet"] == status_mock.full_text
    assert result[1]["truncated"] is False
    assert result[1]["tweet"] == tweets[1]["tweet"]