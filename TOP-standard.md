
# TOP - Transfer of Organizations and Persons



BETAVERSION 3, 2024-06-10



Detta dokument delas upp kapitelvis enligt följande:

[[_TOC_]]

# 1. Bakgrund och avgränsningar

Inom ATI-gruppen under samarbetsorganet ITCF finns en arbetsgrupp vars mål är att ta fram en sektorstandard för att överföra information om personal (löst definierat som "allt som inte platsar i LIS") mellan IT-system. Standarden blir en kompanjon till LIS som används för studentrelaterad information.

## 1.1 Målbild

Arbetet inleddes med att se hur vi kunde använda HROpen. Den standarden visade sig dock sakna viktiga möjligheter för bland annat internationalisering och att samma person har flera roller i olika delar av organisationen, och genom att inte direkt stödja våra usecase blev många konstruktioner repetitiva eller ointuitiva. TOP använder alla delar av HROpen som går, men utökar och stuvar om. Dessutom översatte vi begreppen till svenska, eftersom vi ändå gled så långt bort från HROpen för att stödja våra behov.

Vi har utgått från två huvudsakliga tänkta use-case: att ett lärosäte får ut sin HR-data från en HR-applikationsleverantör i ett applikationsoberoende format, och att lärosätet skickar data i samma format till en tjänsteleverantör. Vi har inte som uttryckligt use-case att lärosäten använder TOP internt, men gör samtidigt standarden avsiktligt dynamisk så att det är möjligt att göra i många olika arkitekturer om man vill det. Det går att använda TOP både in transit och at rest om man så önskar.

## 1.2 Exempel: Lilla Lärosätet

I hela standarden används ett och samma exempel. Här beskrivs detta, och eftersom informationsmodellens begrepp definieras först i nästa kapitel kommer beskrivningen här att vara lite vag för den som återvänder efter att ha tagit till sig hela standarden. Varje del av nedanstående exempel är relevant för någon del av standarden.

> _Lilla Lärosätet_ (LL) är ett ofattbart litet lärosäte. Personalen består av fyra personer, och de har två studenter. Organisationen består av en institution (Institutionen för Småskalighet) som är uppdelad en enda avdelning (Avdelningen för Smått Tänkande). Avdelningen har en professor, Patrik Socrates (men, som Patrik själv säger "det är bara min mamma som kallar mig Patrik, alla andra har i hela mitt liv kallat mig Putte.") Under Putte på avdelningen finns en lektor, Lena Lund. Man har också en administratör anställd på institutionen, han heter Adam Nistram. Han är egentligen heltidsanställd, men är föräldraledig på 40%.
>
> Givetvis har man en rektor, hon heter Hedda Master. Institutionen har en prefekt, förtroendevald på 5 år, och i ett hårt val blev det professor Putte som fick den posten. Han är därmed, enligt linjeorganisationen, chef över sig själv.
>
>Lilla Lärosätet har valt att organisera sina program i en matrisstruktur. Lena Lund fungerar som programansvarig för deras enda program, Kandidatprogram i Långsiktig Småskalighet, och programmet får en del av lärosätets pengar till sin budget. Denna budgetdel överför de till institutionen då de ger kurser som programmet vill ha.
>
>Två studenter läser på Lilla Lärosätet, Emil Studat och Emilia Fodat. Som avlastning vid tentamensrättning har avdelningen valt att anställa Emilia Fodat på timmar.
>
>Men Lilla Lärosätet har ambitioner. De har startat ett stort övergripande projekt som de kallar "Måttade Medelmedel" där de undersöker vilka medel som skulle behövas för att bli medelstora. Där har de hyrt in en projektledare, Linda Projektil, från ett konsultbolag på heltid under första halvåret 2023, och en projektdeltagare Peroja Deltacko som skall göra enstaka timmar med utredningsuppdrag.
> 
> Lilla Lärosätet har en integration till en extern applikation, ett passersystem, där alla med ett "anställningsliknande förhållande" till institutionen skall få behörighet att komma in i skalskyddet.

# 2. Informationsmodell / abstrakt datamodell

För att överföra information måste avsändare och mottagare vara överens om hur informationen är modellerad och strukturerad. Detta kapitel beskriver de olika begrepp som används och hur dessa skall förstås i lärosäteskontext. Tillsammans med schemat visar detta entydigt hur man kodar och avkodar data, och vad den betyder.

Den grundläggande datamodellen går att använda både för data i vila och för data under färd. 

Vissa entiteter i standarden är dock mest relevanta för data under färd. Ett exempel är modellen som beskriver vem som är någons chef. Rådatat till den är både chefskap och ett komplett organisatoriskt träd, tillsammans med en lokal regeluppsättning för att lösa upp sådant som att prefekter ibland skulle bli chefer över sig själva eller hur man prioriterar när någon har flera parallella anställningar.

För att en mottagare varken skall behöva känna till reglerna eller ha ett komplett organisationsträd så kan man överföra färdigberäknade relationer mellan personer, t.ex. att Hedda är chef över Putte.

## 2.1 Begrepp och modeller

### 2.1.1 Rundvandring / överblick

