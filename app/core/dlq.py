import json
from kafka import KafkaProducer
from app.config.settings import settings

dlq_producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_to_dlq(topic: str, message: dict):
    dlq_producer.send(f"{topic}_DLQ", message)
    dlq_producer.flush()