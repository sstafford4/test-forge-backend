from beanie import Document, Link
from app.models import Course as CourseModel
from app.models import Quiz as QuizModel
from app.models import CourseMaterial as MaterialModel


# All 3 of these are just prototypes. They will be changed later.
# For now, they are just here to show how to use the models.

class Course(Document, CourseModel): 
    class Settings:
        collection = "courses"
        indexes = ["code"] # creating a index on the code of the course. This will improve the speed of querying based on the course number. 
        # without indexes, mongodb will have to scan the entire collection to find the course.

class Quiz(Document, QuizModel):
    course: Link[Course] # creating a relationship between the quiz and the course
    
    class Settings:
        collection = "quizzes"
        indexes = ["course"] # index based on the course attribute.

class CourseMaterial(Document, MaterialModel):
    course: Link[Course] # course material also gets a link to Course. 

    class Settings:
        collection = "course_materials"
        indexes = ["course"] # index based on the course attribute.
