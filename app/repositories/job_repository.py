from app.models.job_table import Job

class JobRepository:
    def __init__(self, db):
        self.db = db

    def create(self, job_data):
        job = Job(**job_data)
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job