# Module for defining Pydantic models for the application.
from pydantic import BaseModel, Field

class Course(BaseModel):
    """
    This is the data model for a course in the application.
    Attributes include the name of the course (ex. "Multivariable Calculus"), the code of the course (ex. "CSE 195"), 
    and the name of the professor teaching the course (ex. "Dr. Smith").

    Attributes:
    - name (str): The name of the course. Max length 100 characters to account for longer course names. 
    - code (str): The code of the course. Restricted to only 10 characters to ensure its short and sweet.
    - professor (str): The name of the professor teaching the course. Subject to change. 
    """

    name : str = Field(title="Course Name",
                       description="Name of the course",
                       max_length=100,
                       min_length=1,
                       example="Multivariable Calculus")
    
    code : str = Field(title="Course Code",
                       description="Code of the course",
                       max_length=10,
                       min_length=1, 
                       example="MATH 023")
    
    professor : str = Field(title="Professor Name",
                            description="Name of the professor",
                            max_length=50,
                            min_length=1, 
                            example="Santosh")

class Quiz(BaseModel):
    """
    This is the data model for any quizzes made by the application to be classified. It will be used to hold the quiz pdfs. 
    Attributes include the title of the quiz (ex. "Quiz 1"), and the quiz itself (ex. "quiz1.pdf").

    Attributes:
    - title (str): The title of the quiz. Max length 100 characters to account for longer quiz titles.
    - quiz (str): The quiz pdf. Restricted to only 200 characters to ensure its short and sweet.
    """
    # Ask about whether we want to hold the pdfs themselves in the database or just the links to them.
    # for now, im just going to hold the links to them.

    title : str = Field(title="Quiz titla",
                       description="title of the quiz",
                       max_length=100,
                       min_length=1, 
                       example=["Quiz 1", "Quiz 2"])
    
    quiz_link : str = Field(title="Quiz PDF",
                       description="Link to the quiz pdf",
                       max_length=200,
                       min_length=1,
                       example=["quiz1.pdf", "quiz2.pdf"])
    
    course_id: str = Field(title="Course Code",
                            description="Reference to the course") 

class CourseMaterial(BaseModel):
    """
    This is the data model for any course materials made by the application to be classified. It will be used to hold the course materials. 
    Attributes include the title of the course material (ex. "Lecture Notes"), and the course material itself (ex. "lecture_notes.pdf").

    Attributes:
    - title (str): The title of the course material. Max length 100 characters to account for longer course material titles.
    - course_material (str): The course material pdf. Restricted to only 200 characters to ensure its short and sweet.
    """

    title : str = Field(title="Course Material Title",
                       description="title of the course material",
                       max_length=100,
                       min_length=1, 
                       example=["Lecture Notes", "Lecture Slides"])
    
    course_material_link : str = Field(title="Course Material PDF",
                       description="Link to the course material pdf",
                       max_length=200,
                       min_length=1,
                       example=["lecture_notes.pdf", "lecture_slides.pdf"])
    
    course: str = Field(title="Course Code",
                        description="Reference to the course")

class UploadResponse(BaseModel):
    filename: str
    s3_key: str
    url: str