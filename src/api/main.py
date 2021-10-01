from fastapi import Request, FastAPI
from api.service.tweet_service import TweetService

import configparser

app = FastAPI()

tweet_service = TweetService()

config = configparser.RawConfigParser()
config.read('toggles.properties')
incidence_counter_toggle = config.getboolean("toggles", "incidence_counter")

@app.get("/")
async def root():
    return {"body": "I am free!!!"}

@app.get("/total_incidence_between_dates/start-date={start_date}&end-date={end_date}")
async def get_total_incidence_between_dates(start_date, end_date):
    if config.getboolean("toggles", "incidence_counter"):
        total_count = tweet_service.get_total_incidence_between_dates()
        return {
            "body" : total_count
        }
    return {
            "body" : "feature is disabled"
    }