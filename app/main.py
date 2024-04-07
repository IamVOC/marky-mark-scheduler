from celery import Celery
from celery.schedules import crontab

from app.config import get_settings


settings = get_settings()
app = Celery('main', broker=settings.REDIS_URL)

app.autodiscover_tasks(['app.tasks.schedule'])

app.conf.beat_schedule = {
        'get-timetable-every-day-for-groups': {
            'task': 'schedule.get_timetable',
            'schedule': 3,
        }
    }

app.conf.timezone = settings.TIMEZONE


