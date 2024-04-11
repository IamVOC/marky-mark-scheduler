from app.services.enqueuer_by_timetable_service import EnqueuerByTimetableService
from app.models.base import Base
from app.db import engine


Base.metadata.create_all(engine)
EnqueuerByTimetableService().send_tasks_according_to_timetable()
