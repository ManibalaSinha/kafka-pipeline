from prometheus_client import Counter, generate_latest

KAFKA_EVENTS = Counter("kafka_events_total", "Total Kafka events processed")
RETRY_EVENTS = Counter("retry_events_total", "Retry attempts")
DLQ_EVENTS = Counter("dlq_events_total", "Dead letter queue events")

def inc_kafka():
    KAFKA_EVENTS.inc()

def inc_retry():
    RETRY_EVENTS.inc()

def inc_dlq():
    DLQ_EVENTS.inc()

def metrics_output():
    return generate_latest()