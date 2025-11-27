# 4 Entiteter

## 4.1 <a name="Date">Date</a>



## 4.2 <a name="DateTime">DateTime</a>



## 4.3 <a name="Anknytningsavtal">Anknytningsavtal</a>

Ett anknytningsavtal säger att en person knutits till lärosätet och hur, men säger inte vad
personen gör (det finns i Rolltilldelning).

Den vanligaste formen av anknytningsavtal är ett anställningsavtal. Ett annat exempel är när
en professor muntligen bjuder in en forskarkollega från Harvard för att sprida stjärnglans
genom ett löst samarbete. En konsult som hyrs in på enstaka timmar i ett projekt, en
bemanningskonsult som hyrs in på årsbasis, avtalet som tar in en företags/industridoktorand,
och ett beslut om att någon ges emeriti-status är andra exempel.

Varje anknytningsavtal har en typ som säger hur personen knutits in till lärosätet (t.ex.
"emeritus", "anställd", "forskande gäst" eller "bemanningspersonal").

Under ett långvarigt anknytningsavtal kan viss data naturligt variera utan att avtalet skrivs om.
Dessa har egna entitetstyper:

* Under en _ersättningsperiod_ utgår ersättning - t.ex. lön - till personen.
* Under en _omfattningsperiod_ finns en bestämd omfattning (dvs ett visst antal timmar eller
timmar/vecka) av tid som personen tillför lärosätet.
* Under en _frånvaroperiod_ minskar omfattningen t.ex. på grund av semester, tjänstledighet,
sjukskrivningar, föräldraledighet eller liknande.
* En _hemvistperiod_ säger var personen har sin organisatoriska hemvist - normalt där ens chef är.

Till skillnad från Primula så skapas alltså inte ett nytt anknytningsavtal varje gång någon byter lön,
får tjänstledigt, eller byter enhet i organisationen, utan dessa varierar inom samma avtal.

Det är mycket vanligt att behöva förmedla vilka avtalsperioder som motsvarar t.ex.
"anställningsliknande former", och därför har avtalsperioder ett flervärt "tag"-fält där sådan tolkad
information kan läggas.


### 4.3.1 Attribut

### 4.3.1 `person`
Typ: [`Person`](Person)

Den person som detta anknytningsavtal gäller.


### 4.3.2 `typ`
Typ: [`Tagg`](Tagg)!

Typ av anknytningsavtal, t.ex. "anställning", "delegering" eller "muntligt avtal".


### 4.3.3 `organisationellAvtalspart`
Typ: [`Organisationsdel`](Organisationsdel)

Den organisationsdel som är motpart i avtalet. För anställningsavtal är detta lärosätet som helhet, och vilken organisationsdel (t.ex. institution eller avdelning) personen har sin chef/ansvarige pekas ut via hemvistperioder. För muntliga avtal är motparten den institution eller liknande vars chef gjort överenskommelsen.


### 4.3.4 `hemvistperioder`
Typ: Lista av [`Hemvistperiod`](Hemvistperiod)

Organisatorisk(a) hemvist(er) - på vilken organisationsdel placerar detta avtal just nu personen. Bara en får vara giltig åt gången, men det går här att lägga in både dåtida och framtida orghemvister om man kan och vill.


### 4.3.5 `omfattningsperioder`
Typ: Lista av [`Omfattningsperiod`](Omfattningsperiod)

Omfattningar för detta anknytningsavtal.


### 4.3.6 `rolltilldelningar`
Typ: Lista av [`Rolltilldelning`](Rolltilldelning)

Rolltilldelningar i kontexten av detta avtal.


### 4.3.7 `franvaroperioder`
Typ: Lista av [`Franvaroperiod`](Franvaroperiod)

Frånvaroperioder. Alla förhållanden som minskar omfattningen (.workSchedule) under någon period, t.ex. semester, tjänstledighet eller sjukskrivning.


### 4.3.8 `lopandeErsattningar`
Typ: Lista av [`LopandeErsattning`](LopandeErsattning)

Lön eller ersättning. Kan vara flera, och kan variera under giltighetstiden. Lönetillägg för specifika rolltilldelningar (t.ex. prefekttillägg) läggs i rolltilldelningen.


### 4.3.9 `engangsersattningar`
Typ: Lista av [`Engangsersattning`](Engangsersattning)

Engångsersättningar för detta anknytningsavtal.


### 4.3.10 `begransningskod`
Typ: `boolean`

Begränsningskoden talar om varför någon inte har en fastanställning.


### 4.3.11 `arHuvudavtal`
Typ: `boolean`

Om du, av någon anledning, inte kan hantera att personer omfattas av mer än ett avtal, ta det här avtalet.


### 4.3.12 `underordnat`
Typ: [`Anknytningsavtal`](Anknytningsavtal)

Detta avtal är underordnat ett annat (t.ex. kan en delegering vara underordnad en anställning), det är ett "hängavtal". Giltigheten på detta avtal begränsas därmed av giltigheten på det utpekade avtalet.


### 4.3.13 `underordnade`
Typ: Lista av [`Anknytningsavtal`](Anknytningsavtal)

Andra avtal som är underordnade detta. De underordnade avtalen kan aldrig vara giltiga när detta avtal inte är det.


### 4.3.14 `avslutsorsak`
Typ: `boolean`

Om vi vill veta varför ett visst avtal har avslutats så kan vi skriva något om det här.


### 4.3.15 `avslutsorsakskoder`
Typ: Lista av [`Tagg`](Tagg)

aanstperiod.avslutdkod_id -> avslutskod.typ (typ är t.ex. "1" för S1). Det finns för t.ex. anställningar formella koder till pensionsmyndigheten (S1-S9). Dessa är taggar som man kan lägga in här.


### 4.3.16 `anstallningsnummer`
Typ: `integer`

Anställningsnummer används vid rapporter till Skatteverket med mera.


### 4.3.17 `befattningsnamn`
Typ: `boolean`

Befattningarna är lönenära och matchar nästan, men inte riktigt, rollen.


### 4.3.18 `befattningskategori`
Typ: `boolean`


### 4.3.19 `befattningskodSCB`
Typ: `boolean`


### 4.3.20 `BESTA`
Typ: `boolean`

BESTA-kod (9 tecken).


### 4.3.21 `skatt`
Typ: [`Skatt`](Skatt)


## 4.4 <a name="MedObligatoriskIdentifierare">MedObligatoriskIdentifierare</a>

