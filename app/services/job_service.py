class JobService:

    def __init__(self, db):
        self.db = db
        self.repo = JobRepository()

    def create_job(self, job):
        ...

    def get_jobs(self, skip, limit):
        ...

    def get_job(self, job_id):
        ...

    def update_job(self, job_id, job):
        ...

    def delete_job(self, job_id):
        ...

    def publish_job(self, job_id):
        ...

    def cache_job(self, job_id):
        ...

    def ingest_jobs(self):
        ...