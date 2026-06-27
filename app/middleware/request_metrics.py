import time
from fastapi import Request

from app.metrics.api import REQUEST_COUNT, REQUEST_LATENCY

async def metrics_middleware(request: Request, call_next):

    start = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start

    REQUEST_COUNT.labels(request.method, request.url.path).inc()

    REQUEST_LATENCY.observe(duration)

    return response