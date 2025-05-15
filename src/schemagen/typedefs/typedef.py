
from typing import *

if TYPE_CHECKING:
    from schemagen.schema import Schema


class Typedef:
    def __init__(self, schema: "Schema", name: str):
        self.schema = schema
        self.name = name
        self.description = ""

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

    def specific_markdown_doc(self, top_chapter: int, sub_chapter: int) -> list[int]:
        return []

    def markdown_doc(self, top_chapter: int, sub_chapter: int=0) -> list[str]:
        md = [
            f'## {top_chapter}.{sub_chapter} <a name="{self.name}">{self.name}</a>',
            '',
            self.description.replace("    ", ""),
            ''
        ] + self.specific_markdown_doc(top_chapter, sub_chapter)
        return md
