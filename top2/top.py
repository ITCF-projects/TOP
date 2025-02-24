import json

from top2.gen import Schema

import top2.common
import top2.person

sch = Schema()
sch.load_module(top2.common)
sch.load_module(top2.person)
sch.close_schema()

print(json.dumps(sch.make_single_schema("Person"), indent=2))
