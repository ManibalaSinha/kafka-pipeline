from app.database.db import Base

# Import all models 
from app.models.student import Student
from app.models.job_table import JobTable
from app.models.job import JobEvent
from sqlalchemy.orm import declarative_base

Base = declarative_base()