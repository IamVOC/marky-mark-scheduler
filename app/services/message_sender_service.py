import requests

from app.abstractions.message_sender_service_interface import IMessageSenderService
from app.factories.message_factory import MessageFactory
from app.values.subject import Subject
from app.config import get_settings


class MessageSenderService(IMessageSenderService):

    def send_message(self, chat_id: int, subject: Subject):
        content = MessageFactory().generate_message(chat_id, subject)
        requests.post(url=f'{get_settings().TELEGRAM_URL}/sendMessage', 
                      data=content)
