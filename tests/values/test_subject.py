from pydantic import ValidationError
import pytest

from app.values.subject import Subject


def test_subject_validated():
    try:
        value = Subject(subject_id=1,
                    subject_name='Dummy',
                    date='1900.01.01',
                    begin_lesson_time='11:11',
                    end_lesson_time='12:12',
                    lecturer_name='Jack',
                    auditorium='1-100')
    except:
        pytest.fail()

def test_subject_failed_time_diff():
    with pytest.raises(ValueError, match='End of lesson must be after begin'):
        value = Subject(subject_id=1,
                        subject_name='Dummy',
                        date='1900.01.01',
                        begin_lesson_time='12:12',
                        end_lesson_time='11:11',
                        lecturer_name='Jack',
                        auditorium='1-100')

def test_subject_failed_begin():
    with pytest.raises(ValidationError):
        value = Subject(subject_id=1,
                        subject_name='Dummy',
                        date='1900.01.01',
                        begin_lesson_time=' 11:11',
                        end_lesson_time='12:12',
                        lecturer_name='Jack',
                        auditorium='1-100')

def test_subject_failed_end():
    with pytest.raises(ValidationError):
        value = Subject(subject_id=1,
                        subject_name='Dummy',
                        date='1900.01.01',
                        begin_lesson_time='11:11',
                        end_lesson_time=' 12:12',
                        lecturer_name='Jack',
                        auditorium='1-100')

def test_subject_failed_date():
    with pytest.raises(ValidationError):
        value = Subject(subject_id=1,
                        subject_name='Dummy',
                        date='190.01.01',
                        begin_lesson_time='11:11',
                        end_lesson_time='12:12',
                        lecturer_name='Jack',
                        auditorium='1-100')
    