MedObligatoriskIdentifierare(*, postid: top2.common.Identifierare, korrelationsidn: list[top2.common.Identifierare] = None, sammanslagnaIdn: list[top2.common.Identifierare] = None, tidigareKorrelationsidn: list[top2.common.Identifierare] = None)

### 4.4.1 Attribut

### 4.4.1 `postid`
Typ: [`Identifierare`](Identifierare)!

Huvudsakligt ID. Skall "aldrig" ändras, eller i alla fall så sällan det går. Personnummer är dåligt (ändras ofta), medan ett UUID i en lokal personalkatalog kan vara finfint.


### 4.4.2 `korrelationsidn`
Typ: Lista av [`Identifierare`](Identifierare)

ID som kan återfinnas i andra applikationer eller externa system.


### 4.4.3 `sammanslagnaIdn`
Typ: Lista av [`Identifierare`](Identifierare)

Om denna post är resultatet av att andra poster slagits samman, så ligger ID:na för de därmed borttagna posterna här.


### 4.4.4 `tidigareKorrelationsidn`
Typ: Lista av [`Identifierare`](Identifierare)

Om ett korrelations-id försvinner, t.ex. vid ett personnummerbyte, så skickas det id som tidigare varit korrelations-id här under en tid.


## 4.5 <a name="MedTaggning">MedTaggning</a>

MedTaggning(*, taggar: list[top2.common.Tagg] = None, giltighetsbegransadeTaggar: list[top2.common.MedGiltighetsbegransadTaggning] = None)

### 4.5.1 Attribut

### 4.5.1 `taggar`
Typ: Lista av [`Tagg`](Tagg)

Lista över taggar som sitter på posten just nu, där vi inte känner till någon historik/framtid.


### 4.5.2 `giltighetsbegransadeTaggar`
Typ: Lista av [`MedGiltighetsbegransadTaggning`](MedGiltighetsbegransadTaggning)

Lista över taggar som suttit/sitter/kommer att sitta på posten, där vi känner till historik/framtid.


## 4.6 <a name="MedGiltighet">MedGiltighet</a>

MedGiltighet(*, giltighetsperiod: top2.common.Giltighetsperiod = None, utvarderadGiltighet: top2.common.Giltighetsenum = None)

### 4.6.1 Attribut

### 4.6.1 `giltighetsperiod`
Typ: [`Giltighetsperiod`](Giltighetsperiod)

Giltighet. Kan innehålla både en giltighetsperiod och en giltighetsenum. Om värdet utelämnas helt så känner avsändaren varken till start- eller slutdatum, bara att objektet är giltigt just nu.


### 4.6.2 `utvarderadGiltighet`
Typ: `boolean` Value one of "TIDIGARE", "AKTUELLT", "FRAMTIDA")


## 4.7 <a name="MedLokalUtokning">MedLokalUtokning</a>

Plats att lägga alla sina coola extensions på. Se Extension-typen för en beskrivning av innehållet.

### 4.7.1 Attribut

### 4.7.1 `lokalUtokning`
Typ: [`LokalUtokning`](LokalUtokning)!


## 4.8 <a name="BeraknatAnsvar">BeraknatAnsvar</a>

BeraknatAnsvar(*, taggar: list[top2.common.Tagg] = None, giltighetsbegransadeTaggar: list[top2.common.MedGiltighetsbegransadTaggning] = None, giltighetsperiod: top2.common.Giltighetsperiod = None, utvarderadGiltighet: top2.common.Giltighetsenum = None, typ: top2.common.Tagg, ansvarig: 'Person' = None, berord: 'Person' = None)

### 4.8.1 Attribut

### 4.8.1 `typ`
Typ: [`Tagg`](Tagg)!

Ansvarstyp (chef, ekonomiskt ansvarig, arbetsledare...)


### 4.8.2 `ansvarig`
Typ: [`Person`](Person)

Den person som har ansvaret (t.ex. arbetsledaren).


### 4.8.3 `berord`
Typ: [`Person`](Person)

Den person som ansvaret gäller för (t.ex. den arbetsledde).


## 4.9 <a name="Besoksadress">Besoksadress</a>

Besöksadress, eventuellt med öppettider.

### 4.9.1 Attribut

### 4.9.1 `gatuadress`
Typ: `boolean!`

Gatunamn och nummer.


### 4.9.2 `stad`
Typ: `boolean!`

Stad


### 4.9.3 `land`
Typ: `boolean`

Land (implicit om det utelämnas)


### 4.9.4 `byggnad`
Typ: [`SprakhanteradText`](SprakhanteradText)

Byggnadsnamn (t.ex. 'Segerstedtska huset')


### 4.9.5 `hittaIHuset`
Typ: [`SprakhanteradText`](SprakhanteradText)

Instruktioner hur man tar sig till besöksplatsen, t.ex. 'en trappa upp i vänster trapphus, rum 2231 på höger sida' eller 'rum 2231 på plan 2'


### 4.9.6 `besokstider`
Typ: [`Besokstider`](Besokstider)!

Besökstider.


## 4.10 <a name="MedSpridning">MedSpridning</a>

MedSpridning(*, synligheter: list[top2.common.Spridning] = None)

### 4.10.1 Attribut

### 4.10.1 `synligheter`
Typ: Lista av [`Spridning`](Spridning)

Postens synligheter, med postlokal ranking per synlighet.


## 4.11 <a name="Besokstider">Besokstider</a>

En post i en lista av öppettider/besökstider.

### 4.11.1 Attribut

### 4.11.1 `galler`
Typ: [`SprakhanteradText`](SprakhanteradText)!

Beskrivning av när tiderna gäller, t.ex. 'vardagar' eller 'påskafton'.


### 4.11.2 `oppnar`
Typ: `boolean`

Tid på lokal klocka då besök kan börja.


### 4.11.3 `stanger`
Typ: `boolean`

Tid på lokal klocka då besök inte längre kan börja.


### 4.11.4 `avvikelse`
Typ: [`SprakhanteradText`](SprakhanteradText)

Beskrivning som ersätter opens/closes, t.ex. "stängt".


## 4.12 <a name="Bisyssla">Bisyssla</a>

Bisyssla(*, foretag: str, organisationsnummer: str, forvantadFortsattning: str, person: 'Person' = None)

### 4.12.1 Attribut

### 4.12.1 `foretag`
Typ: `boolean!`

BEMANNINGAR är alla formulär BEMANNINGSFALT är alla fälten med namn och kopplat till id i bemanningar BISYSSLA-tabellerna är kopior av BEMANNING-tabellernas innehåll för just bisysslor. För typ combobox är BUFFER kommaseparerade värden... GBEMANNINGSARENDE / GBEMANNINGSARENDEFALT.arende_id aanstallning_id/aperson_id kopplar till individ


