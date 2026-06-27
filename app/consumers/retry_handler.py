from typing import Any, Callable
from app.config.settings import settings
from app.producers.dlq_producer import send_to_dlq
from app.utils.logger import logger

settings.max_retries

def handle_retry(producer, topic:str, message:dict, process_func:Callable[[dict], Any]):
    """
    Retry logic with Kafka retry topics
    student_retry_1 → student_retry_2 → student_retry_3 → DLQ
    """
    attempt = message.get("attempt", 0)

    try:
        process_func(message)
        return True

    except Exception as e:
        attempt += 1
        retry_message = message.copy()

        retry_message["attempt"] = attempt
        retry_message["exception"] = type(e).__name__
        retry_message["error"] = str(e)

        if attempt >= settings.max_retries:
            send_to_dlq(topic, retry_message)
            logger.error("Sent to DLQ:", retry_message)
            #logger.warning("Retry %d for topic %s", attempt, retry_topic)
        else:
            retry_topic = f"{topic}_retry_{attempt}"
            producer.send(retry_topic, retry_message)
            print(f"Sent to retry topic: {retry_topic}")

   