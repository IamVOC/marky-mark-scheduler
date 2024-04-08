import pytest

from app.db import Session
from app.repositories.students_subgroup_repository import StudentsSubgroupRepository


@pytest.mark.parametrize('test_input,expect',
                         [(1, [1]),                                                                               
                          (2, [1, 2])])
def test_get_students_by_subgroups(test_input, expect):
    repo = StudentsSubgroupRepository(Session())

    res = repo.get_students_chatid_by_subgroup(test_input)

    assert res == expect
