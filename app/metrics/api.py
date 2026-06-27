from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total API Requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "API request latency"
)