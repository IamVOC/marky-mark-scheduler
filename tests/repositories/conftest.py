import pytest
from sqlalchemy import insert

from app.db import engine, Session
from app.models.base import Base
from app.models.group import Group
from app.models.student import Student
from app.models.subgroup import Subgroup
from app.models.students_subgroup import StudentsSubgroup


@pytest.fixture(scope='module', autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = Session()
    group_query = insert(Group).values([{'group_id': 1, 'group_name': 'A-200'},
                                 {'group_id': 2, 'group_name': 'B-200'},
                                 {'group_id': 3, 'group_name': 'C-200'},
                                 {'group_id': 4, 'group_name': 'D-200'}
                                 ])
    subgroup_query = insert(Subgroup).values([{'subgroup_id': 1, 'group_id': 1, 'subgroup_name': 'A-200/1'},
                                              {'subgroup_id': 2, 'group_id': 1, 'subgroup_name': 'A-200/2'},
                                              {'subgroup_id': 3, 'group_id': 2, 'subgroup_name': 'B-200/1'}
                                              ])
    students_query = insert(Student).values([{'student_guid': '720cc030-f2cc-4f31-8472-ee3a418270ac',
                                              'student_name': 'Dummy1', 'chat_id': 1},
                                             {'student_guid': '37e671c6-67b5-4077-83ed-93e621cd21d2',
                                              'student_name': 'Dummy2', 'chat_id': 2}
                                             ])
    association_query = insert(StudentsSubgroup).values([{'student_guid': '720cc030-f2cc-4f31-8472-ee3a418270ac',
                                                          'subgroup_id': 1},
                                                         {'student_guid': '720cc030-f2cc-4f31-8472-ee3a418270ac',
                                                          'subgroup_id': 2},
                                                         {'student_guid': '37e671c6-67b5-4077-83ed-93e621cd21d2',
                                                          'subgroup_id': 2},
                                                         {'student_guid': '37e671c6-67b5-4077-83ed-93e621cd21d2',
                                                          'subgroup_id': 3}
                                                         ])
    session.execute(group_query)
    session.execute(subgroup_query)
    session.execute(students_query)
    session.execute(association_query)
    session.commit()
    session.close()
    yield
    Base.metadata.drop_all(bind=engine)