### 4.12.2 `organisationsnummer`
Typ: `boolean!`


### 4.12.3 `forvantadFortsattning`
Typ: `boolean!`


### 4.12.4 `person`
Typ: [`Person`](Person)


## 4.13 <a name="ElektroniskAdress">ElektroniskAdress</a>

Elektronisk adress

### 4.13.1 Attribut

### 4.13.1 `media`
Typ: [`Tagg`](Tagg)!

Media. Standarden definierar taggar för t.ex. web och epost, men det är fritt att definiera egna för specifika media.


### 4.13.2 `adress`
Typ: `boolean!`

Adressen. Utseendet beror på media. För epost är det t.ex. en epostadress, för web en URL.


## 4.14 <a name="Engangsersattning">Engangsersattning</a>

Engångsersättning, t.ex. ett arvode.

### 4.14.1 Attribut

### 4.14.1 `typ`
Typ: [`Tagg`](Tagg)!

Typen av ersättning, t.ex. arvode.


### 4.14.2 `utbetalningsdatum`
Typ: [`Date`](Date)!


### 4.14.3 `varde`
Typ: `number!`

Monetärt värde, per utbetalning.


### 4.14.4 `valuta`
Typ: `boolean!`

Valuta


### 4.14.5 `konteringar`
Typ: Lista av [`Kontering`](Kontering)

Hur summan delas upp på olika konteringar.


### 4.14.6 `detaljerarRolltilldelning`
Typ: [`Rolltilldelning`](Rolltilldelning)

Den rolltilldelningsperiod som denna ersättning detaljerar.


### 4.14.7 `detaljerarAnknytningsperiod`
Typ: [`Anknytningsavtal`](Anknytningsavtal)

Den anknytningsperiod som denna ersättning detaljerar.


## 4.15 <a name="Franvaroperiod">Franvaroperiod</a>

En frånvaroperiod uttrycker semester, föräldraledighet, sjukskrivningar med mera. Det finns möjlighet
att ange en omfattning om man önskar.


### 4.15.1 Attribut

### 4.15.1 `heltidsandel`
Typ: `number`

Andel av heltid, som ett flyttal.


### 4.15.2 `timmar`
Typ: `integer`

Ett visst antal timmar.


### 4.15.3 `betaldFranvaro`
Typ: `boolean`

Betald eller obetald frånvaro.


### 4.15.4 `slutdatumArPreliminart`
Typ: `boolean`

Om sann så är slutdatumet på perioden preliminärt, t.ex. slutdatum på en längre sjukskrivning som kan få en fortsättning. Om falsk så förväntas personens frånvaro sluta enligt giltigheten, t.ex. en beviljad semesterperiod.


### 4.15.5 `anknyntningsperiod`
Typ: [`Anknytningsavtal`](Anknytningsavtal)

Den anknytningsperiod som denna frånvaroperiod detaljerar.


## 4.16 <a name="MedFrivilligIdentifierare">MedFrivilligIdentifierare</a>

MedFrivilligIdentifierare(*, postid: top2.common.Identifierare = None, korrelationsidn: list[top2.common.Identifierare] = None, sammanslagnaIdn: list[top2.common.Identifierare] = None, tidigareKorrelationsidn: list[top2.common.Identifierare] = None)

### 4.16.1 Attribut

### 4.16.1 `postid`
Typ: [`Identifierare`](Identifierare)

Huvudsakligt ID (om något finns). Skall "aldrig" ändras, eller i alla fall så sällan det går. Personnummer är dåligt (ändras ofta), medan ett UUID i en lokal personalkatalog kan vara finfint.


### 4.16.2 `korrelationsidn`
Typ: Lista av [`Identifierare`](Identifierare)

ID:n som kan återfinnas i andra applikationer eller externa system.


### 4.16.3 `sammanslagnaIdn`
Typ: Lista av [`Identifierare`](Identifierare)

Om denna post är resultatet av att andra poster slagits samman, så ligger ID:na för de därmed borttagna posterna här.


### 4.16.4 `tidigareKorrelationsidn`
Typ: Lista av [`Identifierare`](Identifierare)

Om ett korrelations-id försvinner, t.ex. vid ett personnummerbyte, så skickas det id som tidigare varit korrelations-id här under en tid.


## 4.17 <a name="MedTyptagg">MedTyptagg</a>

MedTyptagg(*, typ: top2.common.Tagg)

### 4.17.1 Attribut

### 4.17.1 `typ`
Typ: [`Tagg`](Tagg)!

En ensam tag som representerar objektets typ.


## 4.18 <a name="Giltighetsperiod">Giltighetsperiod</a>

En tidsperiod inom vilken ett associerat värde är giltigt. Om invalidFrom 

### 4.18.1 Attribut

### 4.18.1 `giltigFrom`
Typ: [`DateTime`](DateTime)!


### 4.18.2 `ogiltigFrom`
Typ: [`DateTime`](DateTime)


## 4.19 <a name="Hemvistperiod">Hemvistperiod</a>

Säger att den organisatoriska hemvisten för ett visst anknytningsavtal under viss period ligger
på en viss orgenhet. Den organisatoriska hemvisten används för att beräkna var ansvaret för en
person ligger (t.ex. chefsansvar).


### 4.19.1 Attribut

### 4.19.1 `organisationsdel`
Typ: [`Organisationsdel`](Organisationsdel)!

Den organisatoriska enhet som ansvarar för den person som anknyntningsavtalet gäller.


### 4.19.2 `anknytningsperiod`
Typ: [`Anknytningsavtal`](Anknytningsavtal)

Det anknytningsavtal som denna orghemvist detaljerar.


## 4.20 <a name="Identifierare">Identifierare</a>

Identifierare med typ och värde. Två identifierare är identiska endast om namnrymd, typnamn, varde
och varderymd (om den är angiven) är identiska.

Syftet med namnrymden är att vi är många som kanske vill definiera en typ "person-id", och om sådana
identifierare riskerar att mötas i något system skulle man kunna missta dem som samma identifierare.

På samma sätt finns varderymd som är en namnrymd för värdet. Dess syfte är att kunna förmedla
identifierare från t.ex. testinstanser utan risk att de misstas för skarpa värden.


### 4.20.1 Attribut

### 4.20.1 `namnrymd`
Typ: `boolean!`

