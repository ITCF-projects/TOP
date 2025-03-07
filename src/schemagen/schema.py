
import enum
import json
import re
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

    def try_add(self, name, obj):
        if not isinstance(obj, type):
            # We might want to add non-classes to the schema in the future, but for now it's
            # only classes.
            return

        if obj in self.typedefs_by_type:
            # We've already added it.
            return

        if isinstance(obj, type) and hasattr(obj, "__json_args__"):
            if issubclass(obj, enum.Enum):
                typedef = EnumTypedef(self, name, [x.name.strip("_") for x in obj])
            elif hasattr(obj, "__json_schema__"):
                typedef = ExplicitTypedef(self, name, obj.__json_schema__)
            else:
                typedef = Struct(self, name, obj)
            self.typedefs_by_name[name] = typedef
            self.typedefs_by_type[obj] = typedef
            if for_type := obj.__json_args__.get("python_type", None):
                self.typedefs_by_type[for_type] = typedef
            self.types_by_name[name] = obj

            for b in obj.__bases__:
                self.try_add(b.__name__.split(".")[-1], b)

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

    def make_single_schema_string(self, toplevel_name: str) -> str:
        schema = json.dumps(self.make_single_schema(toplevel_name), ensure_ascii=False, indent=2)
        lines = schema.splitlines()
        out = []
        while lines:
            if lines[0].strip() == "{" and "$ref" in lines[1]:
                out.append("        {" + lines[1].strip() + lines[2].strip())
                lines = lines[3:]
            else:
                out.append(lines.pop(0))
        return "\n".join(out)

