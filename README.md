# TOP

Transfer of Organizations and Persons är backronymen för en standard för hur vi inom sektorn för högre utbildning modellerar och överför information om organisation, personer, och hur de knyts till varandra.

Den är svagt baserad på HROpen (svagare och svagare för varje dag eftersom HROpen både är "corporate", "private sector" och "American international standard").

Standarden i version Beta 3 finns som Markdown i [TOP-entities.md](TOP-entities.md) i denna katalog. Exempel och bakgrundsinformation ligger i [TOP-standard.md](TOP-standard.md). Ett färdiggenererat JSON-schema finns i [TOP.json](TOP.json)

Schemat definieras av Python-kod i modulen `src/top2`. Den använder `src/schemagen`, som är hemmaskriven. Men titta i `src/top2` så tror jag att du hänger med i hur den fungerar!

Om man ändrar på schemat i `src/top2` så  

JSON-schemat är automatgenererat utifrån  Python-kod som ligger i `src/top2`-katalogen. Python-koden är förmodligen mer lättsmält att läsa än JSON-schemat.

För att generera json-schemat, ställ dig i `src`-katalogen och kör `python3 ./top.py` - (eller något motsvarande om du använder såndär Windows). Jag skall nog orka paketera det lite snällare om någon behöver det.

