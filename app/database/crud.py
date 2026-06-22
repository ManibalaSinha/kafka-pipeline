from sqlalchemy.orm import Session

from app.models.job import JobEvent
from app.models.job_table import JobTable


class JobRepository:

    def create_job(self, db: Session, job: JobEvent):
        db_job = JobTable(
            job_id=job.job_id,
            user_id=job.user_id,
            event_type=job.event_type,
            status=job.status,
            payload=job.payload,
            timestamp=job.timestamp,
        )

        db.add(db_job)
        db.commit()
        db.refresh(db_job)

        return db_job

    def get_job_by_id(self, db: Session, job_id: str):
        return (
            db.query(JobTable)
            .filter(JobTable.job_id == job_id)
            .first()
        )

    def update_status(self, db: Session, job_id: str, status: str):
        job = self.get_job_by_id(db, job_id)

        if not job:
            return None

        job.status = status

        db.commit()
        db.refresh(job)

        return job

    def delete_job(self, db: Session, job_id: str):
        job = self.get_job_by_id(db, job_id)

        if not job:
            return None

        db.delete(job)
        db.commit()

        return job