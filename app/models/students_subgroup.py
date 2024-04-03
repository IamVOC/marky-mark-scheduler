from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID

from base import Base


class StudentsSubgroup(Base):
    __tablename__ = 'students_subgroups'

    student_guid: Mapped[UUID]
    subgroup_id: Mapped[int]
