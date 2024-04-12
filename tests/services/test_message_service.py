from unittest.mock import Mock, patch

from app.services.message_sender_service import MessageSenderService


factory_mock = Mock()
generate_message_mock = Mock()
generate_message_mock.generate_message.return_value = {'dummy': 'content'}
factory_mock.return_value = generate_message_mock
requests_mock = Mock()
post_mock = Mock()
requests_mock.post = post_mock
subj_mock = Mock()

@patch('app.services.message_sender_service.MessageFactory', new=factory_mock)
@patch('app.services.message_sender_service.requests', new=requests_mock)
def test_message_service():
    service = MessageSenderService()

    service.send_message(1, subj_mock)

    post_mock.assert_called_with(url='https://api.telegram.org/bot0000000000:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/sendMessage',
                                 data={'dummy': 'content'})


