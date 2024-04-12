from unittest.mock import Mock, patch

from app.tasks.default.tasks import send_notification_task


service_mock = Mock()

@patch('app.tasks.default.tasks.MessageSenderService', new=service_mock)
def test_sender():
    subj = Mock()

    send_notification_task(1, subj)

    service_mock.assert_called_once()
