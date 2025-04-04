"""
Module for defining database document models.

This module uses Beanie's Document base class combined with Pydantic models
to define the schema of documents stored in the MongoDB collection.
"""
from beanie import Document, Link
from app.models import Course as CourseModel
from app.models import Quiz as QuizModel
from app.models import CourseMaterial as MaterialModel


# All 3 of these are just prototypes. They will be changed later.
# For now, they are just here to show how to use the models.


class Course(Document, CourseModel): 
    class Settings:
        collection = "courses"

class Quiz(Document, QuizModel): 
    class Settings:
        collection = "quizzes"

class CourseMaterial(Document, MaterialModel):
    course: Link[Course]

    class Settings:
        collection = "course_materials"
        indexes = ["course"]