Namnrymd för typen, väsentligen är detta den som definierat typnamnet. Det möjliggör att t.ex. både Chalmers och GU kan ha typer som heter "person-id". Skall vara '*' om TOP definierar typen, annars något URL-liknande med minst ett domännamn för den som definierat semantiken för typen.


### 4.20.2 `typnamn`
Typ: `boolean!`

Kombinationen av (typDefinieradAv, typnamn) är en unikt definierad typ av identifierare, med semantik enligt vad typDefinieradAv bestämt.


### 4.20.3 `varde`
Typ: `boolean!`

Värde


### 4.20.4 `varderymd`
Typ: `boolean`

Domännamn eller liknande identifierare som ger en kontext för kombinationen (schemeAgencyId, schemeId, value) om samma typ+värde finns i olika kontexter (t.ex. olika instanser av samma applikation). Behöver bara användas när det finns en risk att sådana värden möts i samma mottagare. Oftast på formen "lärosäte.se/applikationsinstans"


## 4.21 <a name="Kommunikation">Kommunikation</a>

Ett kommunikationsvägar-objekt innehåller upp till fyra listor av adresser/kontaktinformation
för fyra olika typer av kontakt - epost (och andra elektroniska adresser), telefon (och fax mm),
fysiskt besök, och snigelpost.

Gemensamt för alla typerna är att avsändaren kan förse dem med en lista av vilka kanaler varje
adress/nummer får spridas. Till exempel så kan Lilla Lärosätets rektor välja att adressen
`rektor@lillalarosatet.se` publiceras på externwebben, medan hennes personliga adress
`hedda.master@lillalarosatet.se` inte publiceras där.

Tillsammans med synligheten kan man också ge en prioritet. När man måste bestämma en ordning
mellan flera synliga objekt (för att ringa upp, för att visa på personkortet på hemsidan, eller
för att sortera flera epostadresser t.ex.), så sorterar man dem på fallande värde, och tar det
som har högst prioritetsvärde först. Saknas prioritet räknas den som 0.


### 4.21.1 Attribut

### 4.21.1 `telefon`
Typ: Lista av [`Telefonnummer`](Telefonnummer)


### 4.21.2 `snigelpost`
Typ: Lista av [`Snigelpost`](Snigelpost)


### 4.21.3 `elektronisk`
Typ: Lista av [`ElektroniskAdress`](ElektroniskAdress)


### 4.21.4 `besok`
Typ: Lista av [`Besoksadress`](Besoksadress)


## 4.22 <a name="Kontering">Kontering</a>

Kontering(*, taggar: list[top2.common.Tagg] = None, giltighetsbegransadeTaggar: list[top2.common.MedGiltighetsbegransadTaggning] = None, konton: list[top2.common.Identifierare], varde: float)

### 4.22.1 Attribut

### 4.22.1 `konton`
Typ: [`Identifierare`](Identifierare)!

Alla relevanta ID:n för att göra en tillräckligt detaljerad specifikation (konto, kostnadsställe, mm)


### 4.22.2 `varde`
Typ: `number!`

Den del av värdet som konteras på detta sätt. När en ersättning konteras skall summan av alla Kontering bli samma som ersättnings totalvärde. Valutan är samma som ersättningens valuta.


## 4.23 <a name="KontextualiseradOrganisationsdelsrelation">KontextualiseradOrganisationsdelsrelation</a>

En kontextualiserad relation med en orgenhet. Används i Organization.filterRelations. Taggen kan
t.ex. representera filterkontexten "en del av", och peka ut alla orgenheter som en viss orgenhet
kan anses vara "en del av".


### 4.23.1 Attribut

### 4.23.1 `type`
Typ: [`Tagg`](Tagg)!

Den struktur där relationen gäller.


### 4.23.2 `organisationsdelar`
Typ: [`Organisationsdel`](Organisationsdel)!

De organisatoriska delar som pekas ut av relationen i denna struktur.


## 4.24 <a name="LokalUtokning">LokalUtokning</a>



## 4.25 <a name="LopandeErsattning">LopandeErsattning</a>

Löpande ersättningar, t.ex. lön eller tillägg. Vilken typ av ersättning, liksom hur ofta
och när den utbetalas, måste förstås av typtaggen.


### 4.25.1 Attribut

### 4.25.1 `typ`
Typ: [`Tagg`](Tagg)!

Ersättningstypen, t.ex. månadslön eller lönetillägg.


### 4.25.2 `varde`
Typ: `number!`

Monetärt värde, per utbetalning.


### 4.25.3 `valuta`
Typ: `boolean!`

Valuta


### 4.25.4 `konteringar`
Typ: Lista av [`Kontering`](Kontering)

Hur summan delas upp på olika konteringar.


### 4.25.5 `detaljerarRolltilldelning`
Typ: [`Rolltilldelning`](Rolltilldelning)

Den rolltilldelning som denna period detaljerar.


### 4.25.6 `detaljerarAnknytningsperiod`
Typ: [`Anknytningsavtal`](Anknytningsavtal)

Den anknytningsperiod som denna period detaljerar.


## 4.26 <a name="MedGiltighetsbegransadTaggning">MedGiltighetsbegransadTaggning</a>

MedGiltighetsbegransadTaggning(*, giltighetsperiod: top2.common.Giltighetsperiod = None, utvarderadGiltighet: top2.common.Giltighetsenum = None, tagg: top2.common.Tagg)

### 4.26.1 Attribut

### 4.26.1 `tagg`
Typ: [`Tagg`](Tagg)!

Lista över taggar som sitter/satt/kommer sitta på posten under giltigheten.


## 4.27 <a name="Meddelande">Meddelande</a>

Toppobjekt med enkla och listvärda referenser till samtliga värdeobjekt. Bra grund för meddelanden,
även t.ex. en lysande topp-Query för ett GraphQL-gränssnitt.


### 4.27.1 Attribut

### 4.27.1 `anknytningsperiod`
Typ: [`Anknytningsavtal`](Anknytningsavtal)


### 4.27.2 `anknytningsperioder`
Typ: Lista av [`Anknytningsavtal`](Anknytningsavtal)


### 4.27.3 `organisationsdel`
Typ: [`Organisationsdel`](Organisationsdel)


### 4.27.4 `organisationsdelar`
Typ: Lista av [`Organisationsdel`](Organisationsdel)


### 4.27.5 `passerkort`
Typ: [`Passerkort`](Passerkort)


### 4.27.6 `passerkortslista`
Typ: Lista av [`Passerkort`](Passerkort)


