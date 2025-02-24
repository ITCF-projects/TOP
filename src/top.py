import json

from schemagen import Schema

import top2

sch = Schema()
sch.load_module(top2)
# sch.load_modules(top2.common, top2.communication, top2.deployment, top2.job, top2.organization,
#                  top2.person, top2.remuneration, top2.responsibility, top2.work_life_cycle, top2.work_schedule,
#                  top2.message)
# print("\n".join(sorted(sch.types_by_name.keys())))
sch.close_schema()

print(json.dumps(sch.make_single_schema("Message"), indent=2))
