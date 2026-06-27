import json

from kafka import KafkaProducer
from app.config.settings import settings
from app.utils.logger import logger


class KafkaMessageProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.kafka_bootstrap_server,
            api_version=(3, 5, 0),
            request_timeout_ms=30000,
            retries=5,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def send(self, topic: str, message: dict):
        try:
            future = self.producer.send(topic, message)
            future.get(timeout=10)
            logger.info(f"Message sent to topic={topic}: {message}")
        except Exception as e:
            logger.exception(f"Kafka Producer Error: {e}")
            raise