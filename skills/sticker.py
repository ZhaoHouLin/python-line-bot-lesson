from typing import Text
from linebot.models import TextSendMessage
from linebot.models.template import ImageCarouselTemplate, ImageCarouselColumn
from linebot.models.actions import PostbackAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('')
def get(message_request: MessageRequest):
    return [
        TextSendMessage(text=f'{message_request.message}')
    ]
