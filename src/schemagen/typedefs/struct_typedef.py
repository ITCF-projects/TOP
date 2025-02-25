
import re
import enum
import types
import typing
import inspect

from typing import *

from schemagen.typedefs.typedef import Typedef
from schemagen.constraints import Constraint, Regexp, ValueRange
from schemagen.hints import *


if TYPE_CHECKING:
    from schemagen.schema import Schema


class Struct(Typedef):
    def __init__(self, schema: "Schema", name: str, typ: type):
        super().__init__(schema, name)
        self.typ = typ
        self.properties = {}
        self.bases: "list[Typedef]" = []
        self.description = self.typ.__json_args__.get("description", self.typ.__doc__)

    def schema_closed(self):
        # Ugly ass hack! I'm proud! Could be reduced to an ugly hack (as opposed to ugly _ass_ hack)
        # by using the AST module.
        vardef = re.compile("^\s+([_a-zA-Z0-9]+)\s*:\s*[A-za-z]+.*")
        comments = {}
        comment_lines = []
        for srcline in inspect.getsource(self.typ).splitlines():
            if not srcline.strip():
                continue
            elif srcline.strip()[0] == '#':
                comment_lines.append(srcline.strip()[1:].strip())
            elif mo := vardef.match(srcline):
                if comment_lines:
                    comments[mo.groups()[0]] = " ".join(comment_lines)
                comment_lines = []
            else:
                comment_lines = []

        for b in self.typ.__bases__:
            if base_td := self.schema.typedefs_by_type.get(b, None):
                self.bases.append(base_td)

        base_hints = set()
        for base in self.typ.__mro__[1:]:
            for name in typing.get_type_hints(base, self.schema.types_by_name, inspect.getmodule(base).__dict__).keys():
                base_hints.add(name)

        with_annotated = typing.get_type_hints(self.typ, self.schema.types_by_name,
                                               inspect.getmodule(self.typ).__dict__, include_extras=True)
        for (name, hint) in typing.get_type_hints(self.typ, self.schema.types_by_name,
                                                  inspect.getmodule(self.typ).__dict__).items():
            if name in base_hints:
                continue
            doc = None
            constraints = []

            if name in comments:
                doc = comments[name]

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
            elif hasattr(self.typ, name) and getattr(self.typ, name) is None:
                optional = True
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

            elif hint is int:
                range = None
                for c in constraints:
                    if isinstance(c, ValueRange):
                        range = c.range
                    else:
                        raise ValueError()
                self.properties[name] = IntegerHint(doc, optional, islist, value_range=range)

            elif hint is float:
                self.properties[name] = NumberHint(doc, optional, islist)

            elif hint is bool:
                self.properties[name] = BooleanHint(doc, optional, islist)

            elif isinstance(hint, type):
                if issubclass(hint, enum.Enum) and hint not in self.schema.typedefs_by_type:
                    self.properties[name] = StringHint(doc, optional, islist, enum=[x.name.strip("_") for x in hint])

                elif hint in self.schema.typedefs_by_type:
                    if constraints:
                        raise ValueError()
                    self.properties[name] = ReferenceHint(doc, optional, islist, self.schema.typedefs_by_type[hint])

                else:
                    raise ValueError(
                        f"{self.typ.__name__}.{name}: {hint} - type not found (did you forget to decorate it with @jsontype()?"
                    )

            else:
                raise ValueError(hint)

    def directly_referenced_typedefs(self) -> "set[Typedef]":
        refs = {v.referenced_typedef for v in self.properties.values() if isinstance(v, ReferenceHint)}
        refs |= set(self.bases)
        return refs

    def reflow(self, t):
        reflowed = [""]
        for word in t.split():
            if len(reflowed[-1]) + len(word) > 120:
                reflowed.append("")
            if reflowed[-1]:
                reflowed[-1] += " "
            reflowed[-1] += word
        return "\n".join(reflowed)

    def json_schema_definition(self, *, as_toplevel: bool) -> dict:
        base_schema = {"type": "object"}
        if self.description:
            base_schema["description"] = self.reflow(self.description)
        if self.bases:
            base_schema["allOf"] = [b.json_schema_use() for b in self.bases]
        base_schema["properties"] = {
            p: h.to_json_schema() for (p, h) in self.properties.items()
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


