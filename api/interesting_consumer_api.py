from fastapi import APIRouter

from core import Database
from services.consumer_service import ConsumerService

router = APIRouter(prefix="/kafka")
db = Database()
consumer_service = ConsumerService(db=db, topic="interesting")


@router.get(
    "/",
    response_description="Consuming news massages from Kafka, and saving to database."
)
async def consume():
    return await consumer_service.create()


@router.get(
    "/news",
    response_description="Get all news saved in database."
)
async def list_news():
    return await consumer_service.list_news()
