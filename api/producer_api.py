from fastapi import APIRouter

from services.producer_service import ProducerService

router = APIRouter(prefix="/kafka", tags=["soldiers"])
producer_service = ProducerService()


@router.get(
    "/",
    response_description="Producing news massages and publishing to Kafka",
)
def publish():
    producer_service.publish()
