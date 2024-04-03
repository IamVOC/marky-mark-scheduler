from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class Group(Base):
    __tablename__ = 'groups'

    group_id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str]
