from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi import status

from src.handler_messages import schemas
from src.handler_messages.api.endpoind_docs.v1.route_game_items import SEND_MESSAGE_RESPONSES
from src.handler_messages.dependencies import validate_data_before_send
from src.handler_messages.services import MessageHandlerService

router = APIRouter()


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    responses=SEND_MESSAGE_RESPONSES
)
async def send_message(
        message_data: Annotated[schemas.MessageInfo, Depends(validate_data_before_send)],
):
    return MessageHandlerService().send_message(
        message_data=message_data
    )
