import json
from kafka import KafkaConsumer
from app.config.settings import settings

consumer = KafkaConsumer(
    "student_created",
    bootstrap_servers=settings.KAFKA_BROKER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

def consume_students():
    for message in consumer:
        print("Consumed:", message.value)