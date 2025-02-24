
import enum
import types
import typing
import inspect


def jsontype(only_local=False):
    def wrap(cls):
        cls.__json_args__ = {"only_local": only_local}
        return cls
    return wrap


"""
En Hint är en typ på ett attribut. En Struct definierar ett objekt. Varje klass i källkoden
har både en Struct (som definierar namn och utseende) och en Hint (som refererar till denna
struct by-name).
"""


class Constraint:
    pass


class Regexp(Constraint):
    def __init__(self, regexp: str):
        self.regexp = regexp


class Hint:
    def __init__(self, doc: str, optional: bool, is_list: bool):
        self.doc = doc
        self.optional = optional
        self.is_list = is_list

    def to_json_schema(self) -> dict:
        if self.is_list:
            sch = {"type": "array", "items": self.json_schema_use()}
        else:
            sch = self.json_schema_use()
        if self.doc:
            sch["description"] = " ".join(x.strip() for x in self.doc.split("\n"))
        return sch

    def json_schema_use(self) -> dict:
        raise NotImplementedError()


class ReferenceHint(Hint):
    def __init__(self, doc: str, optional: bool, is_list: bool, referenced_typedef: "NamedTypedef"):
        super().__init__(doc, optional, is_list)
        self.referenced_typedef = referenced_typedef

    def json_schema_use(self) -> dict:
        return self.referenced_typedef.json_schema_use()


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


class NamedTypedef:
    def __init__(self, schema: "Schema", name: str):
        self.schema = schema
        self.name = name

    def schema_closed(self):
        pass

    def recursively_referenced_typedefs(self) -> "set[NamedTypedef]":
        return set()

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        raise NotImplementedError()

    def json_schema_use(self) -> dict:
        return {"$ref": f"#/$defs/{self.name}"}


class ExplicitTypedef(NamedTypedef):
    def __init__(self, schema: "Schema", name: str, explicit_definition: dict):
        super().__init__(schema, name)
        self.explicit_definition = explicit_definition

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        if as_toplevel:
            raise RuntimeError()
        return {self.name: self.explicit_definition}


class EnumTypedef(NamedTypedef):
    def __init__(self, schema: "Schema", name: str, values: list[str]):
        super().__init__(schema, name)
        self.values = values

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        if as_toplevel:
            raise RuntimeError()
        return {self.name: {"type": "string", "enum": self.values}}


class Struct(NamedTypedef):
    def __init__(self, schema: "Schema", name: str, typ: type):
        super().__init__(schema, name)
        self.typ = typ
        self.properties = {}

    def schema_closed(self):
        base_hints = set()
        for base in self.typ.__mro__[1:]:
            for name in typing.get_type_hints(base, self.schema.types_by_name, inspect.getmodule(base).__dict__).keys():
                base_hints.add(name)

        with_annotated = typing.get_type_hints(self.typ, self.schema.types_by_name, inspect.getmodule(self.typ).__dict__, include_extras=True)
        for (name, hint) in typing.get_type_hints(self.typ, self.schema.types_by_name, inspect.getmodule(self.typ).__dict__).items():
            if name in base_hints:
                continue
            doc = None
            constraints = []
            if typing.get_origin(with_annotated[name]) is typing.Annotated:
                for extra in typing.get_args(with_annotated[name])[1:]:
                    if isinstance(extra, str):
                        doc = extra
                    elif isinstance(extra, Constraint):
                        constraints.append(extra)
                    else:
                        raise ValueError(extra)

            if typing.get_origin(hint) is typing.Union:
                optional = True
                (hint, null) = typing.get_args(hint)
                assert null is types.NoneType
            else:
                optional = False

            if typing.get_origin(hint) is list:
                islist = True
                (hint,) = typing.get_args(hint)
            else:
                islist = False

            if hint is str:
                regexp = None
                for c in constraints:
                    if isinstance(c, Regexp):
                        regexp = c.regexp
                    else:
                        raise ValueError()
                self.properties[name] = StringHint(doc, optional, islist, regexp=regexp)

            elif isinstance(hint, type) and issubclass(hint, enum.Enum) and hint not in self.schema.typedefs_by_type:
                self.properties[name] = StringHint(doc, optional, islist, enum=[x.name.strip("_") for x in hint])

            elif isinstance(hint, type) and hint in self.schema.typedefs_by_type:
                if constraints:
                    raise ValueError()
                self.properties[name] = ReferenceHint(doc, optional, islist, self.schema.typedefs_by_type[hint])

            else:
                raise ValueError(hint)

    def recursively_referenced_typedefs(self) -> set[NamedTypedef]:
        referenced = set()
        to_check = [self]
        while to_check:
            td = to_check.pop()
            if td not in referenced:
                referenced.add(td)
                for v in self.properties.values():
                    if isinstance(v, ReferenceHint) and v.referenced_typedef not in referenced:
                        to_check.append(v.referenced_typedef)
        referenced.remove(self)
        return referenced

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        base_schema = {
            "type": "object",
            "properties": {
                p: h.to_json_schema() for (p, h) in self.properties.items()
            }
        }
        if as_toplevel:
            defs = {}
            for td in sorted(self.recursively_referenced_typedefs(), key=lambda t: t.name):
                defs |= td.json_schema_definition(as_toplevel=False)

            jsonschema = {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "version": "1.0.0",
                "title": self.name,
                "$defs": defs
            }
            jsonschema |= base_schema
            jsonschema["required"] = [n for (n, p) in self.properties.items() if not p.optional]
            jsonschema["unevaluatedProperties"] = False
        else:
            jsonschema = {
                self.name: base_schema
            }
        return jsonschema


class Schema:
    def __init__(self):
        self.typedefs_by_name: dict[str, NamedTypedef] = {}
        self.typedefs_by_type: dict[type, NamedTypedef] = {}
        self.types_by_name: dict[str, type] = {}

    def load_module(self, m):
        for name in dir(m):
            obj = getattr(m, name)
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

    def close_schema(self):
        for t in self.typedefs_by_name.values():
            t.schema_closed()

    def make_single_schema(self, toplevel_name: str) -> dict:
        return self.typedefs_by_name[toplevel_name].json_schema_definition(as_toplevel=True)
