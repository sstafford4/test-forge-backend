# File for creating exception handling functions. 

import logging

from beanie import PydanticObjectId
from fastapi import status

logger = logging.getLogger("uvicorn.error")


class APIException(Exception):
    def __init__(self, code: int, detail: str):
        # HTTP status code that indicates the type of error.
        self.code = code
        # A descriptive error message.
        self.detail = detail
        logger.warning(self.detail)

    def __str__(self) -> str:
        # Return the error message when the exception is printed.
        return self.detail


class InternalServerError(APIException):
    def __init__(self, detail: str):
        # Initialize with HTTP 500 status code and a generic internal server error message.
        super().__init__(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        )
