import dataclasses
from top import *

@dataclasses.dataclass(kw_only=True)
class Message:
    """Toppobjekt med enkla och listvärda referenser till samtliga värdeobjekt. Bra grund för meddelanden!"""
    person: Person = None
    persons: list[Person] = None
