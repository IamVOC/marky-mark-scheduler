from app.db import Session_make
from app.repositories.banned_subjects_repository import BannedSubjectsRepository


def test_getting_all_groups():
    with Session_make() as session:
        repo = BannedSubjectsRepository(session)

        res = repo.get_all_subjects()

    assert res == [1, 2]
