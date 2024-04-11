import app.utils
import datetime
from unittest.mock import Mock, patch


date_mock = Mock()
date_mock.today.return_value = datetime.date(1900, 1, 1)
datetime_mock = Mock()
datetime_mock.now.return_value = datetime.datetime(1900, 1, 1, 12, 10, 30, 0)

def test_get_timetable_url():
    group_id = 100
    time = '1900.01.01'

    res = app.utils.get_timetable_url(group_id, time)

    assert res == 'https://rasp.omgtu.ru/api/schedule/group/100?start=1900.01.01&finish=1900.01.01&lng=1'


@patch('app.utils.date', new=date_mock)
def test_get_today_date():

    res = app.utils.get_today_date()

    assert res == '1900.01.01'

@patch('app.utils.datetime', new=datetime_mock)
def test_get_current_time():
    res = app.utils.get_current_time()

    assert res == datetime.time(12, 10, 30, 0)

def test_get_time_from_string():
    time_str = '12:10'

    res = app.utils.get_time_from_string(time_str)

    assert res == datetime.time(12, 10, 0, 0)

@patch('app.utils.datetime', new=datetime_mock)
def test_get_remaining_seconds_until_time():
    needed_time = datetime.time(13, 20, 40, 0)

    res = app.utils.get_remaining_seconds_until_time(needed_time)

    assert res == 4210
