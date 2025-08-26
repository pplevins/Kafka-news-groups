import uvicorn
from fastapi import FastAPI

from api import interesting_router

app = FastAPI(
    title="Kafka Consumer API - interesting topic",
    summary="A FastAPI backend service that consume data from Kafka pypline and save it to MongoDB database."
)

app.include_router(interesting_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
