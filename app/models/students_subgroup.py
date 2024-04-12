from sqlalchemy import UUID, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class StudentsSubgroup(Base):
    __tablename__ = 'students_subgroups'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student_guid: Mapped[str] = mapped_column(UUID, ForeignKey("students.student_guid"))
    subgroup_id: Mapped[int] = mapped_column(Integer, ForeignKey("subgroups.subgroup_id"))