I huvudsak kan TOP beskrivas som ett sätt att formera information om ett lärosätes organisatoriska struktur, vilka personer som är verksamma vid lärosätet, hur personerna verkar, vilka egenskaper som kan förknippas med organisation, personer och verksamhet, samt hur allt detta varierar över tid.

Vi börjar överblicken i begreppet **organisatorisk del**, som är någon form av gruppering som är viktig för hur lärosätet organiserar en viss aspekt av sitt arbete. De flesta lärosäten har "institutioner", många har "fakulteter", som bägge är exempel på typer av organisationsdelar i linjen. Många har också organisationsdelar som representerar t.ex. forskningsprojekt eller utbildningsprogram - de delarna ligger oftast i separata organisationsträd snarare än i linjeträdet.

> Lilla Lärosätet väljer att ha organisationsdelarna 
> * Lärosätet (typ "Lärosäte", taggar "Resultatenhet" och "Linjeorganisation")
> * Institutionen för Småskalighet (typ "Institution", taggar "Resultatenhet" och "Linjeorganisation")
> * Avdelningen för Smått Tänkande (typ "Avdelning", taggar "Resultatenhet" och "Linjeorganisation")
> * Kandidatprogrammet i Långsiktig Småskalighet (typ "Program", taggat "Matrisorganisation")
> * Måttade Medelmedel (typ "Projekt", taggat "Resultatenhet") 

Organisationsdelarnas relationer struktureras med en eller flera typer av **organisationsdelsrelationer**. Dessa är typade, och den vanligaste typen är de relationer som tillsammans formar linjeträdet. Många lärosäten har andra relationstyper och andra trädstrukturer parallellt med linjeträdet. Man kan t.ex. ha ett grundutbildningsträd och ett separat träd som visas ut på hemsidan.

> Lilla Lärosätet väljer att ha ett linjeträd, och att sedan hålla ordning på att projektet "hör till" Lärosätet och programmet "hör till" institutionen. De behöver alltså ha två olika typer av orgenhetsrelationer - "linjeträdet" och "hör till"-relationen.
> * Två orgenhetrelationer av typ "Linjeträd" bildar linjeträdet: den ena säger att "Lärosätet" ligger över "Institutionen för Småskalighet", den andra säger att "Institutionen för Småskalighet" ligger över "Avdelningen för Smått Tänkande".
> * Två ytterligare relationer av typ "Hör till" knyter in de andra orgenheterna - en placerar projektet under Lärosätet, den andra placerar programmet under institutionen.
> > En visdom från Chalmers som har arbetat med denna typ av modell är dock att även om det _går_ att ha lösa relationer som t.ex. "hör till", så blir det ofta ett elände att visualisera resultatet efter tio års tillägg. Det är bättre att bestämma sig för att man har parallella träd, och att lägga in alla organisationsdelar i alla träd de hör hemma. Chalmers hade valt att ha ett linjeträd och ett separat "utökat linjeträd", där institutionerna återfinns i bägge träden, men projekten bara finns i det utökade linjeträdet.

Orgenhetsrelationerna representerar _varje enskild_ relation i en eller flera strukturer, alltså varje kant i en organisationskarta. Men ett mycket vanligt behov för en mottagare är att kunna hitta relevant data - ofta t.ex. "alla som hör till Institution X eller någon organisationsdel under den i linjeträdet". För det urvalet krävs att man har samtliga orgenheter och orgenhetsrelationer lokalt, vilket vi inte vill kräva av en mottagare. Därför har vi också begreppet **filtreringsrelation**, där man överför färdiga listor över andra orgenheter som är relevanta för filtrering.

> Eftersom Miniatyrmänniskan skall erbjuda inloggning baserat på att personer har ett visst förhållande till institutionen eller någon organisationsdel därunder i linjeträdet, så väljer Lilla Lärosätet att överföra en filtreringsrelation som de kallar "Delträd i linjen". Avdelningen är "en del av" Institutionen och "en del av" Lärosätet, vilket syns genom att bägge dessa ligger med i filtreringsrelationerna för Avdelningen. I Lilla Lärosätets egna system finns bara orgenhetsrelationerna, men man räknar ut de här filtreringsrelationerna när man skickar iväg data.

Orgenheterna kan inte av sig själva utföra nytta, för detta behövs **personer** - individer av kött och blod. Vi försöker att representera både personens egenskaper, hur de hänger fast i lärosätet och vad de förväntas utföra för nytta. 

> Lilla Lärosätet har såklart personposter för alla sina anställda: Hedda Master, Patrik Socrates, Lena Lund och Adam Nistram. Men eftersom både Linda Projektil, Peroja Deltacko och Emilia Fodat utför nytta åt lärosätet finns personposter även för dem.

Personer knyts till lärosätet genom **anknytningsavtal**, där den vanligaste varianten är ett anställningsavtal. Men även gästprofessurer, deltagande i forskningsprojekt, till och med när en professor muntligen bjuder in någon från Harvard att sprida stjärnglans över sin institution är former av sådana avtal.

