from pydantic import BaseModel


class MessageInfo(BaseModel):
    bottoken: str
    chatid: int
    message: str
