from prometheus_client import Counter, Histogram, generate_latest

# Request counter
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total API Requests",
    ["method", "endpoint"]
)

# Kafka metrics
KAFKA_MESSAGES_PRODUCED = Counter(
    "kafka_messages_produced_total",
    "Total Kafka messages produced"
)

KAFKA_MESSAGES_CONSUMED = Counter(
    "kafka_messages_consumed_total",
    "Total Kafka messages consumed"
)

# API latency
REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "API request latency"
)


def metrics_endpoint():
    return generate_latest()