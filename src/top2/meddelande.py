import dataclasses

from schemagen import jsontype
from top2 import LokalUtokning

from top2.rolltilldelning import Rolltilldelning
from top2.roll import Roll
from top2.organisationsdel import Organisationsdel
from top2.person import Person, Passerkort, Passerbehorighet
from top2.anknytningsavtal import Anknytningsavtal
from top2.common import Tagg


@jsontype()
@dataclasses.dataclass(kw_only=True)
class Meddelande:
    """Toppobjekt med enkla och listvärda referenser till samtliga värdeobjekt. Bra grund för meddelanden,
    även t.ex. en lysande topp-Query för ett GraphQL-gränssnitt, eller datatyp för JSON-filer med datadumpar
    i.
    """

    anknytningsperiod: Anknytningsavtal = None
    anknytningsperioder: list[Anknytningsavtal] = None

    # Avsändaren förmedlar en uppsättning definierade taggar. Möjliggör att t.ex. bara skicka "namn" en gång,
    # därefter endast skicka namnrymd/typnamn/varde/varderymd, eller att utbyta taggar för att hitta
    # gemensamma subset.
    definieradeTaggar: list[Tagg] = None

    organisationsdel: Organisationsdel = None
    organisationsdelar: list[Organisationsdel] = None

    passerkort: Passerkort = None
    passerkortslista: list[Passerkort] = None

    passerbehorighet: Passerbehorighet = None
    passerbehorigheter: list[Passerbehorighet] = None

    person: Person = None
    personer: list[Person] = None

    roll: Roll = None
    roller: list[Roll] = None

    rolltilldelning: Rolltilldelning = None
    rolltilldelningar: list[Rolltilldelning] = None

    lokalUtokning: LokalUtokning = None