> Lilla Lärosätet har anknytningsavtal för alla personer, men av olika typ. Hedda Master, Patrik Socrates, Lena Lund och Adam Nistram har alla typen "Anställd" på sina anknyntningsavtal. Eftersom Linda Projektil verkar vid lärosätet på heltid, så får hennes avtal typen "Bemanningspersonal". Peroja Deltacko som bara gör enstaka timmar får typen "Timkonsult", och Emilia Fodat får typen "Intermittent anställd" på sina respektive avtal.

Ett anknytningsavtal kan under sin löptid innefatta många olika egenskaper. Under en 25 år lång anställning (som är _ett_ avtal) kommer en person att byta lön, organisatorisk hemvist, tjänsteomfattning med mera massor av gånger. Varje sådan egenskap representeras därför av ett eller flera intervall eller _perioder_ av något slag - en egenskap med start- och eventuellt slutdatum.

Anknytningsavtalet kan ha ingen, en eller flera **ersättningsperioder** (en anställd kan t.ex. under en viss period få en viss lön), **frånvaroperioder** (t.ex. semester, sjukskrivning eller VAB), **omfattningsperioder** (t.ex. 80% tjänstgöringsgrad), **hemvistperioder** (som pekar ut den organisationsdel där personens chef normalt sett återfinns).

> På Lilla Lärosätet finns en ersättningsperiod vardera för de fyra anställda, med typen "Månadslön" - en summa och enheten "per månad". Emilia Fodat har en ersättningsperiod av typen "Timlön" med en summa och "per arbetad timme". Vilken ersättning man ger till konsulterna bedömer man inte att någon behöver veta, så dem utelämnar man ersättningsperioder för.
> 
> De fast anställda har varsinn omfattningsperiod på 100%. Adam som är föräldraledig har utöver sin omfattning på 100%, också en frånvaroperiod på 40% av typen "Föräldraledig". Linda Projektil har en omfattningsperiod på 100%, där man också noterat att den slutar siste juni när projektet skall vara klart. Varken Peroja eller Emilia har några omfattningsperioder eftersom man inte i förväg vet exakt hur mycket de skall arbeta.
> 
> Hedda Master har en hemvistperiod som pekar ut att hon organisatoriskt hör hemma på orgenheten "Lärosätet". Patrik Socrates och Adam Nistram hör hemma på institutionen och har hemvistperioder som pekar dit. Lena Lund har sin hemvist på avdelningen. Både Linda Projektil och Peroja Deltacko har projektet som orghemvist, medan Emilia Fodat har sin hemvist på institutionen.

Ett anknytningsavtal säger _hur_ personen knutits till lärosätet, men inte _vad_ personen gör där. Det är vanligt att ha en enda anställning men vara verksam på flera olika orgenheter. Både i flera olika forskningsprojekt, deltagande i centran, men även sådant som att ekonomer kan vara anställda på Ekonomiavdelningen men verka på varsinn institution.

En uppsättning arbetsuppgifter, befogenheter, förväntade beteenden, ansvar osv beskrivs av en **roll** (jämför med rollen "Hamlet" i pjäsen med samma namn). Exempel på är roller, t.ex. "rektor", "systemutvecklare" eller "registeransvarig", men lärosätena är fria att räkna nästan vad som helst som en roll. Andra, ofta aningen tvetydiga, begrepp som "titel" eller "befattning" används i delvis liknande betydelse, men de har ofta andra innebörder också. 

> På Lilla Lärosätet har man identifierat rollerna "Rektor", "Prefekt", "Professor", "Lektor", "Projektledare", "Projektdeltagare", "Administratör" och "Amanuens".

Att en person tilldelats en viss roll på en viss organisationsdel under viss period uttrycks som en **rolltilldelning**. En sådan _kan_ förnkippas med ersättningsperioder (t.ex. lönetillägg för prefekter) och omfattningsperioder (som kan vara den faktiska tid en person förväntas lägga, borträknat ledigheter med mera).

> På Lilla Lärosätet har bland annat Hedda Master en rolltilldelning med rollen "Rektor" för orgenheten "Lärosätet", och Putte Socrates har två rolltilldelningar - dels en som "Professor" för Avdelningen och dels en som "Prefekt" för Institutionen. Han tycker att det är mycket viktigare att vara prefekt än professor, och vill att prefektrollen alltid visas först, så den är flaggad som primär.
> 
> Puttes rolltilldelning som prefekt har ett slutdatum (eftersom prefektskapet är tidsbegränsat), och det är förknippat med en ersättningsperiod av typen "Lönetillägg per månad" eftersom han får extra betalt för ansvaret.
> 
> De övriga har rolltilldelningar så som man kan förvänta sig.

Lärosätena tilldelar personer vissa ansvar för vissa orgenheter. Till exempel kan en person få linjechefsansvar, ekonomiskt ansvar eller arbetsmiljöansvar för en viss organisationsdel. Detta uttrycks som **ansvarsperioder**, och dessa kan antingen peka ut en någon som personligen ansvarig, eller peka ut en rolltilldelning som innebär vissa ansvar. Linjechefsansvaret för en organisationsdel tilldelas t.ex. oftast genom att rolltilldelningen som Enhetschef.

