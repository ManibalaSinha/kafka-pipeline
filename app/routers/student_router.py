from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.student import StudentCreate
from app.services.student_service import StudentService

router = APIRouter()
service = StudentService()

@router.post("/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return service.create_student(db, student)