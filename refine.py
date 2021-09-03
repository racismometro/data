import os
import urllib
import pymongo

from data.data_lake import DataLake

def refine(data_lake: DataLake):
    for doc in data_lake.find_all():
        print(doc)