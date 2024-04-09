import pytest

from app.db import Session
from app.repositories.students_group_repository import StudentsGroupRepository


@pytest.mark.parametrize('test_input,expect',
                         [(1, [1, 2]),                                                                               
                          (2, [2])])
def test_get_students_by_groups(test_input, expect):
    repo = StudentsGroupRepository(Session())

    res = repo.get_students_chatid_by_group(test_input)

    assert res == expect
