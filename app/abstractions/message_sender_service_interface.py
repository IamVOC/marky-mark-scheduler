from abc import ABC, abstractmethod

from app.values.subject import Subject


class IMessageSenderService(ABC):

    @abstractmethod
    def send_message(self, chat_id: int, subject: Subject):
        pass
