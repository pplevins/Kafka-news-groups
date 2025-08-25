import json

from kafka import KafkaConsumer


class Consumer:
    def __init__(self, topic, bootstrap_servers=None):
        if bootstrap_servers is None:
            bootstrap_servers = ['localhost:9092']
        self.consumer = KafkaConsumer(topic,
                                      value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                      bootstrap_servers=bootstrap_servers,
                                      consumer_timeout_ms=10000)

    def save_messages_in_db(self):
        for message in self.consumer:
            print(message)
