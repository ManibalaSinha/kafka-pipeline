from datetime import datetime
from typing import Any

from pydantic import BaseModel


class JobCreate(BaseModel):
    job_id: str
    user_id: str
    event_type: str
    status: str
    payload: dict[str, Any]
    timestamp: datetime


class JobUpdate(BaseModel):
    status: str


class JobResponse(JobCreate):
    pass