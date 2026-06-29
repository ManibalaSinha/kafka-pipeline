import json
from kafka import KafkaConsumer
from app.utils.logger import get_logger
from app.config.settings import settings


logger = get_logger(__name__)

consumer = KafkaConsumer(
    "student_created_dlq",
    bootstrap_servers=settings.KAFKA_BROKER,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="dlq-group",
)

logger.info("DLQ Consumer Started")

for message in consumer:
    logger.error(f" DEAD LETTER MESSAGE: {message.value}")

      
        
        #  Save to PostgreSQL failed_messages table
        #  Send email/Slack notification
        #  Push to S3 for investigation
        #  Create support ticket
     