> På Lilla Lärosätet har Hedda ett personligt förordnande som Rektor, vilket ger henne både ekonomiskt och arbetsledande ansvar för organisationsdel Lärosätet. Putte får via sin rolltilldelning som Prefekt bägge ansvaren för Institutionen. Han har också via rolltilldelningen som Professor dessa ansvar för Avdelningen. Linda Projektil har ett arbetsledande ansvar för Projektet via sin rolltilldelning som Projektledare, men Hedda Master håller i pengarna och har det ekonomiska ansvaret där.
> 
> Eftersom man inte _måste_ peka ut ansvar överallt i sina överföringar, så väljer Lilla Lärosätet att inte tala om vem som har vilket ansvar för Programmet.

Utöver att utförd nytta struktureras baserat på roller, så kan orgenheter också ha **servicefunktioner**, där den vanligaste kanske är en expedition eller en helpdesk. De bemannas via rolltilldelningar, men har t.ex. öppettider och besöksadresser som egna egenskaper. 

> Institutionen på Lilla Lärosätet har en expedition, vilket de representerar som en servicefunktion som "hör till" alla tre linjeorganisationerna.

Både för personer, rolltilldelningsperioder, orgenheter och servicefunktioner kan man definiera **kontaktvägar**, till exempel epostadresser, telefonnummer, eller besöksadresser med eller utan öppettider.

> Hedda Master har för sin rolltilldelning som Rektor en epostadress "rektor@lillalarosatet.se", och för sig själv som individ "hedda.master@lillalarosatet.se". Expeditionen har en epostadress "info@lillalarosatet", och en besöksdisk som ligger på huvudadressen i ett rum utan rumsnummer i källaren bakom en skylt "Varning för tigern". Den är öppen 9-11 på onsdagar. All denna information överför de i en kontakväg av typen "besöksadress".

Nästan alla dessa begrepp går att typa eller märka med **taggningar**. En taggning förknippar något objekt med en viss tag under viss period. Till exempel kan man utifrån intern logik avgöra vilka personer som via rolltilldelningar just nu skall betraktas som "teknisk och administrativ personal" eller "anställningsliknande personer", och överföra en sådan taggning på dem. Då behöver mottagaren inte känna till hur varje lärosäte avgör dessa egenskaper (för inget lärosäte gör som något annat), och behöver inte heller spara komplett data för att kunna räkna ut det.

> Lilla Lärosätet har valt att tagga anställningsperioderna för Hedda, Putte och Lena med "Anställningsliknande avtal". De har valt samma taggning för Linda Projektil, trots att hon formellt är anställd av konsultbolaget. Övriga har inte fått den taggningen. Denna taggning överförs till Miniatyrmänniskan, som skall ge behörighet baserat på den.
> 
> Eftersom Hedda, Putte, Lena och Linda alla har minst ett nutida anställningsavtal som är taggat med "Anställningsliknande avtal", så väljer Lilla Lärosätet också att tagga deras fyra personposter med "Anställningsliknande person". Även om de använt anställningsavtalen för att räkna ut detta, så väljer de att överföra det som en explicit taggning på personerna, så att mottagarna inte behöver veta vilka egenskaper som gör att en person räknas som "anställningsliknande". 

Som man märker är det en väldig massa perioder överallt. Det finns tre olika fält som används. Det första är giltighetsstatus, med värdena dåtida/nutida/framtida (past/present/future). Sen kan man detaljera med start- och slutdatum om man känner till dem och mottagaren har nytta av dem.

> På Lilla Lärosätet väljer man att överföra start- och slutdatum på både anknytningsavtal och hemvistperioder via integrationen till passersystemet. De beräknade behörigheterna där kan då få korrekta start- och slutdatum vilket gör det lätt att i passersystemet se när en beräknad behörighet kommer att ta slut. 

Eftersom man kan överföra dåtida perioder, så skulle "en persons löneperioder" kunna betyda "alla sen 1980-talet" för de som arbetat länge. Det är sällan användbart. Vi pratar istället om **aktuella perioder**. Det finns inget som hindrar att man överför _alla_ objekt, men det normala är att man överför de _aktuella_, och då använder man följande definitioner:
* De nutida objekten räknas alltid som aktuella.
* _Om_ man överför framtida objekt räknas även de som aktuella (givetvis märkta som framtida).
* _Om_ man överför dåtida objekt så räknas de som aktuella under 60 dagar från den dag de blev dåtida, med syfte att mottagare skall hinna reagera på att objekt byter från "nutida" till "dåtida".

### 2.1.2 Hantering av ID:n

#### 2.1.2.1 Olika ID:n

Ett ID i denna standard består alltid av tre eller fyra delar: alltid namnrymd, datatyp och värde. Om värdet inte är globalt unikt kan man också ge ett scope, eller värderymd, för värdet.

Datatyper med namn som "personnummer" finns på många ställen, men har ibland olika definition - Primula har t.ex. ett ID som de kallar "personnummer" och som i de flesta fall är ett unikt värde utgivet av svenska staten. Men Primula tillåter att man lägger in rena hittepåvärden (t.ex. "19121212KK88") i personnummerfältet, och då är just det värdet inte längre unikt mellan olika Primula-instanser (och inte längre ett personnummer enligt svenska statens definition). 

