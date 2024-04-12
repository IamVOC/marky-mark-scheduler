from abc import ABC, abstractmethod


class IEnqueuerByTimetableService(ABC):

    @abstractmethod
    def send_tasks_according_to_timetable(self) -> None:
        pass
