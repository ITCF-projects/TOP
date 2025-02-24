import enum

from top2.common import WithId
from top2.gen import jsontype
from typing import *


if TYPE_CHECKING:
    from top2.common import I18NText


@jsontype()
class Name:
    given: str
    family: str


@jsontype()
class PersonState(enum.Enum):
    _new = 0
    ACTIVE = 1
    past = 2


class InlineState(enum.Enum):
    _foo = 0
    BAR_ = 1


@jsontype()
class Person(WithId):
    """A Person"""
    name: Annotated[Optional[Name], "The name, y'know?"]
    names: list[Name]
    description: "Optional[I18NText]"
    state: PersonState

    # Precomment
    state2: InlineState

