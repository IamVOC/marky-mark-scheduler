from app.db import Session
from app.repositories.groups_repository import GroupRepository


def test_getting_all_groups():
    repo = GroupRepository(Session())

    res = repo.get_all_groups()

    assert res == [1, 2, 3, 4]
