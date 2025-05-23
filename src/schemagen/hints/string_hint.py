
from schemagen.hints.hint import Hint


class StringHint(Hint):
    def __init__(self, doc: str, optional: bool, is_list: bool, regexp: str = None, enum: list[str] = None):
        super().__init__(doc, optional, is_list)
        self.regexp = regexp
        self.enum = enum

    def json_schema_use(self) -> dict:
        base_schema = {"type": "string"}
        if self.regexp:
            base_schema["pattern"] = self.regexp
        if self.enum:
            base_schema["enum"] = self.enum
        return base_schema

    def to_markdown(self) -> str:
        md = "`" + self.cardinalize("boolean") + "`"
        if self.enum:
            return md + ' Value one of "' + '", "'.join(self.enum) + '")'
        elif self.regexp:
            return md + f' Must match regexp: `{self.regexp}`'
        return md


