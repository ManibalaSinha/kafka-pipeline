import time
from fastapi import Request
from app.monitoring.metrics import REQUEST_COUNT, REQUEST_LATENCY


async def metrics_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path
    ).inc()

    REQUEST_LATENCY.observe(process_time)

    return response