from unittest.mock import Mock, patch
from app.tasks.schedule.tasks import get_timetable_task


service_mock = Mock()

@patch('app.tasks.schedule.tasks.EnqueuerByTimetableService', new=service_mock)
def test_service_caller():

    get_timetable_task()

    service_mock.assert_called_once()

