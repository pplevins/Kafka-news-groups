import uvicorn
from fastapi import FastAPI

from api import router as producer_router

app = FastAPI(
    title="Kafka Producer API",
    summary="A FastAPI backend service that produce data and publish it to Kafka pypline.",
)

app.include_router(producer_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