### 4.27.7 `passerbehorighet`
Typ: [`Passerbehorighet`](Passerbehorighet)


### 4.27.8 `passerbehorigheter`
Typ: Lista av [`Passerbehorighet`](Passerbehorighet)


### 4.27.9 `person`
Typ: [`Person`](Person)


### 4.27.10 `personer`
Typ: Lista av [`Person`](Person)


### 4.27.11 `roll`
Typ: [`Roll`](Roll)


### 4.27.12 `roller`
Typ: Lista av [`Roll`](Roll)


### 4.27.13 `rolltilldelning`
Typ: [`Rolltilldelning`](Rolltilldelning)


### 4.27.14 `rolltilldelningar`
Typ: Lista av [`Rolltilldelning`](Rolltilldelning)


## 4.28 <a name="Omfattningsperiod">Omfattningsperiod</a>

En mängd arbetstid som personen i kontexten av ett anknytningsavtal förväntas utföra (en
omfattningsperiod). Kan antingen vara ett visst antal timmar (hours) eller en del av heltid
(fullTimeEquivalentRatio). Kan alltså tillsammans med giltighetstider uttrycka '200 timmar under 2023',
'20% under januari 2024' och '95% av en heltid löpande'. Syftet är att överföra förutsättningar,
inte utfall. Avsikten är alltså inte att den skall representera en timrapport.


### 4.28.1 Attribut

### 4.28.1 `heltidsandel`
Typ: `number`

Andel av heltid, som ett flyttal.


### 4.28.2 `timmar`
Typ: `integer`

Ett visst antal timmar.


### 4.28.3 `timmarPerDag`
Typ: `Lista av number`

Fördelning av timmar över veckodagar.


### 4.28.4 `rolltilldelning`
Typ: [`Rolltilldelning`](Rolltilldelning)

Den rolltilldelning som denna omfattningsperiod detaljerar.


### 4.28.5 `anknytningsperiod`
Typ: [`Anknytningsavtal`](Anknytningsavtal)

Den anknytningsperiod som denna omfattningsperiod detaljerar.


## 4.29 <a name="Organisationsdel">Organisationsdel</a>

Representerar någon form av gruppering som är viktig för hur lärosätet organiserar en viss
aspekt av sitt arbete. Inga gränser sätts för vad som är eller inte är en organisationsdel,
varje lärosäte avgör utifrån behov och förmåga. Exempel på möjliga orgenheter är:

* Fakultet
* Institution
* Utbildningsprogram (om lärosätet har matrisorganisation t.ex.)
* Administrativ enhet
* Utvecklingsprojekt (kanske bara centralt finansierade eller av viss storlek)
* Kurstillfälle (ur genomförande perspektivet)
* Centran (av viss storlek, eller även "kaffereps-centran")
* Excellensinitiativ (ja, det begreppet finns på ett lärosäte)

Gemensamt är att de är väl definierade grupper med gemensamma mål och tydliga relationer till
andra organisationsdelar, där någon person ansvarar för gruppens ekonomi, och någon person
ansvarar för att arbetsleda gruppens gemensamma arbete.


### 4.29.1 Attribut

### 4.29.1 `namn`
Typ: [`SprakhanteradText`](SprakhanteradText)

Orgenhetens namn.


### 4.29.2 `typer`
Typ: Lista av [`Tagg`](Tagg)

Orgenhetens typ(er). Övriga taggningar som inte kan sägas vara dess typ läggs i stället i de vanliga taggningsattributen. "Institution" är t.ex. tydligt en typ av organisation, men om "resultatenhet" är en typ eller en taggning är upp till varje lärosäte att avgöra.


### 4.29.3 `kommunikationsvagar`
Typ: [`Kommunikation`](Kommunikation)

Kommunikationsvägar till orgenheten som abstrakt entitet, t.ex. en info@institution-epostadress.


### 4.29.4 `rolltilldelningar`
Typ: Lista av [`Rolltilldelning`](Rolltilldelning)

Rolltilldelningar, som knyter personer till orgenheten i betydelsen att de utför arbete åt den.


### 4.29.5 `servicefunktioner`
Typ: Lista av [`Servicefunktion`](Servicefunktion)

Servicefunktioner (t.ex. expeditioner) som erbjuder tjänster för denna orgenhet.


### 4.29.6 `motpartForAnknytningsavtal`
Typ: Lista av [`Hemvistperiod`](Hemvistperiod)

Anknytningsavtal för vilka denna orgenhet är motpart. Används t.ex. för att hitta vem som är en persons lönesättande chef.


### 4.29.7 `ansvarshallare`
Typ: Lista av [`Organisationsdelsansvar`](Organisationsdelsansvar)

Personer med vissa ansvar för denna orgenhet, utpekade personligen eller via en rolltilldelning.


### 4.29.8 `foralderrelationer`
Typ: Lista av [`OrganisatoriskRelation`](OrganisatoriskRelation)

Relationer som definierar denna orgenhets förälder/föräldrar. Andra änden av OrganizationalRelation.child.


### 4.29.9 `barnrelationer`
Typ: Lista av [`OrganisatoriskRelation`](OrganisatoriskRelation)

Relationer som definierar denna orgenhets barn. Andra änden av OrganizationalRelation.parent.


### 4.29.10 `filterrelationer`
Typ: Lista av [`KontextualiseradOrganisationsdelsrelation`](KontextualiseradOrganisationsdelsrelation)

Orgenheter som är relevanta för filtrering, uppdelade per relationstyp. Vanligt är t.ex. relationen 'en del av', där man för orgenhet X har en lista av alla orgenheter som X anses vara 'en del av'.


## 4.30 <a name="Organisationsdelsansvar">Organisationsdelsansvar</a>

Ansvar för viss orgenhet, antingen tilldelat personligen eller via en rolltilldelning.


### 4.30.1 Attribut

### 4.30.1 `typ`
Typ: [`Tagg`](Tagg)!

Ansvarstyp(er) (chef, ekonomiskt ansvarig, arbetsledare...)


### 4.30.2 `organisationsdel`
Typ: [`Organisationsdel`](Organisationsdel)

Den organisation för vilken ansvaret gäller.


### 4.30.3 `viaRolltilldelningar`
Typ: Lista av [`Rolltilldelning`](Rolltilldelning)

Rolltilldelning(ar) via vilken ansvaret tilldelats (t.ex. tilldelning av chefsroll)


### 4.30.4 `direktUtpekade`
Typ: Lista av [`Person`](Person)

Individ(er) som fått ansvaret personligen tilldelat.