Vi måste skilja på dessa två olika saker som bägge kallas "personnummer". Det gör vi genom att ge en namnrymd för typen - är det "personnummer enligt svenska statens definition" eller är det "personnummer sådana Primula hanterar dem".

#### 2.1.2.2 Identifikation av namnrymd

Namnrymden anges normalt sett genom ett domännamn som identifierar den definierande entiteten, t.ex. "chalmers.se" eller "orcid.org". I resten av denna standard skrivs exempel-ID:n som t.ex. `chalmers.se:person-id:123123123`, men i överföringen är dessa strukturerade som tre attribut i ett objekt `{namnrymd: "chalmers.se", typnamn: "person-id", varde: "123123123"}` (se 3.1.1 för detaljer).

Syftet med att använda domännamn är att det redan finns ett register för dem, så denna standard behöver inte definiera en registerhantering. Dock finns några väldigt allmäna begrepp, t.ex. svenskt personnummer, där det kan upplevas som lite krystat att sätta domännamnet - det är formellt svenska staten som delar ut personnummer, även om det är Skatteverket som managerar det. För några sådana begrepp finns en defintion med utgivare i sektion 5.1.1. 

Om ett värde inte är globalt unikt och det finns anledning att tro att en mottagare kan få sådana värden från olika ställen, så rekommenderas att den som garanterar värdets korrekthet sätter en värderymd. Till exempel finns Primulas fält "APersonId", där samma ID kan återanvändas i olika Primulainstanser, men då representera olika personer. Där skulle man då sätta en värderymd som tillräckligt unikt definierar den instans där värdet hämtats, vilket vi i text skriver t.ex. `evry.se:APersonId:1234(chalmers.se)`. I överföringen är värderymden ett extra attribut `varderymd` i objektet.

#### 2.1.2.3 De olika ID-fälten och hur de hanteras

En avsändare fyller i ett attribut `id` med den mest stabila identifierare man känner till för det objekt som överförs. Det skall vara en identifierare som ändras så sällan som möjligt. Syftet är att mottagare enkelt skall upptäcka att de får ny data för ett objekt de tidigare fått från samma avsändare. Därför är personnummer inte ett bra sånt här id om det går att undvika - alla personer har inte ett personnummer, vissa personer har flera, och många byter personnummer under en livstid. Ett bättre val för `id` kan vara ett post-id i en lokal masterdatabas. 

För att erbjuda möjlighet för mottagaren att upptäcka att man får samma objekt från flera olika avsändare så kan avsändaren skicka över `korrelationsidn`, som är en lista av andra ID:n som man råkar känna till. På en person kan detta t.ex. vara personnummer, temporärpersonnummer från Ladok, Ladok-UID eller ORCID

Man kan inte räkna med att en viss typ av ID alltid kommer som antingen huvud-id eller korrelationsid. En avsändare som inte har något annat än personnummer använder det som huvud-id, men en avsändare som har ett annat mer stabilt id använder istället personnummer som korrelationsid.

Avsändaren kan tvingas byta ID på ett objekt. För huvud-ID:n sker det oftast när man av misstag fått dublettposter som måste slås samman, för korrelations-ID:n sker det t.ex. när någon leverantör uppströms behövt göra samma sak, eller när en person byter personnummer. Vid ID-byten överförs det gamla ID:t i `sammanslagnaIdn` eller `tidigareKorrelationsidn`. 

Ett personnummerbyte representeras t.ex. från en avsändare som skickar det som korrelationsid genom att det nya personnumret läggs i `korrelationsidn` medan det gamla personnumret under en tid överförs i `tidigareKorrelationsidn`.

### 2.1.3 Hantering av taggar

En tag är likt ett ID, men kan dessutom ha ett språkhanterat namn för mänsklig konsumtion. I standarden används konstruktionen på många ställen, både för att ange typer och för att göra allmäna taggningar. Där många standarder kanske hade valt en enum (utan möjlighet till beskrivande text), så väljer denna standard i allmänhet en tag och definierar en standarduppsättning.

Precis som ID:n används en utgivare, en datatyp och ett värde (med frivillig språkhanterad benämning). De taggar som definieras i denna standard har "*" som utgivare. Övriga har ett domännamn som identifierar utgivaren. Taggar skrivs i löptext som `<namnrymd>:<typ>:<värde>(<svensk text>/<engelsk text>)` men kodas egentligen som objekt i överföringen (se 3.1.2) där man också kan överföra fler språk än svenska och engelska om det behövs.

Tillexempel definierar standarden en tag som i löptext skrivs `*:remuneration_type:monthly_salary` (Månadslön). Den överförs som ett objekt precis som id:n.

### 2.1.4 Språkhanterad text

På många ställen är det relevant att ha språkhanterad text, t.ex. namn på organisationsdelar, benämningar på taggar och rollnamn. Standarden definierar hur man överför dessa, nämligen som en uppsättning par av språkkod och text. Det går att ange hur många språk som helst, men de flesta kommer att vara på svenska (sv) och engelska (en). Avsändare som har mängder av språk för något användningsfall uppmuntras att bara överföra de som mottagaren kan förväntas vilja ha för att hålla datamängderna nere. 

