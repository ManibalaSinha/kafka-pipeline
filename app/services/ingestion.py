import json
import logging
from kafka import KafkaConsumer
from sqlalchemy.orm import Session

from app.models.job import JobEvent
from app.database.crud import JobRepository
from app.database.db import SessionLocal
from app.config.settings import settings

logger = logging.getLogger(__name__)

class JobIngestionService:

    def __init__(self):
        self.consumer = KafkaConsumer(
            "job-events",
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVER,
            group_id="job-consumers",
            enable_auto_commit=False,
            value_deserializer=lambda v: json.loads(v.decode("utf-8"))
        )

        self.repo = JobRepository()

    def process_event(self, event_data: dict, db: Session):
        """
        Core business logic
        """

        # 1. Convert to domain model
        job_event = JobEvent.from_dict(event_data)

        # 2. Validation
        if not job_event.job_id or not job_event.user_id:
            raise ValueError("Invalid event payload")

        # 3. Business logic
        if job_event.event_type == "created":
            self.repo.create_job(db, job_event)

        elif job_event.event_type == "updated":
            self.repo.update_status(db, job_event.job_id, job_event.status)

        elif job_event.event_type == "deleted":
            self.repo.delete_job(db, job_event.job_id)

        else:
            raise ValueError(f"Unknown event type: {job_event.event_type}")

    def start(self):
        """
        Main consumer loop
        """
        logger.info("Starting Kafka consumer...")

        for message in self.consumer:
            db = SessionLocal()

            try:
                event_data = message.value

                self.process_event(event_data, db)

                # commit only after success
                self.consumer.commit()

                logger.info(f"Processed event: {event_data['job_id']}")

            except Exception as e:
                db.rollback()
                logger.error(f"Failed processing event: {e}")

                # DO NOT commit → message will be retried
                # optionally send to DLQ here

            finally:
                db.close()