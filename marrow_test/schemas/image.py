from typing import Annotated

from fastapi import File, UploadFile
from pydantic import BaseModel, field_validator


class GetImageRequest(BaseModel):
    image_file: Annotated[UploadFile, File()] | None = None

    image_url: str | None = None

    @field_validator("image_file", mode="before")
    def check_image_file(cls, v):
        if not v.filename.endswith((".jpg", ".jpeg", ".png")):
            raise ValueError("Invalid image file type")
        return v

    @field_validator("image_url", mode="before")
    def check_image_url(cls, v):
        if not v.startswith(("http://", "https://")):
            raise ValueError("Invalid image URL")
        return v
