from app.documents import Course, Quiz, CourseMaterial
from app.models import Course as CourseModel
from app.models import Quiz as QuizModel
from app.models import CourseMaterial as MaterialModel

# Adding a course to the database. 
async def create_course(name: str, code: str, professor: str) -> Course:
    new_course: Course = await Course(
        name=name,
        code=code,
        professor=professor
    ).insert()

    return new_course

# Uploading course material to the database. 
