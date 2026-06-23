from prometheus_client import Counter

KAFKA_EVENTS = Counter(
    "kafka_events_total",
    "Total Kafka events processed"
)

def inc_event():
    KAFKA_EVENTS.inc()