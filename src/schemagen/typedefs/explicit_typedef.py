
from typing import *
from schemagen.typedefs.typedef import Typedef

if TYPE_CHECKING:
    from schemagen.schema import Schema


class ExplicitTypedef(Typedef):
    def __init__(self, schema: "Schema", name: str, explicit_definition: dict):
        super().__init__(schema, name)
        self.explicit_definition = explicit_definition

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        if as_toplevel:
            raise RuntimeError()
        return {self.name: self.explicit_definition}


