import json

from app.constants import GREEN_BOOK, RED_BOOK, BLUE_BOOK, YELLOW_BOOK
from app.values.subject import Subject


class MessageFactory:

    def generate_message(self, chat_id: int, subject: Subject):
        header = f'*{subject.subject_name}*'
        content = f'{subject.auditorium}\n{subject.begin_lesson_time}-{subject.end_lesson_time}'
        footer = f'{subject.lecturer_name}'
        text = f'{header}\n\n{content}\n\n{footer}'

        reply_markup = json.dumps({'inline_keyboard':
                                   [[{'text': f'{GREEN_BOOK}Присутствовал{GREEN_BOOK}',
                                      'callback_data': f'{subject.date}|{subject.begin_lesson_time}|G'},
                                     {'text': f'{RED_BOOK}Пропустил неув.{RED_BOOK}',
                                      'callback_data': f'{subject.date}|{subject.begin_lesson_time}|R'}],
                                    [{'text': f'{YELLOW_BOOK}Пропустил ув.{YELLOW_BOOK}',
                                      'callback_data': f'{subject.date}|{subject.begin_lesson_time}|Y'},
                                     {'text': f'{BLUE_BOOK}Дистанционно{BLUE_BOOK}',
                                      'callback_data': f'{subject.date}|{subject.begin_lesson_time}|B'}]]})
        return {'chat_id': chat_id,
                'text': text,
                'parse_mode': 'markdown',
                'reply_markup': reply_markup
                }

