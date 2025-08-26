from typing import List

from pydantic import BaseModel

from models.news_model import NewsModel


class NewsCollection(BaseModel):
    news_reports: List[NewsModel]
