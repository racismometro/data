import tweepy

from data.data_lake import DataLake

class TweetExtractor():

    def __init__(self, api: tweepy.API, data_lake: DataLake):
        self.__api = api
        self.__data_lake = data_lake

    def extract():
        search_query = '(racismo AND sofri) OR (discriminação AND sofri)'
        # words_list = ['racismo', 'sofri', 'discriminação'] in case we use stream to fetch tweets

        # there is a search_full_archive as well but it needs an environment to be set
        new_tweets = api.search( q=search_query,
                                 result_type = 'recent',
                                 lang = 'pt' )

        documents = []

        for tweet in new_tweets:
            tweet_json = tweet._json

            if tweet.truncated == True:
                extended_tweet = api.get_status(tweet.id, tweet_mode='extended')
                tweet_json['text'] = extended_tweet.full_text

            documents.append(tweet_json)

        data_lake.bulk_insert(documents)

    def parse_tweets_to_json_documents(tweets) -> list[dict]:
        pass
