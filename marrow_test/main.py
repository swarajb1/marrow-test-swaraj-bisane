import uvicorn
from api.image import router
from fastapi import FastAPI

app: FastAPI = FastAPI()

app.include_router(router)


def main():
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8002,
    )


if __name__ == "__main__":
    main()

__all__ = ["app"]
