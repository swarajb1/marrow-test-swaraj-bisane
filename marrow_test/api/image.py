import os

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from schemas.image import GetImageRequest

API_KEY = os.environ["OPENAI_API_KEY"]

router: APIRouter = APIRouter()


QUESTION: str = "Extract text from the image in structured format."


@router.post("/work")
async def work_(request: Request, data: GetImageRequest):
    # file = data.image_file.file

    return JSONResponse(
        content={
            "status": "ok",
            "message": "work",
            # "image_url": image_url,
        },
        status_code=200,
    )
