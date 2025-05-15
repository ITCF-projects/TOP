
from schemagen.hints.hint import Hint


class IntegerHint(Hint):
    def __init__(self, doc: str, optional: bool, is_list: bool, value_range: tuple[int, int] = None):
        super().__init__(doc, optional, is_list)
        self.value_range = value_range

    def json_schema_use(self) -> dict:
        base_schema = {"type": "integer"}
        if self.value_range:
            base_schema["minimum"] = self.value_range[0]
            base_schema["maximum"] = self.value_range[1]
        return base_schema

    def to_markdown(self) -> str:
        return "`" + self.cardinalize("integer") + "`"

