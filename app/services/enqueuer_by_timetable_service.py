from datetime import datetime
import requests
from typing import Dict
from sqlalchemy.orm import Session


from app.abstractions.enqueuer_by_table_service_interface import (
    IEnqueuerByTimetableService
)
from app.utils import (get_timetable_url,
                       get_today_date,
                       get_time_from_string,
                       get_remaining_seconds_until_time)
from app.db import Session_make
from app.repositories.groups_repository import GroupRepository
from app.repositories.banned_subjects_repository import BannedSubjectsRepository
from app.repositories.students_subgroup_repository import StudentsSubgroupRepository
from app.repositories.students_group_repository import StudentsGroupRepository
from app.tasks.default.tasks import send_notification


class EnqueuerByTimetableService(IEnqueuerByTimetableService):

    def send_tasks_according_to_timetable(self) -> None:
        with Session_make() as session:
            current_date = get_today_date()
            group_ids = GroupRepository(session).get_all_groups()
            banned_subjects = BannedSubjectsRepository(session).get_all_subjects()
            for group_id in group_ids:
                timetable = requests.get(get_timetable_url(group_id, current_date)).json()
                for subject in timetable:
                    # Checking that subject not banned
                    if subject['disciplineOid'] in banned_subjects:
                        continue
                    # Calculating countdown for message task
                    lesson_begin_time = get_time_from_string(subject['beginLesson'])
                    delta_to_lesson_begin = get_remaining_seconds_until_time(lesson_begin_time)

                    chat_ids = self._get_chat_ids_by_subjects_subgroup(session, subject, group_id)
                    for chat_id in chat_ids:
                        send_notification.apply_async(args=[chat_id], countdown=delta_to_lesson_begin)

    def _get_chat_ids_by_subjects_subgroup(self, session: Session, subject: dict, group_id: int):
        if subject['subGroupOid']:
            chat_ids = (StudentsSubgroupRepository(session)
                        .get_students_chatid_by_subgroup(subject['subGroupOid']))
        else:
            chat_ids = (StudentsGroupRepository(session)
                        .get_students_chatid_by_group(group_id))
        return chat_ids

                    