## 4.31 <a name="OrganisatoriskRelation">OrganisatoriskRelation</a>

Vi har alla någon form av struktur bland våra organisationsdelar. Det är vanligt att ha flera
olika strukturer, t.ex.:

* linjeträd som representerar arbetsrättsliga ansvar
* attestträd som representerar ekonomiska beslutsvägar
* organisationsträd i Ladok som representerar beslutsvägar för examination.
* ett träd som visas ut på hemsidan.

För vissa lärosäten kanske träden är identiska, men för de flesta skiljer sig dessa träd åt. Det
är däremot långt ifrån vanligt att ha flera än två-tre av dessa dimensioner i ett IT-system.

Varje organisationsdelsrelation representerar ett riktat förhållande i något av träden som
lägger en organisationsdel "under" en annan under någon tidsperiod. Ur relationens perspektiv så
pekar den ut en "förälder" och ett "barn". Ur organisationsdelarnas perspektiv så har de `[0..*]`
relationer som pekar ut dess föräldrar i olika träd, och `[0..*]` relationer som pekar ut dess barn.


### 4.31.1 Attribut

### 4.31.1 `typer`
Typ: [`Tagg`](Tagg)!

Den/de strukturer/träd/perspektiv som denna relation gäller för.


### 4.31.2 `foralder`
Typ: [`Organisationsdel`](Organisationsdel)

Den orgenhet som är förälder/ovanför i denna relation. Andra änden av Organization.childRelations.


### 4.31.3 `barn`
Typ: [`Organisationsdel`](Organisationsdel)

Den orgenhet som är barn/under i denna relation. Andra änden av Organization.parentRelations.


## 4.32 <a name="Passerbehorighet">Passerbehorighet</a>

En passerbehörighet, identifierad av ett för mottagaren meningsfullt ID. Tilldelningen av behörigheten
görs till en person eller ett passerkort.

### 4.32.1 Attribut

### 4.32.1 `postid`
Typ: [`Identifierare`](Identifierare)!

Behörighetens ID (inte resursen behörigheten gäller för).


### 4.32.2 `resursId`
Typ: [`Identifierare`](Identifierare)!

ID på den resurs som behörigheten gäller för (inte behörighetens egna ID om ett sådant finns).


### 4.32.3 `tilldeladPersoner`
Typ: [`Person`](Person)!

De person(er) som tilldelats behörigheten.


### 4.32.4 `tilldeladPasserkort`
Typ: [`Passerkort`](Passerkort)!

De passerkort som tilldelats behörigheten.


## 4.33 <a name="Passerkort">Passerkort</a>

Ett passerkort och de behörigheter detta kort skall vara försedda med. Om behörigheter knyts till
personen snarare än till dennes kort så används istället PersonType.accessPrivileges. Notera att
giltighetstider i detta objekt rör passerkortet i sig, behörigheterna har egna giltighetstider.


### 4.33.1 Attribut

### 4.33.1 `passerbehorigheter`
Typ: Lista av [`Passerbehorighet`](Passerbehorighet)

Behörigheter som kortet skall förknippas med (behörigheter för individ läggs i Person.accessPrivileges)


## 4.34 <a name="Person">Person</a>

En person av kött och blod. Datat är så normaliserat som avsändaren klarar av - i normalfallet
motsvaras varje fysisk person av som mest _en_ datapost. Ingen avsändare skall t.ex. skicka flera
personposter med olika ID:n när en person har flera parallella anställningar.

Personobjekt innehåller vissa rena individegenskaper, t.ex. namn och diverse identifierare
(t.ex. personnummer). Kontaktinformation till personen, både i professionell och privat kontext
kan också finnas med här. Den främsta informationen framkommer dock i hur personen hänger ihop
med lärosätets organisation, vilket beskrivs av _anknytningsavtal_ och _rolltilldelningar_.


### 4.34.1 Attribut

### 4.34.1 `fornamn`
Typ: `boolean`

APERSON fornamn/efternamn Förnamn (alla)


### 4.34.2 `tilltalsnamn`
Typ: `boolean`

Tilltalsnamn. Om vi har alla namn så skickas samtliga i fornamn, och tilltalsnamnet här. Får vara ett smeknamn.


### 4.34.3 `efternamn`
Typ: `boolean`

Efternamn (inklusive eventuella mellannamn).


### 4.34.4 `formatteratNamn`
Typ: `boolean`

