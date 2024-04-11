from app.db import Session_make
from app.repositories.groups_repository import GroupRepository


def test_getting_all_groups():
    with Session_make() as session:
        repo = GroupRepository(session)

        res = repo.get_all_groups()

    assert res == [1, 2, 3, 4]
