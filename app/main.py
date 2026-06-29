from fastapi import FastAPI, Response
from app.middleware.request_metrics import metrics_middleware
from app.database.db import Base, engine
from app.metrics.endpoint import metrics_endpoint
from app.auth.router import router as auth_router
from app.routers.student_router import router as student_router
from app.routers.metrics_router import router as metrics_router

app = FastAPI(title="Enterprise Data Pipeline", version="1.0.0")

app.include_router(auth_router)

app.middleware("http")(metrics_middleware)

# include real routers
app.include_router(student_router, prefix="/api/v1/students", tags=["Students"])
app.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "KAFKA Data Pipeline Running"}