from schemagen import Schema

import top2

sch = Schema()
sch.load_module(top2)
sch.close_schema()

md = sch.make_markdown_string(4)
with open("/Users/viktor/src/TOP/TOP-autogen.md", "w") as fp:
    fp.write(md)

