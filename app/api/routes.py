from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.job_schema import (
    JobCreate,
    JobResponse,
    JobUpdate,
)
#from app.services.job_service import JobService

router = APIRouter(prefix="/api/v1/jobs", tags=["Jobs"],)

@router.post(
    "/",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,)

def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new job.
    """

    return JobService(db).create_job(job)

@router.get(
    "/",
    response_model=List[JobResponse],
)
def get_jobs(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """
    Get all jobs.
    """

    return JobService(db).get_jobs(skip, limit)


@router.get(
    "/{job_id}",
    response_model=JobResponse,
)
def get_job(
    job_id: str,
    db: Session = Depends(get_db),
):
    """
    Get a single job.
    """

    job = JobService(db).get_job(job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    return job


@router.put(
    "/{job_id}",
    response_model=JobResponse,
)
def update_job(
    job_id: str,
    job: JobUpdate,
    db: Session = Depends(get_db),
):
    """
    Update an existing job.
    """

    updated_job = JobService(db).update_job(job_id, job)

    if not updated_job:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    return updated_job


@router.delete(
    "/{job_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_job(
    job_id: str,
    db: Session = Depends(get_db),
):
    """
    Delete a job.
    """

    deleted = JobService(db).delete_job(job_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    return None


@router.post(
    "/ingest",
    status_code=status.HTTP_202_ACCEPTED,
)
def ingest_jobs(
    db: Session = Depends(get_db),
):
    """
    Trigger data ingestion from external APIs.
    """

    JobService(db).ingest_jobs()

    return {
        "message": "Data ingestion started successfully."
    }


@router.post(
    "/publish/{job_id}",
)
def publish_to_kafka(
    job_id: str,
    db: Session = Depends(get_db),
):
    """
    Publish a job event to Kafka.
    """

    JobService(db).publish_job(job_id)

    return {
        "message": "Job published to Kafka successfully."
    }


@router.post(
    "/cache/{job_id}",
)
def cache_job(
    job_id: str,
    db: Session = Depends(get_db),
):
    """
    Cache a job in Redis.
    """

    JobService(db).cache_job(job_id)

    return {
        "message": "Job cached successfully."
    }


@router.get("/health")
def health():
    """
    Health check endpoint.
    """

    return {
        "status": "UP",
        "service": "Enterprise Data Pipeline"
    }