Färdigformatterat namn, med stora/små bokstäver (t.ex. "Stefan Ponzi von Tillman och Ovar mcPherson"


### 4.34.5 `kommunikationsvagar`
Typ: [`Kommunikation`](Kommunikation)

aperson.adress_id -> primulaadress Kommunikationsvägar till personen som individ


### 4.34.6 `passerbehorigheter`
Typ: Lista av [`Passerbehorighet`](Passerbehorighet)

Accessbehörigheter som personen skall ha, oavsett vilket passerkort hen använder.


### 4.34.7 `passerkort`
Typ: Lista av [`Passerkort`](Passerkort)

Passerkort inklusive eventuella behörigheter för kortet i sig snarare än för personen.


### 4.34.8 `anknytningsavtal`
Typ: Lista av [`Anknytningsavtal`](Anknytningsavtal)

Anknytningsavtal för denna person.


### 4.34.9 `rolltilldelningar`
Typ: Lista av [`Rolltilldelning`](Rolltilldelning)

Rolltilldelningar för denna person.


### 4.34.10 `avliden`
Typ: `boolean`


### 4.34.11 `utbildningsniva`
Typ: [`Tagg`](Tagg)

personkompetens.kompskikt_id -> kompskikt (t.ex. docent) Uppnådd utbildningsnivå (t.ex. vid rekrytering)


### 4.34.12 `docentLarosate`
Typ: `boolean`

personkompetens.kompskikt_id -> kompskikt (t.ex. docent) Är du inte docent, pojk?!


### 4.34.13 `docentAmne`
Typ: `boolean`

personkompetens.kompinriktning_id -> kompinriktning.text


### 4.34.14 `statligAnstallningFrom`
Typ: [`Date`](Date)

aperson Statlig anställning fortsätter när du byter lärosäte t.ex.


### 4.34.15 `forskningsamne`
Typ: `boolean`

aanstallning.amnestillhor -> amnestillhor.kod/text1 Forskningsämnen behöver rapporteras som ämneskoder för jämförelser mellan lärosäten. Lista på "SCB forskningsämnen" LiU använder 3 första (101 Matematik) andra alla 5.


### 4.34.16 `forskningsamneSCB`
Typ: `boolean`


### 4.34.17 `arbetsstalleID`
Typ: `integer`

aperson.arbetsstallenr_id -> arbetsstallekod Arbetsställe-ID fås från och rapporteras till SCB.


### 4.34.18 `arbetsplatsAdress`
Typ: `boolean`

aperson.arbetsstallenr_id -> arbetsstallekod Arbetsplatsadress skall rapporteras till Skatteverket kräver gatuadress eller GPS-koordinat.


### 4.34.19 `personligaAnsvar`
Typ: Lista av [`Organisationsdelsansvar`](Organisationsdelsansvar)

Personligt tilldelade ansvar.


### 4.34.20 `beraknadeAnsvar`
Typ: Lista av [`BeraknatAnsvar`](BeraknatAnsvar)

Alla ansvar denna person kan beräknas ha för andra personer.


### 4.34.21 `omfattasAvAnsvar`
Typ: Lista av [`BeraknatAnsvar`](BeraknatAnsvar)

Alla ansvar andra personer kan beräknas ha över denna person",


### 4.34.22 `bisysslor`
Typ: Lista av [`Bisyssla`](Bisyssla)

Registrerade bisysslor


## 4.35 <a name="RemunerationCode">RemunerationCode</a>



## 4.36 <a name="Roll">Roll</a>

En viss roll - en uppsättning arbetsuppgifter och ansvar t.ex. 'Studievägledare' eller 'Rektor'.
Personer kan agera i en roll (d.v.s. utföra de arbetsuppgifter som rollen beskriver), men rollen
i sig kan inte utföra något. De personer som förväntas agera i en viss roll på en viss orgenhet
har en rolltilldelning där.


### 4.36.1 Attribut

### 4.36.1 `namn`
Typ: [`SprakhanteradText`](SprakhanteradText)

Rollens namn, t.ex. {'sv': 'Studievägledare', 'en': 'Study counsellor'}


### 4.36.2 `beskrivning`
Typ: [`SprakhanteradText`](SprakhanteradText)

Beskrivning av rollen, t.ex. vilka arbetsuppgifter och ansvar som ingår i den.


### 4.36.3 `rolltilldelningar`
Typ: [`Rolltilldelning`](Rolltilldelning)

Rolltilldelningar för denna roll.


## 4.37 <a name="Rolltilldelning">Rolltilldelning</a>

En rolltilldelning säger att en person förväntas agera i en viss roll för en viss del av organisationen
under viss tid. Förhoppningsvis har personen också tilldelats möjligheten att uppfylla de ansvar som rollen
medför - eller så används Rolltilldelningen som bas för att automatiskt utdela sådana behörigheter.

Det är rekommenderat (men inte tvingande) att peka ut det anknytningsavtal inom vilket denna rolltilldelning
skett. Många personer agerar i flera olika roller på ett lärosäte i kontexten av t.ex. en anställning, och
det ger tydlighet att peka ut den kontexten. Om ett avtal pekas ut, så begränsas rolltilldelningens
giltighet både av sin egen giltighet men även av giltigheten på det utpekade anknytningsavtalet.


### 4.37.1 Attribut

### 4.37.1 `anknyntningsavtal`
Typ: [`Anknytningsavtal`](Anknytningsavtal)

Det anknytningsavtal som denna rolltilldelning detaljerar. Reverse: Anknytningsavtal.rolltilldelningar


### 4.37.2 `organisationsdel`
Typ: [`Organisationsdel`](Organisationsdel)

Den del av organisationen där personen tilldelats rollen.


### 4.37.3 `kommunikationsvagar`
Typ: [`Kommunikation`](Kommunikation)

Kommunikationsvägar till personen i kontexten av denna rolltilldelning.


### 4.37.4 `roll`
Typ: [`Roll`](Roll)

Den roll som personen tilldelas.


### 4.37.5 `onfattningsperioder`
Typ: Lista av [`Omfattningsperiod`](Omfattningsperiod)

Omfattning(ar) för denna rolltilldelning.


### 4.37.6 `lopandeErsattningsperioder`
Typ: Lista av [`LopandeErsattning`](LopandeErsattning)

Lönetillägg eller andra extra ersättningar som personen får för denna rolltilldelning. Kan vara flera, och kan variera under giltighetstiden. Lön läggs i avtalsperioden.


### 4.37.7 `engangsersattningar`
Typ: Lista av [`Engangsersattning`](Engangsersattning)

Engångsersättningar för denna rolltilldelning.


### 4.37.8 `ansvarsperioder`
Typ: Lista av [`Organisationsdelsansvar`](Organisationsdelsansvar)

De ansvar som denna rolltilldelning medför (t.ex. linjechefsansvar för en orgenhet tilldelat av en rolltilldelning som enhetschef. Andra änden av OrganizationResponsibility.deployment.


### 4.37.9 `ansvarsperioderForTilldelningen`
Typ: Lista av [`Rolltilldelningsansvar`](Rolltilldelningsansvar)

Personliga ansvar tilldelade någon annan för denna rolltilldelning (t.ex. handledarskap för en rolltilldelning som praktikant). Andra änden av DeploymentResponsibility.deployment.


### 4.37.10 `bemannarServicefunktioner`
Typ: Lista av [`Servicefunktion`](Servicefunktion)

De servicefunktioner (om några) som bemannas via denna rolltilldelning. En specifik rolltilldelning som studievägledare kan t.ex. innebära att man bemannar en studentmottagning.


## 4.38 <a name="Rolltilldelningsansvar">Rolltilldelningsansvar</a>

Ansvar för person som har viss rolltilldelning, t.ex. att vara handledare för en viss praktikant.


### 4.38.1 Attribut

### 4.38.1 `typ`
Typ: [`Tagg`](Tagg)!

Ansvarstyp(er) (arbetsledare, handledare...)


### 4.38.2 `ansvarig`
Typ: [`Person`](Person)

Den person som har ansvaret (t.ex. handledaren).


### 4.38.3 `rolltilldelning`
Typ: [`Rolltilldelning`](Rolltilldelning)

Rolltilldelningen som responsiblePerson ansvarar för (t.ex. rolltilldelningen som säger att någon är praktikant).


## 4.39 <a name="Servicefunktion">Servicefunktion</a>

En servicefunktion, t.ex. en expedition, handläggargrupp, eller annat sätt att utföra arbete som inte
direkt relaterar till en specifik rolltilldelning. Servicefunktionerna kan tillhöra en eller flera
orgenheter. Både fysiska expeditioner med besökstider och handläggargrupper i ett ärendehanteringssystem
kan representeras som servicefunktioner.


### 4.39.1 Attribut

### 4.39.1 `namn`
Typ: [`SprakhanteradText`](SprakhanteradText)!

Servicefunktionens namn, t.ex. "Datatekniska institutionens expedition".


### 4.39.2 `beskrivning`
Typ: [`SprakhanteradText`](SprakhanteradText)

En beskrivning, t.ex. "Hjälper dig att klaga på tentor och säger nej till passerkortsbehörigheter"


### 4.39.3 `kommunikationsvagar`
Typ: [`Kommunikation`](Kommunikation)

Kommunikationsvägar till servicefunktionen (inklusive eventuella besökstider).


### 4.39.4 `bemannadViaRolltilldelningar`
Typ: Lista av [`Rolltilldelning`](Rolltilldelning)

Den eller de rolltilldelningar via vilka servicefunktionen bemannas. För en studentmottagning kan man t.ex. peka ut de rolltilldelningar som studievägledare som gör att vissa personer förväntas bemanna mottagningen.


### 4.39.5 `organisationsdelar`
Typ: Lista av [`Organisationsdel`](Organisationsdel)

De organisatoriska delar för vilka denna servicefunktion tillhandahåller tjänster.


## 4.40 <a name="Skatt">Skatt</a>

Skatt(*, giltighetsperiod: top2.common.Giltighetsperiod = None, utvarderadGiltighet: top2.common.Giltighetsenum = None, SINK: float, tabell: str, kolumn: str, procskatt: float, jamkning: float, ungdomsskatt: bool)

### 4.40.1 Attribut

### 4.40.1 `SINK`
Typ: `number!`


### 4.40.2 `tabell`
Typ: `boolean!`


### 4.40.3 `kolumn`
Typ: `boolean!`


### 4.40.4 `procskatt`
Typ: `number!`


### 4.40.5 `jamkning`
Typ: `number!`


### 4.40.6 `ungdomsskatt`
Typ: `boolean!`


## 4.41 <a name="Snigelpost">Snigelpost</a>

Färdigformatterad postadress, eventuellt med kopior av vanliga filtrerings- och sorteringsvärden
i egna fält.

### 4.41.1 Attribut

### 4.41.1 `formatteradAdress`
Typ: `boolean!`

Formatterad adress, sådan den skrivs på ett kuvert som postas på svensk brevlåda.


### 4.41.2 `landskod`
Typ: `boolean`

Kopia av landskoden från formattedAddress.


### 4.41.3 `landsnamn`
Typ: `boolean`

Kopia av landsnamn från formattedAddress.


### 4.41.4 `postnummer`
Typ: `boolean`

Kopia av postnumret från formattedAddress


### 4.41.5 `postort`
Typ: `boolean`

Kopia av postort från formattedAddress.


## 4.42 <a name="SprakhanteradText">SprakhanteradText</a>



## 4.43 <a name="Spridning">Spridning</a>

Spridning(*, synlighet: top2.common.Tagg, ranking: int = None)

### 4.43.1 Attribut

### 4.43.1 `synlighet`
Typ: [`Tagg`](Tagg)!

En tag som beskriver ett sätt posten får spridas (t.ex. internt, intranät, extranät...)


### 4.43.2 `ranking`
Typ: `integer`

Om flera poster av samma typ möts i ovanstående medium (t.ex. att flera rolltilldelningar för samma person är synliga på en personsida på intranätet), så sorteras de utifrån rankingvärdet. Lägst värde vinner. Om flera objekt har samma ranking så väljer mottagaren godtyckligt.


## 4.44 <a name="Tagg">Tagg</a>

En tag - en egenskap uttryckt som en boolesk variabel med ett sant värde. Dessa definieras oftast av
lärosätet själva för att uttrycka egenskaper som 'anställningsliknande förhållande' på en person eller
'linjeorganisation' på en organisatorisk del.

Upplägget är i princip identiskt med identifierare, med utökningen att man kan skicka med en
språkhanterad text för att visa taggen för människor. "varderymden" används för att lärosätena
skall kunna skapa lokala taggar av en gemensamt överenskommen typ. Till exempel kan vi komma
överens om att ha en tagtyp "anställningsform", där Chalmers vill ha någon egen variant. Då sätter
Chalmers "chalmers.se" som värderymd på den taggen.


### 4.44.1 Attribut

### 4.44.1 `namnrymd`
Typ: `boolean!`

Namnrymd för typen, väsentligen är detta den som definierat typnamnet. Det möjliggör att t.ex. både Chalmers och GU kan ha typer som heter "person-id". Skall vara '*' om TOP definierar typen, annars något URL-liknande med minst ett domännamn för den som definierat semantiken för typen.


### 4.44.2 `typnamn`
Typ: `boolean!`

Kombinationen av (typDefinieradAv, typnamn) är en unikt definierad typ av identifierare, med semantik enligt vad typDefinieradAv bestämt.


### 4.44.3 `varde`
Typ: `boolean!`

Värde


### 4.44.4 `varderymd`
Typ: `boolean`

Domännamn eller liknande identifierare som ger en kontext för kombinationen (schemeAgencyId, schemeId, value) om samma typ+värde finns i olika kontexter (t.ex. olika instanser av samma applikation). Behöver bara användas när det finns en risk att sådana värden möts i samma mottagare. Oftast på formen "lärosäte.se/applikationsinstans"


### 4.44.5 `namn`
Typ: [`SprakhanteradText`](SprakhanteradText)

Beskrivning av taggen avsedd för mänsklig konsumtion. Inte värdebärande - varje avsändare kan egentligen lägga lite vad de vill här. Mottagaren skall _inte_ agera på .name, bara på kombinationen namnrymd/typnamn/varde/varderymd.


## 4.45 <a name="Telefonnummer">Telefonnummer</a>

Telefonnummer.

### 4.45.1 Attribut

### 4.45.1 `nummer`
Typ: `boolean!` Must match regexp: `[+][0-9]{6,}`

Universellt telefonnummer inklusive landskod, utan separerare, t.ex. +46317721000


### 4.45.2 `formatterat`
Typ: `boolean` Must match regexp: `[+]?[-0-9() ]{6,}`

Telefonnummer i visuellt format, t.ex. +46 (0)31-772 10 00


### 4.45.3 `kanTaEmotSMS`
Typ: `boolean!`

Går det att skicka SMS till detta telefonnummer? Saknat värde tolkas som 'nej'.

