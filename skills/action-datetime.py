from typing import Text
from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import DatetimePickerAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{action_datetime}')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='Menu',
            text='Please select',
            actions=[
                DatetimePickerAction(
                    label='請選擇日期', data='datetime_postback', 
                    mode='datetime',
                    initial='2022-12-01t00:00',
                    max='2022-12-31t23:59',
                    min='2022-01-01t00:00'
                )
            ]
        )
    )

    return [
        msg
    ]
