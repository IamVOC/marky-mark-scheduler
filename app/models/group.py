from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from .base import Base
from app.models.subgroup import Subgroup


class Group(Base):
    __tablename__ = 'groups'

    group_id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str]

    subgroups: Mapped[List["Subgroup"]] = relationship()

