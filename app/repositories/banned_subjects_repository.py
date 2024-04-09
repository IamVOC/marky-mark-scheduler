from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List

from app.abstractions.banned_subjects_repository_interface import IBannedSubjectsRepository
from app.models.banned_subject import BannedSubject


class BannedSubjectsRepository(IBannedSubjectsRepository):

    def __init__(self, session: Session):
        self._session = session

    def get_all_subjects(self) -> List[int]:
        stmt = select(BannedSubject.subject_id)
        with self._session as session:
            return [r for r, in session.execute(stmt)]
