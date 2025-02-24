
import enum
import types
import datetime

from typing import *
from schemagen.typedefs import *
import schemagen.default_jsontypes


class Schema:
    def __init__(self):
        self.typedefs_by_name: dict[str, Typedef] = {}
        self.typedefs_by_type: dict[type, Typedef] = {}
        self.types_by_name: dict[str, type] = {}
        self.load_module(schemagen.default_jsontypes)
        self.typedefs_by_type[datetime.datetime] = self.typedefs_by_name["DateTime"]

    def try_add(self, name, obj):
        if isinstance(obj, type) and hasattr(obj, "__json_args__"):
            if issubclass(obj, enum.Enum):
                typedef = EnumTypedef(self, name, [x.name.strip("_") for x in obj])
            elif hasattr(obj, "__json_schema__"):
                typedef = ExplicitTypedef(self, name, obj.__json_schema__)
            else:
                typedef = Struct(self, name, obj)
            self.typedefs_by_name[name] = typedef
            self.typedefs_by_type[obj] = typedef
            self.types_by_name[name] = obj

    def load_modules(self, *modules: types.ModuleType):
        for m in modules:
            self.load_module(m)

    def load_module(self, m: types.ModuleType):
        for name in dir(m):
            obj = getattr(m, name)
            self.try_add(name, obj)

    def close_schema(self):
        for t in self.typedefs_by_name.values():
            t.schema_closed()

    def make_single_schema(self, toplevel_name: str) -> dict:
        return self.typedefs_by_name[toplevel_name].json_schema_definition(as_toplevel=True)
