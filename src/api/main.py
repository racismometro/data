from fastapi import FastAPI
from src.api.controller import refined_data_controller

app = FastAPI()
app.include_router(refined_data_controller.router, prefix="/refined_data")


@app.get("/")
async def root():
    return {"body": "I am free!!!"}
