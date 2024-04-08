from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from app.abstractions.students_subgroup_repository_interface import IStudentsSubgroupRepository
from app.models.students_subgroup import StudentsSubgroup
from app.models.student import Student


class StudentsSubgroupRepository(IStudentsSubgroupRepository):

    def __init__(self, session: Session):
        self._session = session

    def get_students_chatid_by_subgroup(self, subgroup_id: int) -> List[int]:
        stmt = select(Student.chat_id).where(
                StudentsSubgroup.student_guid == Student.student_guid).where(
                StudentsSubgroup.subgroup_id == subgroup_id) 
        res = [r for r, in self._session.execute(stmt)]
        self._session.close()
        return res
