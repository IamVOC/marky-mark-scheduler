from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class Subgroup(Base):
    __tablename__ = 'subgroups'

    subgroup_id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int]
    group_name: Mapped[str]
