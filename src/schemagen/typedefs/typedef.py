
from typing import *

if TYPE_CHECKING:
    from schemagen.schema import Schema


class Typedef:
    def __init__(self, schema: "Schema", name: str):
        self.schema = schema
        self.name = name

    def schema_closed(self):
        pass

    def directly_referenced_typedefs(self) -> "set[Typedef]":
        return set()

    def recursively_referenced_typedefs(self) -> "set[Typedef]":
        referenced = set()
        to_check: "list[Typedef]" = [self]

        while to_check:
            td = to_check.pop()
            if td in referenced:
                continue

            referenced.add(td)
            for cand in td.directly_referenced_typedefs():
                if cand not in referenced:
                    to_check.append(cand)

        referenced.remove(self)
        return referenced

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        raise NotImplementedError()

    def json_schema_use(self) -> dict:
        return {"$ref": f"#/$defs/{self.name}"}


