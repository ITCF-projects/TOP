from schemagen import Schema

import top2

sch = Schema()
sch.load_module(top2)
sch.close_schema()

js = sch.make_single_schema_string("Message")
print(js)