Det är _inte_ ett egensyfte att översätta alla taggar till så många språk som möjligt!

### 2.1.5 Egna utökningar

Alla avsändare är fria att göra helt egna utökningar av alla entiteter. Sådana utökningar måste vara objekt under en nyckel som är ett domännamn som identifierar den som definierat utökningen, i ett objekt under nyckeln `extensions` i det objekt som utökas:

```json5
{
  person: {
    extensions: {
      "chalmers.se": {
        "chalmers coola utökning": "It rocks!"
      }
    }
  }
}
```

Det är tillåtet att skicka vidare utökningar som någon annan definierat, om man som avsändare vet vad de betyder och vad de innehåller. Avsändare uppmuntras dock att begränsa sig till utökningar där man är säker på livscykel och semantik. Risken om man skickar vidare data i blindo är att man råkade skicka vidare något som inte fick spridas, eller som är lätt att missförstå innebörden av.

## 2.2 ER-diagram

> TODO: Nytt ER-diagram behövs!

![TOP-ER.drawio.png](TOP-ER.drawio.png)

# 3. Dataobjekt (DTO:er)

Denna standard definierar i grunden inte fasta dataobjekt (tabeller, DTO:er, klasser med mera). Istället definieras ett schema, helt utgående från informationsmodellen ovan, som entydigt beskriver hur dataobjekt formas och tolkas. I det schemat är nästan alla attribut frivilliga. Avsändare och mottagare blir överens om hur avsändaren, utifrån schemat och den information som skall överföras, formar DTO:er genom att inkludera/exkludera attribut och nästlade objekt till godtyckligt djup. En mottagare med en full implementation av denna standard kan ta emot och förstå samtliga DTO:er som formats enligt schemat.

Avsikten är att inte låsa nyttjande till specifika detaljarkitekturer. Man kan utgående från TOP och dess grundschema skapa:

* Djupt berikade Data Transfer Object (DTO) med all nuvarande och historisk info om en viss person.
* Supertunna DTO:er med bara attribut som har ändrats sedan någon tidigare överföring.
* Ett GraphQL-gränssnitt.
* Ett silverformat för en medallion architecture data lake.
* En databasmodell för lagring.

Så länge alla dessa formeras utifrån schemat så kan en uttolkare alltid veta exakt vad som kommer i varje del av objektet, och genom härledning till informationsmodellen förstå dess semantik. Det blir också trivialt att t.ex. hämta ut data via GraphQL som sedan lagras in i en silvermodell när bägge har samma grundschema.

För att göra det enklare att komma igång, så finns dock en uppsättning föreslagna objekt. Man kan följa standarden utan att använda de föreslagna objekten. Deras huvudsakliga syfte är som exempel och för att det är enklare att kravställa på en leverantör att de "levererar objekten X, Y och Z enligt kapitel 3.2 i denna standard" snarare än "ge oss lämpliga DTO:er formade enligt schemat". 

## 3.1 Gemensamma egenskaper

TODO: Uppdatera JSON-schemat!

### 3.1.1 ID:n

ID:n består som nämnts i 2.1.2 av en utgivare, en typ och ett värde. ID:n kodas i samtliga DTO:er som objekt, där `valueScope` är frivilligt:

```json5
{
  schemeAgencyId: "definierande entitet",
  schemeId: "id-typ",
  value: "värde",
  valueScope: "chalmers.se"
}
```

### 3.1.2 Taggar

Taggar formas på ett liknande sätt som ID:n (3.1.1), men man kan även överföra ett språkhanterat displaynamn.

```json5
{
  schemeAgencyId: "definierande entitet",
  schemeId: "taggens-typ",
  value: "specific tag",
  valueScope: "chalmers.se",
  name: {
    sv: "Svenskt display-name på taggen",
    en: "Engelskt display-name på taggen"
  }
}
```

### 3.1.3 Giltigheter

Giltighetstider anges på ett av två sätt: Exakta start- och sluttider tillsammans med status eller som enbart status. De kan också utelämnas helt (eftersom alla attribut är frivilliga).

Då man ger start- och sluttider så är det medvetet valt att man måste ange tidpunkt och inte nakna datum, och att fältnamnen tydligt visar huruvida sluttiden ingår i intervallet eller inte. Syftet är att undvika en mycket vanlig kategori buggar som relaterar till huruvida perioder inkluderar slutet eller inte, och hur man i så fall skall expandera datum utan tidpunkt. Om en period är inklusive slutdatum och man överför nakna datum, så måste startdatum expanderas till 00:00:00 på datumet, medan slutdatum måste expanderas till 23:59:59.999999 - något som ofta glöms bort. Genom att avsändaren skickar tidsstämplar och genom att sluttiden inte ingår i intervallet så undviks dessa buggar, och ytterligare tidsaritmetik i mottagaren blir mycket enkel.

* Med datum/tidsstämplar och status:
    ```json5
    {
      effectiveStatus: "present",
      effectiveTimePeriod: {
        validFrom: "2023-01-10T10:00:00",
        invalidFrom: "2024-01-01T00:00:00"
      }
    }
    ```

* Bara status nutida/dåtida/framtida.
    ```json5
    {
      effectiveStatus: "present",
    }
    ```

