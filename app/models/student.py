from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID
from typing import Optional

from base import Base


class Student(Base):
    __tablename__ = 'students'

    student_guid: Mapped[UUID] = mapped_column(primary_key=True)
    chat_id: Mapped[Optional[int]]
