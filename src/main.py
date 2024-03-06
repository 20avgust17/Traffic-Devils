from fastapi import FastAPI

from src.handler_messages.api.v1.base import api_router as handler_messages_router


def include_router(app: FastAPI):
    app.include_router(handler_messages_router)


def start_application():
    app = FastAPI(title='Traffic Devils Test')
    include_router(app)
    return app


app = start_application()
