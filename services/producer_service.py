from core import DataFetcher
from models import Producer


class ProducerService:
    def __init__(self):
        self._producer = Producer()
        self._fetcher = DataFetcher()

    def publish(self):
        for topic in self._fetcher.data.keys():
            categories = self._fetcher.categories[topic].copy()
            massages = []
            len_massages = len(self._fetcher.data[topic])
            for i in range(len_massages):
                if self._fetcher.data[topic][i]['category'] in categories:
                    massage = self._fetcher.data[topic].pop(i)
                    categories.remove(massage['category'])
                    massages.append(massage)
                if not categories:
                    break
            self._producer.publish_massage(topic=topic, msg=massages)
