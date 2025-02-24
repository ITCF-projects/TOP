
from top2.gen import jsontype


@jsontype()
class WithId:
    id: str
    correlationIds: list[str] = None


@jsontype()
class I18NText:
    __json_schema__ = {
        "patternProperties": {
            "^[a-z.-]+$": {"type": "object"}
        }
    }
