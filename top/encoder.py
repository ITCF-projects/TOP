import copy
import dataclasses
import enum
import inspect
import json
import time
import typing
from typing import *
from top import *

def to_json(obj) -> str:
    def _convert(obj) -> Any:
        if dataclasses.is_dataclass(obj):
            dct = dict()
            if hasattr(obj, "_json_type_name"):
                dct["__type"] = obj._json_type_name
            for field in dataclasses.fields(obj):
                value = _convert(getattr(obj, field.name))
                if value is not None:
                    dct[field.name] = value
            return dct
        elif isinstance(obj, Mapping):
            return {_convert(k): _convert(v) for (k, v) in obj.items()}
        elif isinstance(obj, Collection) and not isinstance(obj, (str, bytes, enum.Enum)):
            return [_convert(v) for v in obj]
        else:
            return copy.deepcopy(obj)

    return json.dumps(_convert(obj), indent=2)


class _Field:
    def __init__(self, type_hint: type, is_list: bool, optional: bool, docstring: str, constraints: List[Constraint]):
        self.type = type_hint
        self.is_list = is_list
        self.optional = optional
        self.docstring = docstring or ""
        self.constraints = constraints

    @classmethod
    def unique_hints(cls, typ: type) -> "dict[str, _Field]":
        """Return a mapping from attribute name to _Field instance for all fields defined in <typ> itself
        (i.e. excluding any field defined in its base classes). We use JSON Schema includes, so the base
        class fields will already be defined by the base class type.
        """
        hints = typing.get_type_hints(typ, globalns=globals())
        hints_with_extra = typing.get_type_hints(typ, globalns=globals(), include_extras=True)

        base_hints = {}
        for base_class in typ.__mro__[1:]:
            base_hints |= typing.get_type_hints(base_class)

        res = {}
        for (attr, hint) in hints.items():
            if attr in base_hints:
                continue
            doc = None
            constraints = []
            if typing.get_origin(hints_with_extra[attr]) is Annotated:
                for extra in typing.get_args(hints_with_extra[attr])[1:]:
                    if isinstance(extra, str):
                        doc = extra
                    elif isinstance(extra, Constraint):
                        constraints.append(extra)
                    else:
                        raise ValueError(extra)
            optional = attr in typ.__dict__
            if typing.get_origin(hint) is list:
                res[attr] = _Field(typing.get_args(hint)[0], True, optional, doc, constraints)
            else:
                res[attr] = _Field(hint, False, optional, doc, constraints)
        return res

    def __str__(self):
        return f"<_Field {'list of ' if self.is_list else ''}{self.type} optional={self.optional} '{self.docstring}'>"


class _Model:
    _singleton_cache: "dict[type, _Model]" = {}

    def __init__(self, kls: type):
        self.type = kls
        self.name = kls.__name__
        self.docstring = kls.__doc__ if isinstance(kls.__doc__, str) else ""
        self.fields: dict[str, _Field] = _Field.unique_hints(kls)
        self.includes: "Set[_Model]" = {self.__class__.from_class(b) for b in kls.__mro__[1:] if dataclasses.is_dataclass(b)}

    @classmethod
    def from_class(cls, kls: type) -> "_Model":
        if kls not in cls._singleton_cache:
             cls._singleton_cache[kls] = cls(kls)
        return cls._singleton_cache[kls]

    def referenced_models(self) -> "Set[_Model]":
        refs = self.includes.copy()
        for field in self.fields.values():
            if dataclasses.is_dataclass(field.type):
                refs.add(_Model.from_class(field.type))
        return refs

    def recursive_references(self) -> "Set[_Model]":
        all_models = {self}
        while True:
            to_add = set()
            for submdl in all_models:
                to_add |= (submdl.referenced_models() - all_models)
            if to_add:
                all_models |= to_add
            else:
                break
        return all_models

    def __str__(self):
        return f'<_Model {self.name} ({self.type}) keys={tuple(self.fields.keys())}, includes={[i.name for i in self.includes]}>'


def _string_defs(constraints: List[Constraint]):
    res = "STRING"
    for c in constraints:
        if isinstance(c, Regexp):
            res += f" REGEXP={c.regexp}"
    return res


def _object_defs(mdl: "_Model") -> List[str]:
    o = [f"OBJECT <{mdl.name}>"]
    o += [f"  DOCSTRING {mdl.docstring.strip()}"]
    for i in mdl.includes:
        o += [f"  INCLUDE <{i.name}>"]

    for (name, field) in mdl.fields.items():
        if field.docstring:
            o += [f"    # {field.docstring}"]

        if field.type is str:
            typedef = _string_defs(field.constraints)
        elif dataclasses.is_dataclass(field.type):
            typedef = f"$ref {_Model.from_class(field.type).name}"
        else:
            typedef = "???"

        if field.is_list:
            typedef = f"LIST[{typedef}]"

        if field.optional:
            typedef = f"OPTIONAL {typedef}"
        o += [f"    {name} {typedef}"]

    return o


def to_json_schema(kls: type) -> str:
    mdl = _Model.from_class(kls)

    json_schema = []
    for ref in sorted(mdl.recursive_references(), key=lambda m: m.name):
        if ref is mdl:
            pass
        json_schema += _object_defs(ref)

    json_schema += ["", f"MAIN"] + _object_defs(mdl)

    return "\n".join(json_schema)


if __name__ == "__main__":
    print(to_json_schema(Message))

