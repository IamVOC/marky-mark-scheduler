from app.main import celery
from app.values.subject import Subject
from app.services.message_sender_service import MessageSenderService


@celery.task(name='default.send_notification')
def send_notification_task(chat_id: int, subject: Subject):
    MessageSenderService().send_message(chat_id, subject)
    
