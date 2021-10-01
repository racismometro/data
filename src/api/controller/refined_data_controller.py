from fastapi import APIRouter
from api.service.tweet_service import TweetService

import configparser

tweet_service = TweetService()

config = configparser.RawConfigParser()
config.read('toggles.properties')

router = APIRouter()

@router.get("/total_incidence_between_dates/start-date={start_date}&end-date={end_date}")
async def get_total_incidence_between_dates(start_date, end_date):
    if config.getboolean("toggles", "incidence_counter"):
        total_count = tweet_service.get_total_incidence_between_dates(start_date, end_date)
        return {
            "body" : total_count
        }
    return {
            "body" : "feature is disabled"
    }