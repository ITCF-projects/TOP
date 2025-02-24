
from schemagen.hints.hint import Hint


class BooleanHint(Hint):
    def __init__(self, doc: str, optional: bool, is_list: bool):
        super().__init__(doc, optional, is_list)

    def json_schema_use(self) -> dict:
        base_schema = {"type": "boolean"}
        return base_schema


