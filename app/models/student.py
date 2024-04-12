from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID
from typing import Optional

from .base import Base


class Student(Base):
    __tablename__ = 'students'

    student_guid: Mapped[str] = mapped_column(UUID, primary_key=True)
    student_name: Mapped[str]
    chat_id: Mapped[Optional[int]]
