from prometheus_client import generate_latest

def metrics_endpoint():
    return generate_latest()