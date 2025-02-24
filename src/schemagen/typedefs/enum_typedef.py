
from typing import *
from schemagen.typedefs.typedef import Typedef

if TYPE_CHECKING:
    from schemagen.schema import Schema


class EnumTypedef(Typedef):
    def __init__(self, schema: "Schema", name: str, values: list[str]):
        super().__init__(schema, name)
        self.values = values

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        if as_toplevel:
            raise RuntimeError()
        return {self.name: {"type": "string", "enum": self.values}}


