
from typing import *

from schemagen.hints.hint import Hint


class ReferenceHint(Hint):
    def __init__(self, doc: str, optional: bool, is_list: bool, referenced_typedef: "Typedef"):
        super().__init__(doc, optional, is_list)
        self.referenced_typedef = referenced_typedef

    def json_schema_use(self) -> dict:
        return self.referenced_typedef.json_schema_use()


