from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class BannedSubject(Base):
    __tablename__ = 'banned_subjects'

    subject_id: Mapped[int] = mapped_column(primary_key=True)
