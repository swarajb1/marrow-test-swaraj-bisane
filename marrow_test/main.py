import os

import uvicorn
from api.image import router
from fastapi import FastAPI

app: FastAPI = FastAPI()

app.include_router(router)

API_KEY = os.environ["OPENAI_API_KEY"]


def main():
    print(API_KEY)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8002,
    )


if __name__ == "__main__":
    main()

__all__ = ["app"]
