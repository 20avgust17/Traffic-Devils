import requests

from starlette import status
from starlette.responses import JSONResponse

from src import utils
from src.handler_messages import schemas


class MessageHandlerService:
    @staticmethod
    def send_message(message_data: schemas.MessageInfo) -> JSONResponse:
        url = f"https://api.telegram.org/bot{message_data.bottoken}/sendMessage"
        response = requests.post(
            url=url,
            json={"chat_id": message_data.chatid, "text": message_data.message}
        )
        utils.raise_exception_if_true(
            item=not (response.status_code == 200),
            on_error_message="Internal server error please contact technical support",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        return JSONResponse(
            {
                'Status': 'OK',
                'Detail': f'Your message has been delivered to chat with id: {message_data.chatid}. '
                          f'Using a bot with a token: {message_data.bottoken}'
            }
        )

    @staticmethod
    def validate_bot_token(bot_token: str) -> None:
        url = f"https://api.telegram.org/bot{bot_token}/getMe"
        response = requests.get(url)
        utils.raise_exception_if_true(
            item=not (response.status_code == 200),
            on_error_message="Invalid bot token: '%s'" % bot_token,
            status_code=status.HTTP_400_BAD_REQUEST
        )

    @staticmethod
    def validate_chat_id(bot_token: str, chat_id: int) -> None:
        url = f"https://api.telegram.org/bot{bot_token}/getChat"
        payload = {"chat_id": chat_id}
        response = requests.post(url, json=payload)
        utils.raise_exception_if_true(
            item=not (response.status_code == 200),
            on_error_message="Invalid chat id: '%s'" % chat_id,
            status_code=status.HTTP_400_BAD_REQUEST
        )
