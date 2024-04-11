from app.main import celery
from app.services.enqueuer_by_timetable_service import EnqueuerByTimetableService


@celery.task(name='schedule.get_timetable')
def get_timetable_task():
    EnqueuerByTimetableService().send_tasks_according_to_timetable()
    

