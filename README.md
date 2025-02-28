# TOP

Transfer of Organizations and Persons är backronymen för en standard för hur vi inom sektorn för högre utbildning modellerar och överför information om organisation, personer, och hur de knyts till varandra.

Den är svagt baserad på HROpen (svagare och svagare för varje dag eftersom HROpen både är "corporate" och "private sector"). Den som kan HROpen utan och innan kommer dock att känna igen sig.

Standarden i version Beta 3 finns som [TOP.md](TOP.md) i denna katalog. 

Ett färdiggenererat JSON-schema finns i [TOP.json](TOP.json)

JSON-schemat är automatgenererat utifrån lite Python-kod som ligger i `src/top2`-katalogen. Python-koden är förmodligen mer lättsmält att läsa än JSON-schemat.

För att generera json-schemat, ställ dig i `src`-katalogen och kör `python3 ./top.py` - (eller något motsvarande om du använder såndär Windows). Jag skall nog orka paketera det lite snällare om någon behöver det.

