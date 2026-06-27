from kafka import KafkaProducer
import json
from app.config.settings import settings
DLQ_TOPIC = "student_dlq"

producer = KafkaProducer(bootstrap_servers="kafka:9092", value_serializer=lambda v: json.dumps(v).encode())

def publish(topic, message):
    producer.send(topic, message)
    producer.flush()

def send_to_dlq(original_topic: str, message: dict) -> None:
    """
    Publish a failed message to the Dead Letter Queue.
    """
    message["original_topic"] = original_topic

    producer.send(DLQ_TOPIC, message)
    producer.flush()