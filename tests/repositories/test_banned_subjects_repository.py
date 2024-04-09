from app.db import Session
from app.repositories.banned_subjects_repository import BannedSubjectsRepository


def test_getting_all_groups():
    repo = BannedSubjectsRepository(Session())

    res = repo.get_all_subjects()

    assert res == [1, 2]
