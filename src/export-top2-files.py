
# Modulen schemagen innehåller de typer som används för att definiera TOP i modulen "top2".
from schemagen import Schema

# Importera själva standarden.
import top2

sch = Schema()
sch.load_module(top2)
sch.close_schema()

# Exportera ut TOP-schemat till Markdown.
md = sch.make_markdown_string(4)

# Skriv new markdownen till en fil.
with open("TOP-entities.md", "w") as fp:
    fp.write(md)

# Exportera ut TOP-schemat som JSON-schema, med "Meddelande"-entiteten som toppentitet.
js = sch.make_single_schema_string("Meddelande")
with open("TOP.json", "w") as fp:
    fp.write(md)


