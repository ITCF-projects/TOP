import datetime

from pony import orm
from pony.orm import Optional, Required

db = orm.Database()


class Identifierare(db.Entity):
    _table_ = "identifierare"

    namnrymd = orm.Required(str)
    typnamn = orm.Required(str)
    varde = orm.Required(str)
    varderymd = orm.Optional(str)

    person_postid = orm.Set("Person", reverse="postid")
    person_korrelationsidn = orm.Set("Person", reverse="korrelationsidn")
    person_sammanslagen_fran = orm.Set("Person", reverse="sammanslagen_fran")
    person_tidigare_korrelationsidn = orm.Set("Person", reverse="tidigare_korrelationsidn")


class SprakhanteradText(db.Entity):
    _table_ = "sprakhanterad_text"

    sprak = orm.Required(str)
    text = orm.Required(str)

    _tagg_namn = orm.Set("Tagg", reverse="namn")
    _besokstider_galler = orm.Set("Besokstider", reverse="galler")
    _besokstider_avvikels = orm.Set("Besokstider", reverse="avvikelse")
    _besoksadress_byggnad = orm.Set("Besoksadress", reverse="byggnad")
    _besoksadress_hitta_i_huset = orm.Set("Besoksadress", reverse="hittaIHuset")


class Tagg(db.Entity):
    _table_ = "tagg"

    namnrymd = orm.Required(str)
    typnamn = orm.Required(str)
    varde = orm.Required(str)
    varderymd = orm.Optional(str)

    namn = orm.Set(SprakhanteradText, table="Tagg_Namn")
    _giltighetsbegransade = orm.Set("GiltighetsbegransadTaggning")
    _spridning_synlighet = orm.Set("Spridning")
    _person_taggar = orm.Set("Person")
    _besokstider_taggar = orm.Set("Besokstider")
    _elektronisk_adress_taggar = orm.Set("ElektroniskAdress", reverse="taggar")
    _elektronisk_adress_media = orm.Set("ElektroniskAdress", reverse="media")
    _besoksadress_taggar = orm.Set("Besoksadress")


class GiltighetsbegransadTaggning(db.Entity):
    tagg = orm.Required(Tagg)

    # MedGiltighet
    giltighetsperiod_start = orm.Optional(datetime.datetime)
    giltighetsperiod_stop = orm.Optional(datetime.datetime)
    utvarderadGiltighet = orm.Optional(bool)

    _person_giltighetsbegransade_taggar = orm.Set("Person")
    _besokstider_giltighetsbegransade_taggar = orm.Set("Besokstider")
    _elektronisk_adress_giltighetsbegransade_taggar = orm.Set("ElektroniskAdress")
    _besoksadress_giltighetsbegransade_taggar = orm.Set("Besoksadress")


class Spridning(db.Entity):
    synlighet = orm.Required(Tagg)
    ranking = orm.Required(int)

    _telefonnummer = orm.Required("Telefonnummer")
    _snigelpost = orm.Required("Snigelpost")
    _elektronisk_adress = orm.Required("ElektroniskAdress")
    _besoksadress_spridning = orm.Set("Besoksadress")


class Telefonnummer(db.Entity):
    nummer = orm.Required(str)
    formatterat_nummer = orm.Optional(str)
    kan_ta_emot_sms = orm.Required(bool, sql_default=False)

    person_telefonnummer = orm.Set("Person", reverse="telefon")
    spridning = orm.Set(Spridning)


class Snigelpost(db.Entity):
    formatteradAdress = orm.Required(str)

    # Kopia av landskoden från formattedAddress.
    landskod = orm.Optional(str)  #, regexp="[A-Z]{2}")

    # Kopia av landsnamn från formattedAddress.
    landsnamn = orm.Optional(str)  #, regexp="[A-Z ]+")

    # Kopia av postnumret från formattedAddress
    postnummer = orm.Optional(str)  #, regexp="[-A-Z0-9 ]+")

    # Kopia av postort från formattedAddress.
    postort = orm.Optional(str)

    spridning = orm.Set(Spridning)
    personer = orm.Set("Person")


