import base64

from pydantic import BaseModel, field_validator, model_validator


class GetImageRequest(BaseModel):
    image_file_base_encoded: str | None = None

    image_url: str | None = None

    @field_validator("image_file_base_encoded", mode="before")
    def check_image_file_base_encoded(cls, v):
        if not v:
            return None

        data = v.split(",")[1]

        if len(data) % 4 != 0:
            raise ValueError("Invalid base64 image data:")

        try:
            base64.b64decode(data, validate=True)

        except Exception:
            raise ValueError("Invalid base64 image data:")

        return v

    @field_validator("image_url", mode="before")
    def check_image_url(cls, v):
        if not v:
            return None

        if not v.startswith(("http://", "https://")):
            raise ValueError("Invalid image URL")
        return v

    @model_validator(mode="after")
    def check_image(self) -> "GetImageRequest":
        if not self.image_file_base_encoded and not self.image_url:
            raise ValueError("Either image_file_base_encoded or image_url must be provided")
        return self

    @model_validator(mode="after")
    def check_image_data(self) -> "GetImageRequest":
        if self.image_file_base_encoded and self.image_url:
            raise ValueError("Both image_file_base_encoded and image_url must be provided")
        return self
