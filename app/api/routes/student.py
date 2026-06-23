from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas.student import StudentCreate
from app.services.student_service import StudentService
from app.core.response import success_response, error_response
router = APIRouter()

student_service = StudentService()
@router.post("/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    created = student_service.create_student(db, student)

    return success_response(
        data=created,
        message="Student created",
        status_code=201
    )
@router.get("/{id}")
def get_student(id: int, db: Session = Depends(get_db)):
    student = student_service.get_student(db, id)

    if not student:
        return error_response(
            message="Student not found",
            status_code=404
        )

    return success_response(
        data=student,
        message="Student fetched successfully"
    )
@router.delete("/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    student_service.delete_student(db, id)

    return success_response(
        message="Student deleted successfully",
        status_code=200
    )