class ElektroniskAdress(db.Entity):
    """Elektronisk adress"""

    # MedSpridning
    spridning = orm.Set(Spridning)

    # MedTaggning
    taggar = orm.Set(Tagg)
    giltighetsbegransade_taggar = orm.Set(GiltighetsbegransadTaggning)

    # Media. Standarden definierar taggar för t.ex. web och epost, men det är fritt att definiera egna
    # för specifika media.
    media = orm.Set(Tagg)

    # Adressen. Utseendet beror på media. För epost är det t.ex. en epostadress, för web en URL.
    adress = orm.Optional(str)

    personer = orm.Set("Person")


class Besokstider(db.Entity):
    """En post i en lista av öppettider/besökstider."""

    # MedTaggning
    taggar = orm.Set(Tagg)
    giltighetsbegransade_taggar = orm.Set(GiltighetsbegransadTaggning)

    # Beskrivning av när tiderna gäller, t.ex. 'vardagar' eller 'påskafton'.
    galler = orm.Set(SprakhanteradText)

    # Tid på lokal klocka då besök kan börja.
    oppnar = orm.Optional(str)

    # Tid på lokal klocka då besök inte längre kan börja.
    stanger = orm.Optional(str)

    # Beskrivning som ersätter opens/closes, t.ex. "stängt".
    avvikelse = orm.Set(SprakhanteradText)

    _besoksadress = orm.Set("Besoksadress")


class Besoksadress(db.Entity):
    """Besöksadress, eventuellt med öppettider."""

    # MedSpridning
    spridning = orm.Set(Spridning)

    # MedTaggning
    taggar = orm.Set(Tagg)
    giltighetsbegransade_taggar = orm.Set(GiltighetsbegransadTaggning)

    # Gatunamn och nummer.
    gatuadress = orm.Optional(str)

    # Stad
    stad = orm.Optional(str)

    # Land (implicit om det utelämnas)
    land = orm.Optional(str)

    # Byggnadsnamn (t.ex. 'Segerstedtska huset')
    byggnad = orm.Set(SprakhanteradText)

    # Instruktioner hur man tar sig till besöksplatsen, t.ex. 'en trappa upp i vänster trapphus,
    # rum 2231 på höger sida' eller 'rum 2231 på plan 2'
    hittaIHuset = orm.Set(SprakhanteradText)

    # Besökstider.
    besokstider = orm.Set(Besokstider)

    personer = orm.Set("Person")


class Person(db.Entity):
    # MedObligatoriskIdentifierare
    postid = orm.Required(Identifierare)
    korrelationsidn = orm.Set(Identifierare, table="PersonKorrelationsidn")
    sammanslagen_fran = orm.Set(Identifierare, table="PersonSammanslagnaIdn")
    tidigare_korrelationsidn = orm.Set(Identifierare, table="PersonTidigareKorrelationsidn")

    # MedTaggning
    taggar = orm.Set(Tagg)
    giltighetsbegransade_taggar = orm.Set(GiltighetsbegransadTaggning)

    # MedGiltighet
    giltighetsperiod_start = orm.Optional(datetime.datetime)
    giltighetsperiod_stop = orm.Optional(datetime.datetime)
    utvarderadGiltighet = orm.Optional(bool)

    fornamn = orm.Optional(str)
    efternamn = orm.Optional(str)
    tilltalsnamn = orm.Optional(str)
    formatterat_namn = orm.Optional(str)

    # Kommunikation
    telefon = orm.Set(Telefonnummer)
    snigelpost = orm.Set(Snigelpost)
    elektronisk_adress = orm.Set(ElektroniskAdress)
    besoksadress = orm.Set(Besoksadress)


orm.set_sql_debug(True)
db.bind(provider="sqlite", filename=":memory:")
db.generate_mapping(create_tables=True)

@orm.db_session()
def create_p(person_id: int, accs: list[str]):
    p = Person(postid=Identifierare(namnrymd="chalmers.se", typnamn="person/nid", varde=str(person_id)),
               korrelationsidn=[
                   Identifierare(namnrymd="chalmers.se", typnamn="account_name", varde=a) for a in accs
               ], fornamn="Nisse", efternamn="Hult", formatterat_namn="Nisse Hult")
    orm.commit()

create_p(1234, ["viktor", "d2viktor"])