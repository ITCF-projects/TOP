# TOP-standarden som Python dataclasses

TOP-standarden definierar en informationsmodell och en JSON-kodning av denna modell. TOP-standarden definerar däremot
inga meddelanden eller exakta representationer. Standarden gör ändå stor nytta för avsändare/publicerare och
mottagare/konsumenter av TOP-information:

* _Avsändaren_ kan via standarden alltid veta exakt hur viss information skall överföras.
* _Mottagaren_ kan via standarden alltid veta exakt vad all mottagen data betyder.

Genom att definiera informationsmodell och kodning men lämna meddelanden odefinierade så gör sig TOP-standarden
oberoende av faktiska användningsfall och specifika parters behov. Två parter som skall kommunicera enligt
TOP-standarden behöver fortfarande komma överens om vilken data som skall utväxlas, men därefter bestämmer
TOP-standarden hur överföringen måste se ut.

Det gör också att TOP-standarden går att använda både för GraphQL (där mottagaren vid anrop bestämmer vilken data man
vill hämta), för de som vill ha tunna meddelanden, och för de som vill ha djupt berikade meddelanden.

## Varför är typ allt frivilligt?

För att inte låsa sig vid use-case, så måste väldigt många fält vara frivilliga. För ett personmeddelande med inbäddade
rolltilldelningar så är personattributet på rolltilldelning överflödigt, men för ett meddelande med rolltilldelningar så
måste det vara obligatoriskt.

För vissa datatyper innebär det att man strikt talat kan formera data som följer TOP men som inte går att tolka. Man kan
skicka ett chefskap som varken pekar ut en person, en rolltilldelning eller en organisation. Det är korrekt formerat men
mottagaren kan inte göra något med det.

TOP räknar helt enkelt med att avsändarna är vuxna tänkande människor, som kan fatta kloka beslut om hur man använder
standarden.

## Giltighetstider

Det går att skicka giltighetstider på nästan allt i TOP. Men även om man därmed _kan_ skicka över alla
anställningsperioder en person har haft sedan 1950, så innebär det inte att man _bör_ göra det om det inte verkligen
behövs.

TOP säger att i normalfallet skickar man allt som har ett slutdatum senare än "för tre månader sedan" (där "tillsvidare"
räknas som oändligt slutdatum). Eller, med andra ord, man utelämnar allt som är blev inaktuellt för mer än tre månader
sedan.





