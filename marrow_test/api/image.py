from typing import Annotated

import open_ai.base_encoded_image_processing as openai_base_encoded_image_processing
import open_ai.url_image_processing as openai_url_image_processing
from fastapi import APIRouter, File, Request, UploadFile
from fastapi.responses import JSONResponse
from schemas.image import GetImageRequest
from utils import save_text_to_pdf

router: APIRouter = APIRouter()

QUESTION: str = "Extract text from the image in structured format."


@router.post("/image/transcribe-image")
async def transcribe_image(
    request: Request,
    data: GetImageRequest,
    image_file: Annotated[UploadFile, File()] | None = None,
):
    response: dict = {}

    if data.image_url:
        response = openai_url_image_processing.generate_response_with_image_url(
            question=QUESTION,
            image_url=data.image_url,
        )

    elif data.image_file_base_encoded:
        response = openai_base_encoded_image_processing.generate_response_with_image_base_encoded(
            question=QUESTION,
            image_file_base_encoded=data.image_file_base_encoded,
        )

    if "error" in response:
        return JSONResponse(
            content={
                "status": "error",
                "message": response["error"],
            },
            status_code=response["code"] if "code" in response else 500,
        )

    # if "response" in response:
    file_data: dict = save_text_to_pdf(text=response["response"])

    if file_data["code"] == 500:
        return JSONResponse(
            content={
                "status": "error",
                "message": file_data["error"],
            },
            status_code=500,
        )

    # if file_data["code"] == 200:

    return JSONResponse(
        content={
            "status": "ok",
            "text": response,
            "file_name": file_data["message"],
        },
        status_code=200,
    )
