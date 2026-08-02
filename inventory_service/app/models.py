from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Inventory(Base):

    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    product_name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    stock: Mapped[int] = mapped_column(
        Integer
    )

class ProcessedEvent(Base):

    __tablename__ = "processed_events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    event_id = Column(
        Integer,
        unique=True,
        nullable=False
    )