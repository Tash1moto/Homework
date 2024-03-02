from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    BOOLEAN,
    TIMESTAMP,
    ForeignKey,
    CheckConstraint,
    TEXT,
    create_engine
)
from sqlalchemy.orm import DeclarativeBase, declarative_base, relationship, sessionmaker


class Base(DeclarativeBase):
    ...


class Chat(Base):
    __tablename__ = "chats"
    __table_args__ = (
        CheckConstraint("length(name) >= 2"),
    )

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(length=32))


class Dep(Base):
    __tablename__ = "departments"
    __table_args__ = (
        CheckConstraint("length(name) >= 2"),
    )

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(length=32))


class Sdep(Base):
    __tablename__ = "sub_departments"
    __table_args__ = (
        CheckConstraint("length(name) >= 2"),
    )

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(length=32))


class Rchat(Base):
    __tablename__ = "chats_relations"
    __table_args__ = (
        CheckConstraint("length(name) >= 2"),
    )

    id = Column(INT, primary_key=True)
    chat_id = Column(
        INT,
        ForeignKey(column=Chat.id, ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False)
    departament_id = Column(
        INT,
        ForeignKey(column=Dep.id, ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=True
    )
    sub_departament_id = Column(
        INT,
        ForeignKey(column=Sdep.id, ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=True
    )

    chats = relationship(argument="Chat", back_populates="chats_relations")


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint("length(title) >= 2"),
        CheckConstraint("length(body) >= 2"),
    )

    id = Column(INT, primary_key=True)
    departament_id = Column(
        INT,
        ForeignKey(column=Dep.id, ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=True
    )
    sub_departament_id = Column(
        INT,
        ForeignKey(column=Sdep.id, ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=True
    )

    departments = relationship(argument=Dep, back_populates="users")
    sub_departments = relationship(argument=Sdep, back_populates="users")


engine = create_engine(url="postgresql://user1:8nycw4nyc9g4wy49@217.76.60.77:6666/user1")
session_maker = sessionmaker(bind=engine)
