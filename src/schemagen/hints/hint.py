

class Hint:
    def __init__(self, doc: str, optional: bool, is_list: bool):
        self.doc = doc
        self.optional = optional
        self.is_list = is_list

    def to_json_schema(self) -> dict:
        sch = {}
        if self.doc:
            sch["description"] = " ".join(x.strip() for x in self.doc.split("\n"))
        if self.is_list:
            sch |= {"type": "array", "items": self.json_schema_use()}
        else:
            sch |= self.json_schema_use()
        return sch

    def json_schema_use(self) -> dict:
        raise NotImplementedError()

    def cardinalize(self, s: str) -> str:
        if not self.optional:
            return s + "!"
        if self.is_list:
            return f"Lista av {s}"
        return s

    def to_markdown(self) -> str:
        raise NotImplementedError()

