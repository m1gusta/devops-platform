from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))

    description: Mapped[str] = mapped_column(String(500))
    