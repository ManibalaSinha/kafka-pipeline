import time
from app.core.dlq import send_to_dlq

MAX_RETRIES = 3

def retry_with_topic(producer, topic, message, process_func):
    """
    Retry logic with Kafka retry topics
    student_retry_1 → student_retry_2 → student_retry_3 → DLQ
    """

    attempt = message.get("attempt", 0)

    try:
        return process_func(message)

    except Exception as e:
        attempt += 1
        message["attempt"] = attempt
        message["error"] = str(e)

        if attempt >= MAX_RETRIES:
            send_to_dlq(topic, message)
            print("Sent to DLQ:", message)
        else:
            retry_topic = f"{topic}_retry_{attempt}"
            producer.send(retry_topic, message)
            print(f"Sent to retry topic: {retry_topic}")

        time.sleep(1)