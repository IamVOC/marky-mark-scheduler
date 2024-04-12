from celery import Celery
from celery.schedules import crontab

from app.config import get_settings


settings = get_settings()
celery = Celery('main', broker=settings.REDIS_URL)

celery.autodiscover_tasks(['app.tasks.schedule'])

celery.conf.beat_schedule = {
        'get-timetable-every-day-for-groups': {
            'task': 'schedule.get_timetable',
            'schedule': 3,
        }
    }

celery.conf.timezone = settings.TIMEZONE


