from fastapi import APIRouter

from src.handler_messages.api.v1.route_message import router

api_router = APIRouter()

api_router.include_router(
    router=router,
    prefix='/messages',
    tags=['Handler messages for Telegram']
)

