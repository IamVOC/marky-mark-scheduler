from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from app.abstractions.group_repository_interface import IGroupRepository
from app.models.group import Group


class GroupRepository(IGroupRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_all_groups(self) -> List[int]:
        stmt = select(Group.group_id)
        with self._session as session:
            return [r for r, in session.execute(stmt)]
