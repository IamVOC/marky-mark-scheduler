from datetime import datetime, time, date
import pytz
from app.config import get_settings


def get_timetable_url(group_id: int, date: str) -> str:
    return f'https://rasp.omgtu.ru/api/schedule/group/\
{group_id}?start={date}&finish={date}&lng=1'

def get_today_date() -> str:
    return date.today().strftime('%Y.%m.%d')

def get_current_time() -> time:
    return datetime.now(pytz.timezone(get_settings().TIMEZONE)).time()

def get_time_from_string(string_time: str) -> time:
    return datetime.strptime(string_time, '%H:%M').time()

def get_remaining_seconds_until_time(final_time: time) -> int:
    current_time = get_current_time()
    return ((final_time.hour * 3600 + final_time.minute * 60 + final_time.second) -
            (current_time.hour * 3600 + current_time.minute * 60 + current_time.second))
