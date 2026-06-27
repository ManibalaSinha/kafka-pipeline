from prometheus_client import Counter

KAFKA_EVENTS = Counter(
    "kafka_events_total",
    "Total Kafka events processed"
)

def inc_event():
    KAFKA_EVENTS.inc()

KAFKA_MESSAGES_PRODUCED = Counter(
    "kafka_messages_produced_total",
    "Total Kafka messages produced"
)

KAFKA_MESSAGES_CONSUMED = Counter(
    "kafka_messages_consumed_total",
    "Total Kafka messages consumed"
)
from app.metrics.kafka import KAFKA_MESSAGES_PRODUCED

KAFKA_MESSAGES_PRODUCED.inc()
from app.metrics.kafka import KAFKA_MESSAGES_CONSUMED

KAFKA_MESSAGES_CONSUMED.inc()