from sqlalchemy import Column, String, DateTime, JSON

from app.database.db import Base


class JobTable(Base):
    __tablename__ = "jobs"

    job_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    event_type = Column(String)
    status = Column(String)
    payload = Column(JSON)
    timestamp = Column(DateTime)