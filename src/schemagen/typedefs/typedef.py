
from typing import *

if TYPE_CHECKING:
    from schemagen.schema import Schema


class Typedef:
    def __init__(self, schema: "Schema", name: str):
        self.schema = schema
        self.name = name

    def schema_closed(self):
        pass

    def recursively_referenced_typedefs(self) -> "set[Typedef]":
        return set()

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        raise NotImplementedError()

    def json_schema_use(self) -> dict:
        return {"$ref": f"#/$defs/{self.name}"}


