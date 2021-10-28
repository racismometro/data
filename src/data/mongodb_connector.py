import pymongo


class MongoDBConnector:

    @staticmethod
    def connect(host_uri: str) -> pymongo.MongoClient:
        return pymongo.MongoClient(host_uri)
