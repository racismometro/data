import os
import urllib

from data.mongodb_connector import MongoDBConnector
from pymongo.cursor import Cursor
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))


class DataLake():

    def __init__(self):
        user = urllib.parse.quote(os.getenv('MONGO_USER'))
        password = urllib.parse.quote(os.getenv('MONGO_PASSWORD'))

        data_lake_input_client = MongoDBConnector.connect(
                "mongodb+srv://{}:{}@datalake.mzdtn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(user, password)
        )
        data_lake_output_client = MongoDBConnector.connect(
                "mongodb://{}:{}@datalake-mzdtn.a.query.mongodb.net/myFirstDatabase?ssl=true&authSource=admin".format(user, password)
        )

        self.__data_lake_input_collection = data_lake_input_client.data_lake.test_tweets
        self.__data_lake_output_collection = data_lake_output_client.get_database('db').get_collection('collection')

    def pour(self, documents: list[dict]):
        self.__data_lake_input_collection.insert_many(documents)

    def find(self, filter: dict = None) -> Cursor:
        return self.__data_lake_output_collection.find(filter)

    def find_all(self) -> Cursor:
        return self.__data_lake_output_collection.find()