from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session


class TopBase(DeclarativeBase):
    pass


class SprakhanteradText(TopBase):
    __tablename__ = "sprakhanterad_text"

    dbid: Mapped[int] = mapped_column(primary_key=True)
    lang: Mapped[str]
    content: Mapped[str]


class Identifierare(TopBase):
    __tablename__ = "identifierare"

    dbid: Mapped[int] = mapped_column(primary_key=True)
    namnrymd: Mapped[str]
    typnamn: Mapped[str]
    varde: Mapped[str]
    varderymd: Mapped[Optional[str]]


class Person(TopBase):
    __tablename__ = "person"

    dbid: Mapped[int] = mapped_column(primary_key=True)
    # postid_dbid: Mapped[int] = mapped_column(ForeignKey(Identifierare.dbid))
    # postid: Mapped[Identifierare] = relationship(foreign_keys=postid_dbid)
    korrelationsidn_dbid: Mapped[list[int]] = mapped_column(ForeignKey(Identifierare.dbid))
    korrelationsidn: Mapped[Optional[list[Identifierare]]] = relationship(foreign_keys=korrelationsidn_dbid)
    #sammanslagna_idn: Mapped[list[Identifierare]] = relationship(cascade="all, delete-orphan")
    #tidigare_korrelationsidn: Mapped[list[Identifierare]] = relationship(cascade="all, delete-orphan")


# class Tagg(TopBase):
#     __tablename__ = "tagg"
#
#     dbid: Mapped[int] = mapped_column(primary_key=True)
#     namnrymd: Mapped[str]
#     typnamn: Mapped[str]
#     varde: Mapped[str]
#     varderymd: Mapped[Optional[str]]
#
#     namn_dbid: Mapped[list[int]] = mapped_column(ForeignKey("sprakhanterad_text.dbid"))
#     namn: Mapped[list[SprakhanteradText]] = relationship()
#

from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True)
TopBase.metadata.create_all(engine)

with Session(engine) as db:
    me = Person(postid=Identifierare(namnrymd="chalmers.se", typnamn="cid", varde="viktor"))
    db.add_all([me])
    db.commit()