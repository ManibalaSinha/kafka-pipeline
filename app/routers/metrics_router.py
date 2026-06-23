from fastapi import APIRouter, Response
from app.metrics.prometheus_metrics import metrics_output

router = APIRouter()

@router.get("/metrics")
def metrics():
    return Response(metrics_output(), media_type="text/plain")