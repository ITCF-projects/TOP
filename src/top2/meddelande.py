import dataclasses

from schemagen import jsontype

from top2.rolltilldelning import Rolltilldelning
from top2.roll import Roll
from top2.organisationsdel import Organisationsdel
from top2.person import Person, Passerkort, Passerbehorighet
from top2.anknytningsperiod import Anknytningsperiod


@jsontype()
@dataclasses.dataclass(kw_only=True)
class Meddelande:
    """Toppobjekt med enkla och listvärda referenser till samtliga värdeobjekt. Bra grund för meddelanden!"""

    anknytningsperiod: Anknytningsperiod = None
    anknytningsperioder: list[Anknytningsperiod] = None
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
