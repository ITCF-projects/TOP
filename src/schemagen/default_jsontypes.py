
from schemagen.jsontype import jsontype


@jsontype()
class DateTime(str):
    __json_schema__ = {
        "description": "RFC 3339 (ISO-8601) date and time.",
        "type": "string",
        "pattern": "^((?:(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2}(?:\.\d+)?))(Z|[\+-]\d{2}:\d{2})?)$"
    }


