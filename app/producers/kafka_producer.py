import json
from kafka import KafkaProducer
from app.config.settings import settings
from app.core.logger import logger


class KafkaMessageProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.kafka_bootstrap_server,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def send(self, topic: str, message: dict):
        try:
            self.producer.send(topic, message)
            self.producer.flush()
            logger.info(f"Message sent to topic={topic}: {message}")

        except Exception as e:
            logger.error(f"Kafka Producer Error: {str(e)}")
            raise