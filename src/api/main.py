from fastapi import FastAPI
from api.service.tweet_service import TweetService

app = FastAPI()
tweet_service = TweetService()

@app.get("/")
async def root():
    return {"body": "I am free!!!"}

@app.get("/total_incidence_between_dates")
async def get_total_incidence_between_dates():
    total_count = tweet_service.get_total_incidence_between_dates()

    return {
        "body" : total_count
    }