import app.actions as Actions
import app.documents as Documents
import app.schemas as Schemas
from app.models import UploadResponse

from fastapi import APIRouter, HTTPException, UploadFile, File  
from botocore.exceptions import ClientError, BotoCoreError
import uuid

from app.s3_config import s3, BUCKET_NAME, REGION_NAME

router = APIRouter()

@router.post("/courses", response_model=Schemas.createCourseResponse, status_code=201)
async def create_course(course: Schemas.createCourseRequest) -> Documents.Course:
    try:
        return await Actions.create_course(**course.model_dump())
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)) -> UploadResponse:
    try:
        # Optional: generate a unique filename
        file_key = f"{uuid.uuid4()}_{file.filename}"

        # Upload file to S3
        s3.upload_fileobj(file.file, BUCKET_NAME, file_key)

        # You can return the file URL if needed
        file_url = f"https://{BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/{file_key}"
        return UploadResponse(filename=file.filename, s3_key=file_key, url=file_url)

    except (BotoCoreError, ClientError) as e:
        raise HTTPException(status_code=500, detail=str(e))