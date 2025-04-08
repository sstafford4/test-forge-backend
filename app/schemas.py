from pydantic import BaseModel
from app.models import Course, Quiz, CourseMaterial

class createCourseRequest(Course, BaseModel):
    pass

class createCourseResponse(Course, BaseModel):
    pass