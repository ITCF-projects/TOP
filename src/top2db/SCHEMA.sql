
-- common.py

CREATE TABLE IF NOT EXISTS IF NOT EXISTS sprakhanteradText (
    dbid INTEGER PRIMARY KEY AUTOINCREMENT,
    sprak TEXT NOT NULL,
    innehall TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tagg (
    dbid INTEGER PRIMARY KEY AUTOINCREMENT,
    namnrymd text not null,
    typnamn text not null,
    displayNameSv text,
    displayNameEn text,
    varderymd text
);

CREATE TABLE IF NOT EXISTS identifierare (
    dbid INTEGER PRIMARY KEY AUTOINCREMENT,
    namnrymd text not null,
    typnamn text not null,
    varde text not null,
    varderymd text
);

CREATE TABLE IF NOT EXISTS person (
    -- MedObligatoriskIdentifierare
    postid INTEGER FOREIGN KEY REFERENCES identifierare,

    fornamn TEXT,
    tilltalsnamn TEXT,
    efternamn TEXT,
    formatteratNamn TEXT,

    avliden INTEGER DEFAULT 0,

    utbildningsniva INTEGER FOREIGN KEY REFERENCES tagg,
    docentVid TEXT,
    docentAmne TEXT,

    statligAnstallningFrom TEXT,
    forskningsamne TEXT,
    forskningsamneSCB TEXT,

    arbetsstalleID INTEGER,
    arbetsplatsAdress TEXT
);

-- Person(MedObligatoriskIdentifierare)
CREATE TABLE IF NOT EXISTS person_korrelationsid (
    person INTEGER FOREIGN KEY REFERENCES person,
    extid INTEGER FOREIGN KEY REFERENCES identifierare
);

-- Perosn(MedObligatoriskIdentifierare)
CREATE TABLE IF NOT EXISTS person_sammaslaget_id (
    person INTEGER FOREIGN KEY REFERENCES person,
    extid INTEGER FOREIGN KEY REFERENCES identifierare
);

-- Person(MedObligatoriskIdentifierare)
CREATE TABLE IF NOT EXISTS person_tidigare_korrelationsid (
    person INTEGER FOREIGN KEY REFERENCES person,
    extid INTEGER FOREIGN KEY REFERENCES identifierare
);

-- Person(MedTaggning.taggar)
CREATE TABLE IF NOT EXISTS person_taggar (
    person INTEGER FOREIGN KEY REFERENCES person,
    tagg INTEGER FOREIGN KEY REFERENCES tagg
);

-- Person(MedTaggning.giltighetsbegransadeTaggar)
CREATE TABLE IF NOT EXISTS person_giltighetsbegransade_taggar (
    person INTEGER FOREIGN KEY REFERENCES person,
    tagg INTEGER FOREIGN KEY REFERENCES tagg,
    -- MedGiltighet
    giltig_from TEXT,
    ogiltig_from TEXT,
    giltighet TEXT
);

-- Person(MedGiltighet)
CREATE TABLE IF NOT EXISTS person_giltighet (
    person INTEGER FOREIGN KEY REFERENCES person,
    giltig_from TEXT,
    ogiltig_from TEXT,
    giltighet TEXT
);

-- Person.kommunikationsvagar.telefonnummer
CREATE TABLE IF NOT EXISTS person_kommunikationsvagar_telefonnummer (
    person INTEGER FOREIGN KEY REFERENCES person,
    nummer TEXT NOT NULL,
    formatterat TEXT,
    kan_ta_emot_sms INTEGER NOT NULL DEFAULT 0
);

-- Person.kommunikationsvagar.snigelpost
CREATE TABLE IF NOT EXISTS person_kommunikationsvagar_snigelpost (
    person INTEGER FOREIGN KEY REFERENCES person,
    formatterad_adress TEXT NOT NULL,
    landskod TEXT,
    landsnamn TEXT,
    postnummer TEXT,
    postort TEXT
);

-- Person.kommunikationsvagar.elektronisk
CREATE TABLE IF NOT EXISTS person_kommunikationsvagar_elektronisk (
    person INTEGER FOREIGN KEY REFERENCES person,
    media INTEGER FOREIGN KEY REFERENCES tagg NOT NULL,
    adress TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS passerbehorighet (
    dbid INTEGER PRIMARY KEY AUTOINCREMENT,
    postid INTEGER FOREIGN KEY REFERENCES identifierare,
    resurs_id INTEGER FOREIGN KEY REFERENCES identifierare,
    -- MedGiltighet
    giltig_from TEXT,
    ogiltig_from TEXT,
    giltighet TEXT
);

CREATE TABLE IF NOT EXISTS passerbehorighet_korrelationsid (
    passerbehorighet INTEGER FOREIGN KEY REFERENCES passerbehorighet,
    identifierare INTEGER FOREIGN KEY REFERENCES identifierare
);

CREATE TABLE IF NOT EXISTS passerbehorighet_sammanslaget_id (
    passerbehorighet INTEGER FOREIGN KEY REFERENCES passerbehorighet,
    identifierare INTEGER FOREIGN KEY REFERENCES identifierare
);

CREATE TABLE IF NOT EXISTS passerbehorighet_tidigare_korrelationsid (
    passerbehorighet INTEGER FOREIGN KEY REFERENCES passerbehorighet,
    identifierare INTEGER FOREIGN KEY REFERENCES identifierare
);

CREATE TABLE IF NOT EXISTS person_passerbehorighet (
    person INTEGER FOREIGN KEY REFERENCES person,
    passerbehorighet INTEGER FOREIGN KEY REFERENCES passerbehorighet
);

CREATE TABLE IF NOT EXISTS passerkort (
    dbid INTEGER PRIMARY KEY AUTOINCREMENT,
    postid INTEGER FOREIGN KEY REFERENCES identifierare,
    resurs_id INTEGER FOREIGN KEY REFERENCES identifierare,
    -- MedGiltighet
    giltig_from TEXT,
    ogiltig_from TEXT,
    giltighet TEXT
);

CREATE TABLE IF NOT EXISTS passerkort_passerbehorighet (
    passerkort INTEGER FOREIGN KEY REFERENCES passerkort,
    passerbehorighet INTEGER FOREIGN KEY REFERENCES passerbehorighet
);


