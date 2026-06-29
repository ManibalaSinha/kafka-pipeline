import json
from kafka import KafkaConsumer
from app.utils.logger import get_logger
from app.database.db import SessionLocal
from app.models.student import Student
from app.config.settings import settings

class KafkaMessageConsumer:
    def __init__(self, topic: str):
        self.logger = get_logger(__name__)

        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=settings.KAFKA_BROKER,
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            group_id="student-group",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )

    def start(self):
        self.logger.info("Kafka Consumer Started...")

        for message in self.consumer:
            db = None
            try:
                data = message.value
                self.logger.info(f"Consumed message: {data}")

                db = SessionLocal()
                self.process_message(db, data)

                self.consumer.commit()  # commit only after DB success

            except Exception as e:
                self.logger.error(f"Consumer error: {str(e)}")

            finally:
                if db:
                    db.close()

    def process_message(self, db, data: dict):
        try:
            student = Student(
                name=data["name"],
                email=data["email"],
                age=data["age"],
            )

            db.add(student)
            db.commit()

            self.logger.info("Student saved from Kafka event")

        except Exception as e:
            db.rollback()
            self.logger.error(f"DB error in consumer: {str(e)}")
            raise


if __name__ == "__main__":
    consumer = KafkaMessageConsumer("student_created")
    consumer.start()