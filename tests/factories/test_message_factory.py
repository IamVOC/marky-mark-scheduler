import json

from app.factories.message_factory import MessageFactory
from app.constants import GREEN_BOOK, RED_BOOK, BLUE_BOOK, YELLOW_BOOK
from app.values.subject import Subject


def test_message_generate():
    value = Subject(subject_id=1,
                    subject_name='Dummy',
                    date='1900.01.01',
                    begin_lesson_time='11:11',
                    end_lesson_time='12:12',
                    lecturer_name='Jack',
                    auditorium='1-100')
    expect = {'chat_id': 2,
              'text': '*Dummy*\n\n1-100\n11:11-12:12\n\nJack',
              'parse_mode': 'markdown',
              'reply_markup': json.dumps({'inline_keyboard':
                                   [[{'text': f'{GREEN_BOOK}Присутствовал{GREEN_BOOK}',
                                      'callback_data': f'1900.01.01|11:11|G'},
                                     {'text': f'{RED_BOOK}Пропустил неув.{RED_BOOK}',
                                      'callback_data': f'1900.01.01|11:11|R'}],
                                    [{'text': f'{YELLOW_BOOK}Пропустил ув.{YELLOW_BOOK}',
                                      'callback_data': f'1900.01.01|11:11|Y'},
                                     {'text': f'{BLUE_BOOK}Дистанционно{BLUE_BOOK}',
                                      'callback_data': f'1900.01.01|11:11|B'}]]})
            }

    res = MessageFactory().generate_message(2, value)

    assert res == expect
