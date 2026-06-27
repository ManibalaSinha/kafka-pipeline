from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.services.job_service import JobService

router = APIRouter()

@router.get("/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    return JobService(db).get_job(job_id)

@router.post("/ingest")
def ingest_jobs(db: Session = Depends(get_db)):
    return JobService(db).ingest_jobs()