En helt utelämnad giltighetstid säger egentligen ingenting om giltighet, men kan såklart förstås som en utfästelse att objektet var giltigt precis då det formades (annars skulle det _förmodligen_ inte varit med i överföringen).

### 3.1.4 Lokala utökningar

Lokala utökningar får göras av alla entiteter. De görs genom att definiera nyckeln `extensions` som ett objekt, där man under sitt domännamn läger ett objekt som håller utökningarna. Man får lov att hantera och skicka vidare utökningar som definierats av andra, om man vet vad de betyder, känner till deras livscykel, och vet att man får lov att hantera/skicka vidare dem.

```json5
{
  extensions: {
    "chalmers.se": {
      ...
    },
    "gu.se": {
      ...
    }
  }
}
```

### 3.1.5 Referenser

Om man väljer att i en DTO som representerar en person överföra en referens till de deployments som gäller för personen, så ser det som ett minimum ut såhär:

```json5
{
  person: {
    deployments: [
      {"id": "123123123131"},
      {"id": "283746923874"}
    ]
  }
}
```

Om man sedan väljer att utöka denna DTO så att man även tar med en referens till organisationen för varje deployment:

```json5
{
  person: {
    deployments: [
      {
        id: "123123123131",
        organization: {id: "jh387hgwefhjsdhh"}
      },
      {
        id: "283746923874",
        organization: {id: "jh387hgwefhjsdhh"}
      }
    ]
  }
}
```

De refererade objekten är alltså helt enkelt nästlade objekt där man bara skickar ett ID.


### 3.3.2 Exempel på tjocka objekt

Schemat tillåter oändligt många kombinationer av attribut och nästlade objekt. De objekt som beskrivs här är för dem som vill ha så få DTO:er som möjligt, som innehåller så mycket data per styck som möjligt.

# 4. Ändpunkter

## 4.1 Asynkrona ändpunkter

Asynkrona ändpunkter förväntas kunna producera meddelanden innehållande objekt som uppfyller denna standard. Den viktigaste regeln för deras beteende är: 

> Asynkrona ändpunkter _skall_ producera ett nytt meddelande så snart data i ett tidigare meddelande ändrats, men _får_ producera meddelanden även om ingen data ändrats. 

Regeln omfattar all data i meddelandet. Om t.ex. ett personobjekts rolltilldelningar innehåller svenskt namn på en organisationsdel, så måste det personobjektet sändas om när orgenheten byter svenskt namn eftersom dess data inte längre är korrekt.

Den som tar emot meddelanden av någon viss typ skall alltså med säkerhet veta att det den senast tagit emot är korrekt i sin helhet tills dess den tar emot ett nytt meddelande för samma id, och att om någon del av innehållet ändras så kommer den att få ett nytt meddelande.

Syftet med denna regel är att göra alla former av cache hos mottagaren enkel att upprätthålla.

### 4.1.1 Att upptäcka vad som ändrats

Preliminärt: Standarden definierar en plats i toppobjektet där en lista av JSON Pointer (RFC 6901) kan placeras som talar om vilken del av objektet som ändrats sedan förra spridningen. Många lärosäten har redan motsvarande information i sin metadata runt meddelanden, och de kan tolka dessa JSON Pointers för att skapa denna metadata alternativt använda sin metadata för att producera sådana JSON Pointers.

## 4.2 Synkrona ändpunkter med statiska DTO:er

De synkrona ändpunkterna förväntas producera en lista av objekt utifrån vissa urvalsvillkor, sådana de såg ut vid någon viss tidpunkt.

Avsändare som har både synkrona och asynkrona ändpunkter uppmuntras att designa så att de asynkrona DTO:erna är äkta delmängder av de synkrona. Målet med denna design är att den som vill kunna fullsynka/verifiera/initiera en cache har möjlighet att hämta objekt synkront, och sedan uppdatera dem asynkront.

### 4.2.1 Stora datamängder

Avsändaren måste garantera att även mycket stora datamängder levereras på ett sätt som bibehåller intern datakonsistens. Det får alltså inte vara så att ändringar som sker under tiden överföringen görs leder till att olika delar av datamängden representerar olika intern state.

En väldefinierad pagineringslösning som är stabil för dataförändringar mellan sidor är ett exempel på en sådan lösning.

# 5. Definierade ID-typer och taggar

Alla ID-typer och taggar definieras här med sin korta form. Följande är den faktiska kodningen av personnummer:

```json5
{
  schemeAgencyId: "*",
  schemeId: "personnummer",
  value: "191212121212"
}
```

Detta skrivs i definitionerna nedan som `*:personnummer:YYYYMMDDNNNN`.

Taggen för att tala om att en person har en formell anställning på lärosätet överförs såhär:

```json5
{
  schemeAgencyId: "*",
  schemeId: "personType",
  value: "employee",
  name: {
      "sv": "Anställd",
      "en": "Employee"
  }
}
```

## 5.1 Definierade ID-typer och taggar

Alla ID:n och taggar är en kombination av en utgivare, en typ och ett värde. Utgivaren är den som delar ut värdet. Alla producenter är därmed fria att definiera sina egna id-typer och taggar genom att använda sitt eget domännamn som utgivare. 

