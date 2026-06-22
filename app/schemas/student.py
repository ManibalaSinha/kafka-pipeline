from datetime import datetime
from typing import Any

from pydantic import BaseModel

class StudentCreate(BaseModel):
    job_id: str
    user_id: str
    event_type: str
    status: str
    payload: dict[str, Any]
    timestamp: datetime

class StudentUpdate(BaseModel):
    status: str

class StudentResponse(StudentCreate):
    pass