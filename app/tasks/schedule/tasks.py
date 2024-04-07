from app.main import app
from app.services.enqueuer_by_timetable_service import EnqueuerByTimetableService


@app.task(name="schedule.get_timetable")
def get_timetable_task():
    EnqueuerByTimetableService().send_tasks_according_to_timetable()
    

