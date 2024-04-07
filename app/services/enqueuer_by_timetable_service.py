from datetime import date


from app.abstractions.enqueuer_by_table_service_interface import (
    IEnqueuerByTimetableService
)
from app.utils import get_timetable_url


class EnqueuerByTimetableService(IEnqueuerByTimetableService):

    def send_tasks_according_to_timetable(self) -> None:
        pass
