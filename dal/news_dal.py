from core import Database


class NewsDAL:
    """Class to represent news's Data Layer, and implementing CRUD operations for news."""

    def __init__(self, db: Database, topic: str):
        """Constructor."""
        self.collection = db.get_topic_collection(topic)

    async def create(self, news: dict) -> dict:
        """Create a new news report record in the database."""
        result = await self.collection.insert_one(news)
        news["id"] = result.inserted_id
        return news

    async def list(self) -> list:
        """List all news in the database."""
        return await self.collection.find().to_list()
