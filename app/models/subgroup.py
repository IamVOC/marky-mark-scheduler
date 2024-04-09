from typing import List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.student import Student

from .base import Base


class Subgroup(Base):
    __tablename__ = 'subgroups'

    subgroup_id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[Optional[int]] = mapped_column(ForeignKey("groups.group_id"))
    subgroup_name: Mapped[str]

    students: Mapped[List["Student"]] = relationship(secondary="students_subgroups")

