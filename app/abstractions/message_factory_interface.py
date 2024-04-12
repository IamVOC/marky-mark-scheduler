from abc import ABC, abstractmethod

from app.values.subject import Subject


class IMessageFactory(ABC):

    @abstractmethod
    def generate_message(self, chat_id: int, subject: Subject):
        pass
