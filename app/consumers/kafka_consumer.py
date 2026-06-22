import json
from kafka import KafkaConsumer
from app.core.config import settings
from app.core.logger import logger
from app.db.session import SessionLocal
from app.models.student import Student


class KafkaMessageConsumer:
    def __init__(self, topic: str):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=settings.KAFKA_BROKER,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="student-group",
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

    def start(self):
        logger.info("Kafka Consumer Started...")

        for message in self.consumer:
            try:
                data = message.value
                logger.info(f"Consumed message: {data}")

                self.process_message(data)

            except Exception as e:
                logger.error(f"Consumer error: {str(e)}")

    def process_message(self, data: dict):
        db = SessionLocal()

        try:
            student = Student(
                name=data["name"],
                email=data["email"],
                age=data["age"]
            )

            db.add(student)
            db.commit()

            logger.info("Student saved from Kafka event")

        except Exception as e:
            db.rollback()
            logger.error(f"DB error in consumer: {str(e)}")

        finally:
            db.close()