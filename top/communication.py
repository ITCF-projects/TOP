from dataclasses import dataclass
from typing import *

from top.common import Tag, I18nText, TagsMixin, VisibilityConfigurationMixin, Regexp


@dataclass(kw_only=True)
class Phone:
    """Telefonnummer."""
    number: Annotated[
        str, "Universellt telefonnummer inklusive landskod, utan separerare, t.ex. +46317721000", Regexp("\+[0-9]{6,}")]
    formattedNumber: Annotated[
        str, "Telefonnummer i visuellt format, t.ex. +46 (0)31-772 10 00", Regexp("\+?[-0-9() ]{6,}")] = None
    textable: Annotated[bool, "Går det att skicka SMS till detta telefonnummer? Saknat värde tolkas som 'nej'."] = False


@dataclass(kw_only=True)
class Address(VisibilityConfigurationMixin, TagsMixin):
    """Postadress"""

    # Formatterad adress, sådan den skrivs på ett kuvert som postas på svensk brevlåda.
    formattedAddress: list[str]

    # Kopia av landskoden från formattedAddress.
    countryCode: str = None  # regexp="[A-Z]{2}"

    # Kopia av landsnamn från formattedAddress.
    countryName: str = None  # regexp="[A-Z ]+"

    # Kopia av postnumret från formattedAddress
    postalCode: str = None  # regexp="[-A-Z0-9 ]+")

    # Kopia av postort från formattedAddress.
    city: str = None


@dataclass(kw_only=True)
class ElectronicAddress(VisibilityConfigurationMixin, TagsMixin):
    """Elektronisk adress"""

    # Media. Standarden definierar taggar för t.ex. web och epost, men det är fritt att definiera egna
    # för specifika media.
    media: Tag

    # Adressen. Utseendet beror på media. För epost är det t.ex. en epostadress, för web en URL.
    address: str


@dataclass(kw_only=True)
class VisitingHours:
    """En post i en lista av öppettider/besökstider."""

    # Beskrivning, t.ex. 'vardagar' eller 'påskafton'.
    description: I18nText

    # Tid på lokal klocka då besök kan börja.
    opens: str = None  # regexp="[0-9]{2}:[0-9]{2}

    # Tid på lokal klocka då besök inte längre kan börja.
    closes: str = None  # regexp="[0-9]{2}:[0-9]{2}

    # Annan beskrivning, t.ex. "stängt"
    other: I18nText = None


@dataclass(kw_only=True)
class VisitAddress(VisibilityConfigurationMixin, TagsMixin):
    """Besöksadress"""

    # Gatunamn och nummer.
    street: str

    # Stad
    city: str

    # Land (implicit om det utelämnas)
    country: str = None

    # Byggnadsnamn (t.ex. 'Segerstedtska huset')
    building: I18nText = None

    # Instruktioner hur man tar sig till besöksplatsen, t.ex. 'en trappa upp i vänster trapphus,
    # rum 2231 på höger sida' eller 'rum 2231 på plan 2'
    instructions: I18nText = None

    # Besökstider.
    visitingHours: list[VisitingHours]


@dataclass(kw_only=True)
class Communication:
    """Kommunikationsvägar till någon entitet. Minst ett av attributen måste ha ett värde som inte
    är en tom lista."""
    phone: list[Phone] = None
    address: list[Address] = None
    electronic: list[ElectronicAddress] = None
    visit: list[VisitAddress] = None
