# Person

## Id-typer

* `*:personummer`
* `*:norEduPersonLIN` (valueScope: liu.se)
* `*:norEduPersonLIN` (valueScope: liu.se/student)
* `*:norEduPersonLIN` (valueScope: liu.se/staff)
* `*:eduPersonPrincipalName` (valueScope: liu.se/student)
* `*:eduPersonPrincipalName` (valueScope: liu.se/staff)

## Utbildningsnivå

Någon form av standardvärden...

```
Person {
    Xutbildningsniva: Tag  # Av typ *:utbildningsniva
    XdocentLarosate: str
    XdocentAmne: str
    Xdocent: bool
}

Tag för utbildningsnivå:

*:utbildningsniva:ingenGymnasial
*:utbildningsniva:gymnasialHogstTva
*:utbildningsniva:gymnasialTre
*:utbildningsniva:eftergymnasialMindreAnTre
*:utbildningsniva:eftergymnasialTreArEllerMer
*:utbildningsniva:forskarutbildning

```

## Misc

* X`statligAnstallningFrom`
* X`forskningsamneSCB: str  # Ämneskoder för jämförelser`
* X`arbetsstalleID: int  # Arbetsställe-id som fås från SCB`
* X`arbetsplatsAdress: str  # Skatteverket kräver gatuadress eller GPS-koordinat`

# Avtal

```
WorkLifeCycle {
    Xbegransningskod: str
    Xhuvudavtal: bool  # Om du måste välja _ett_ av nån anledning, ta det här.
    XunderordnatAnnatAvtal: WorkLifeCycle  # Om det andra tagit slut så är detta inte giltigt oavsett slutdatum
    Xavslutsorsak: str  
    Xavslutsorsakskoder: list[Tag]  # S1-S9 till pensionsmyndigheten för anställningar
}

WorkLifeCycleDetails {  # med from/tom
    Xanstallningsnummer: int
    Xbefattningsnamn: str  # Kan vara samma eller annan som roll
    Xbefattningskategori: str
    XbefattningskodSCB: str
    XBESTA: str
}
```



## Skatt

Skatten ligger på anställning sedan 1 jan 2025, så det kopplar till `WorkLifeCycle` (personer som jobbar både i hemlandet och här har t.ex. parallella anställningar med olika skatteregler).

``````
Skatt {
    XSINK: float
    Xtabell: str  # Tre siffror
    Xkolumn: str  # En siffra
    Xjamkning: float
    Xungdomsskatt: float
}
``````

SINK (särskild inkomstskatt för begåvade typer) (%), tabell (sträng-id), %-skatt (jämkning), ungdomsskatt (%).

# Rolltilldelning

* (Få befattningar är bra vid t.ex. uppsägningar.)

```
Deployment {
}
```



# Hemvistperiod

LiU:s fakulteter är matris där tilldelningen baseras på forskningsämne.

# Lönehändelser

Det mesta blir en lönehändelse, t.ex. sjukskrivning, lönetillägg... Vi skall förmodligen konvertera många av dessa till andra typer av perioder.

* Larttyp t.ex. (INTR) "intresse", (ARV) "arvode" eller "lönetillägg", (LED) "ledighet".
* Lartkoderna är individuella per lärosäte.
* Vi behöver gå på lartkoder eller range av lartkoder för att konvertera. Yay...

Tidsanvändningsstatistiken (skall till arbetsgivarverket) https://www.arbetsgivarverket.se/globalassets/arbetsgivarverket/statistik-och-analys/aterrapportering-av-tidsanvandningsstatistik-forklaringar-tabell-1-8.pdf sammanställer alla dessa till koder. Det kan gå att använda detta för att skapa frånvaroperioder med mera. I en fortsättning skulle man kunna skapa utifrån framåtrapporterad frånvaro.

* Sammanställt per månad. Fasta koder K01 (jobbade timmar), K90 (månadslön),  osv. 
* Man skulle vilja generera detta även framåt

# Bisysslor

From, tom, beskrivning, företag, orgnr, fortsätter (<1 år, 2-3 år, tillsvidare)?

```
IncidentalEmployment {
    organizationName: str
    registrationNumber: str
    expectedToContinue: str  # t.ex. "<1 år"
}
```



LiU-extensions? Tidsåtgång, omsättning, inkomst, relation till LiU...

(primula kan avarter som är vanliga, typ semester mitt i en tjänsteresa eller lärarnas semester som läggs ut utan datum)

# Primula

Roller kan vara t.ex. "avdelningschef" och flöden kan konfigureras "skicka till avdelningschef".

