import json
from datetime import datetime

from core import Database
from dal.news_dal import NewsDAL
from models import Consumer


class ConsumerService:
    def __init__(self, db: Database, topic: str):
        self._consumer = Consumer(topic=topic)
        self._dal = NewsDAL(db, topic)

    async def create(self) -> list[dict]:
        """Create a new news report dump, passing the report to Dal."""
        events = self._consumer.get_consumed_messages()
        massages = []
        for event in events:
            event.update({'timestamp': datetime.now()})
            massages.append(event)

        results = []
        for massage in massages:
            created = await self._dal.create(massage)
            results.append(created)

        return results

    async def list_news(self) -> list[dict]:
        """List all news instances passed from Dal."""
        return await self._dal.list()
