from app.main import celery


@celery.task(name='default.send_notification')
def send_notification(chat_id: int, subject_properties: dict):
    pass
    
