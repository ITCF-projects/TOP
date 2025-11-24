from dataclasses import dataclass
from typing import *

from top2.common import Tagg, SprakhanteradText, MedTaggning, MedSpridning, MedLokalUtokning
from schemagen import jsontype, Regexp


@jsontype()
@dataclass(kw_only=True)
class Telefonnummer(MedSpridning, MedTaggning, MedLokalUtokning):
    """Telefonnummer."""

    # Universellt telefonnummer inklusive landskod, utan separerare, t.ex. +46317721000
    nummer: Annotated[str, Regexp("[+][0-9]{6,}")]

    # Telefonnummer i visuellt format, t.ex. +46 (0)31-772 10 00
    formatterat: Annotated[str, Regexp("[+]?[-0-9() ]{6,}")] = None

    # Går det att skicka SMS till detta telefonnummer? Saknat värde tolkas som 'nej'.
    kanTaEmotSMS: bool = False


@jsontype()
@dataclass(kw_only=True)
class Snigelpost(MedSpridning, MedTaggning, MedLokalUtokning):
    """Färdigformatterad postadress, eventuellt med kopior av vanliga filtrerings- och sorteringsvärden
    i egna fält."""

    # Formatterad adress, sådan den skrivs på ett kuvert som postas på svensk brevlåda.
    formatteradAdress: list[str]

    # Kopia av landskoden från formattedAddress.
    landskod: str = None  # regexp="[A-Z]{2}"

    # Kopia av landsnamn från formattedAddress.
    landsnamn: str = None  # regexp="[A-Z ]+"

    # Kopia av postnumret från formattedAddress
    postnummer: str = None  # regexp="[-A-Z0-9 ]+")

    # Kopia av postort från formattedAddress.
    postort: str = None


@jsontype()
@dataclass(kw_only=True)
class ElektroniskAdress(MedSpridning, MedTaggning, MedLokalUtokning):
    """Elektronisk adress"""

    # Media. Standarden definierar taggar för t.ex. web och epost, men det är fritt att definiera egna
    # för specifika media.
    media: Tagg

    # Adressen. Utseendet beror på media. För epost är det t.ex. en epostadress, för web en URL.
    adress: str


@jsontype()
@dataclass(kw_only=True)
class Besokstider(MedTaggning, MedLokalUtokning):
    """En post i en lista av öppettider/besökstider."""

    # Beskrivning av när tiderna gäller, t.ex. 'vardagar' eller 'påskafton'.
    galler: SprakhanteradText

    # Tid på lokal klocka då besök kan börja.
    oppnar: str = None  # regexp="[0-9]{2}:[0-9]{2}

    # Tid på lokal klocka då besök inte längre kan börja.
    stanger: str = None  # regexp="[0-9]{2}:[0-9]{2}

    # Beskrivning som ersätter opens/closes, t.ex. "stängt".
    avvikelse: SprakhanteradText = None


@jsontype()
@dataclass(kw_only=True)
class Besoksadress(MedSpridning, MedTaggning, MedLokalUtokning):
    """Besöksadress, eventuellt med öppettider."""

    # Gatunamn och nummer.
    gatuadress: str

    # Stad
    stad: str

    # Land (implicit om det utelämnas)
    land: str = None

    # Byggnadsnamn (t.ex. 'Segerstedtska huset')
    byggnad: SprakhanteradText = None

    # Instruktioner hur man tar sig till besöksplatsen, t.ex. 'en trappa upp i vänster trapphus,
    # rum 2231 på höger sida' eller 'rum 2231 på plan 2'
    hittaIHuset: SprakhanteradText = None

    # Besökstider.
    besokstider: list[Besokstider]


@jsontype()
@dataclass(kw_only=True)
class Kommunikation(MedLokalUtokning):
    """Ett kommunikationsvägar-objekt innehåller upp till fyra listor av adresser/kontaktinformation
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
    """
    telefon: list[Telefonnummer] = None
    snigelpost: list[Snigelpost] = None
    elektronisk: list[ElektroniskAdress] = None
    besok: list[Besoksadress] = None

