from fastapi import APIRouter, FastAPI, Response
from app.core.middleware import metrics_middleware
from app.database.db import Base, engine
from app.monitoring.metrics import metrics_endpoint
from app.api.routes import router

app = FastAPI(title="Enterprise Data Pipeline", version="1.0.0")
router = APIRouter()
app.include_router(router, prefix="/api/v1")
app.middleware("http")(metrics_middleware)

@app.get("/metrics")
def metrics():
    return Response(metrics_endpoint(), media_type="text/plain")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Enterprise Data Pipeline Running"}