Alla lärosäten som använder Primula kommer att ha "Primulapersonnummer" på personer. Men varje sådant värde kommer att vara olika per lärosäte, och utgivaren måste vara respektive lärosäte - inte "primula". För att undvika krockar uppmuntras alla att använda så specifika namn som möjligt på attributen. I en framtid kan vi eventuellt införa ett "definierande entitet" utöver den som givit ut värdet.

Vissa gemensamma ID:n och begrepp har vi dock stor nytta av att alla uttrycker på samma sätt, och dessa definieras nedan.

### 5.1.1 ID-typer

TODO: Detta måste definieras!

* `*:personnummer:YYYYMMDDNNNN` - officiellt svenskt personnummer eller samordningsnummer, utdelat av svenska staten (via Skatteverket).
* `orcid.org:orcid:<orcid>` - personens ORCID, utdelat av orcid.org.
* `ladok.se:ExterntStudentUID:<nnn>` - ett externt student-uid utdelat av Ladok.
* `<lärosäte>:PrimulaAPersonId:<nnn>` - APerson.id från lärosätets primulainstans.

# 6. Appendix

## 6.1 Relationen mellan denna standard och HROpen

HROpen är en amerikansk "internationell" standard för att överföra HR-information. 

Den är i vissa områden mycket detaljerad, t.ex. finns inte mindre än 15 olika attribut för att överföra en persons namn (trots det kan man inte representera en person med två efternamn), men i andra områden ganska vag. Till exempel saknas möjlighet att representera en organisatorisk struktur, och det är omöjligt att representera att nytta utförs av personer som inte är antingen anställda eller bemanningspersonal.

Fokus för HROpen är på HR-sysslor där överföring mellan olika organisationer ofta krävs, t.ex. lediga tjänster, en persons CV, ersättningspaket, utvärderingar av kandidater och anställda, tidsrapportering och så vidare. Fokus är också tydligt på anställda personer, inte icke anställa uppdragstagare, gäster m.fl.

### 6.1.1 Vårt use-case

Det vi vill överföra är:
* Organisatoriska enheter inom lärosätet
* Förhållanden mellan organisatoriska enheter ("organisationsträd")
* Information om personer (inklusive t.ex. datorkonton och epostadresser)
* Förhållanden mellan personer och organisatoriska enheter (uppdrag, anställningsförhållanden 
  etc.)

### 6.1.2 Interoperabilitetsmål

Vi vill garantera en interoperabilitet, där vi kan vara rimligt säkra på att om två parter bägge implementerar standarden, så kan de därefter utbyta informationen som ryms inom vårt use-case. HROpen har en uppsättning applicerbara attribut, men för vårt use-case har standarden både otillräckligt omfång och otillräcklig tydlighet (detaljer nedan). 

Som ett exempel, så har vi inom vårt use-case behov av att kunna överföra att en viss person är emeritus. Med lite kreativitet skulle man kunna klämma in det i några standardattribut i HROpen, men någon naturlig plats finns inte. Två parter som bägge implementerar HROpen kan därför vara oförmögna att utbyta denna information om de valt olika sätt att representera informationen, trots att bägge följer HROpen.

Oavsett hur mycket av HROpen vi använder, så kommer vår standard att behöva nämna fler specifika detaljer än HROpen gör, så vi kommer i alla lägen att behöva göra en egen standard.

### 6.1.3 Från verkligheten

Eftersom HROpen inte stödjer det vi behöver fullt ut, så måste man välja väg. Antingen tänjer vi på HROpen genom att införa nya attribut, eller så tänjer vi på vår användning genom att lägga data i befintliga attribut även om det är fel attribut enligt HROpens definitioner.

Ett lärosäte (GU) har idag ett internt format som till vissa delar faller inom vårt use-case, och som är baserat på HROpen. De har valt att använda HROpens attribut men tänja på definitionerna. Till exempel används attributet `securityCredentials` för att överföra datorkonto, men HROpen definierar dess användning som SÄPO-klassningar. Rolltilldelningar överförs på liknande sätt i attributet `affiliations`, som HROpen definerar som platsen att överföra medlemskap i fackföreningar och intresseorganisationer.

Fördelen med den lösningen är att man inte behöver skriva en egen standard och ett eget schema. Namnet `affiliations` är också bekant, även om den bekanta betydelsen inte alls är samma som HROpen:s betydelse. Eftersom ingen _annan_ implementation av HROpen kommer att varken skicka eller ta emot data på det sättet, så mister man all interoperabilitet. Men som helt lärosätesinternt format är det såklart oproblematiskt.

I TOP valde vi istället initialt att definiera egna attribut där det behövs, men använda allt applicerbart som HROpen definierar enligt ursprungsdefinition. Eftersom vi insåg att ingen befintlig HROpen-adapter kommer att finnas för TOP, och eftersom det tog mer tid att översätta alla besvärliga begrepp till engelska, så valde vi till sist att översätta hela standarden till svenska.
Det kommer dock fortfarande att vara enklare att anpassa en befintlig HROpen-adapter än att skriva en helt ny om man har use-case som ligger nära det HROpen trots allt klarade av.

