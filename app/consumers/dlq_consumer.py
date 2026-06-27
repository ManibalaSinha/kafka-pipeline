import json
from kafka import KafkaConsumer
from app.config.settings import settings
from app.utils.logger import logger

DLQ_TOPIC = "student_dlq"

def start_dlq_consumer() -> None:
    """
    Consume failed messages from the Dead Letter Queue (DLQ).
    """
    consumer = KafkaConsumer(
        DLQ_TOPIC,
        bootstrap_servers=settings.kafka_bootstrap_server,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="student-dlq-group",
    )

    logger.info("DLQ Consumer started...")

    for record in consumer:
        message = record.value

        logger.error("DLQ Message: %s", message)

      
        
        #  Save to PostgreSQL failed_messages table
        #  Send email/Slack notification
        #  Push to S3 for investigation
        #  Create support ticket
     