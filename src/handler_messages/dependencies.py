from src.handler_messages import schemas
from src.handler_messages.services import MessageHandlerService


def validate_data_before_send(message_data: schemas.MessageInfo) -> schemas.MessageInfo:
    MessageHandlerService().validate_bot_token(message_data.bottoken)
    MessageHandlerService().validate_chat_id(message_data.bottoken, message_data.chatid)
    return message_data
