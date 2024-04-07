
def get_timetable_url(group_id: int, date: str):
    return f'https://rasp.omgtu.ru/api/schedule/group/\
{group_id}?start={date}&finish={date}&lng=1'

