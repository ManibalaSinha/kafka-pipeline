from datetime import datetime
from typing import Any

from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class StudentUpdate(BaseModel):
    status: str

class StudentResponse(StudentCreate):
    pass