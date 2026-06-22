from fastapi import APIRouter

from app.api.routes.student import router as student_router
from app.api.routes.job import router as job_router

router = APIRouter()

router.include_router(student_router, prefix="/students", tags=["Students"])
router.include_router(job_router, prefix="/jobs", tags=["Jobs"])