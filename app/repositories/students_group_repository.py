from sqlalchemy.orm import Session
from sqlalchemy import distinct, select
from typing import List

from app.abstractions.students_group_repository_interface import IStudentsGroupRepository
from app.models.students_subgroup import StudentsSubgroup
from app.models.student import Student
from app.models.subgroup import Subgroup


class StudentsGroupRepository(IStudentsGroupRepository):

    def __init__(self, session: Session):
        self._session = session

    def get_students_chatid_by_group(self, group_id: int) -> List[int]:
        stmt = (select(distinct(Student.chat_id))
                .join(StudentsSubgroup)
                .join(Subgroup)
                .where(Subgroup.group_id == group_id)
        )
        print(stmt)
        with self._session as session:
            return [r for r, in session.execute(stmt)]
