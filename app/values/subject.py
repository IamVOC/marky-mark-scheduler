from pydantic import BaseModel, Field, model_validator


class Subject(BaseModel):
    subject_id: int
    subject_name: str
    date: str = Field(pattern=r"^[0-9]{4}.[0-9]{2}.[0-9]{2}")
    begin_lesson_time: str = Field(pattern=r"^[0-9]{2}:[0-9]{2}")
    end_lesson_time: str = Field(pattern=r"^[0-9]{2}:[0-9]{2}")
    lecturer_name: str
    auditorium: str

    @model_validator(mode='before')
    def end_must_be_after_begin(self) -> 'Subject':
        b1, b2 = map(int, self['begin_lesson_time'].split(':'))
        e1, e2 = map(int, self['end_lesson_time'].split(':'))
        if (b1 == e1 and b2 > e2) or b1 > e1:
            raise ValueError('End of lesson must be after begin')
        return self

