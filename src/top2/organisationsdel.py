from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Tagg, SprakhanteradText, MedTaggning, MedFrivilligIdentifierare, MedObligatoriskIdentifierare, MedGiltighet, MedLokalUtokning

if TYPE_CHECKING:
    from top2.rolltilldelning import Rolltilldelning
    from top2.kommunikation import Kommunikation
    from top2.ansvar import Organisationsdelsansvar
    from top2.anknytningsperiod import Hemvistperiod


@jsontype()
@dataclass(kw_only=True)
class Servicefunktion(MedFrivilligIdentifierare, MedGiltighet, MedTaggning, MedLokalUtokning):
    """En servicefunktion, t.ex. en expedition, handläggargrupp, eller annat sätt att utföra arbete som inte
    direkt relaterar till en specifik rolltilldelning. Servicefunktionerna kan tillhöra en eller flera
    orgenheter. Både fysiska expeditioner med besökstider och handläggargrupper i ett ärendehanteringssystem
    kan representeras som servicefunktioner.
    """

    # Servicefunktionens namn, t.ex. "Datatekniska institutionens expedition".
    namn: SprakhanteradText

    # En beskrivning, t.ex. "Hjälper dig att klaga på tentor och säger nej till passerkortsbehörigheter"
    beskrivning: SprakhanteradText = None

    # Kommunikationsvägar till servicefunktionen (inklusive eventuella besökstider).
    kommunikationsvagar: "Kommunikation" = None

    # Den eller de rolltilldelningar via vilka servicefunktionen bemannas. För en studentmottagning kan man
    # t.ex. peka ut de rolltilldelningar som studievägledare som gör att vissa personer förväntas bemanna
    # mottagningen.
    bemannadViaRolltilldelningar: "list[Rolltilldelning]" = None

    # De organisatoriska delar för vilka denna servicefunktion tillhandahåller tjänster.
    organisationsdelar: "list[Organisationsdel]" = None


@jsontype()
@dataclass(kw_only=True)
class Kontextualiseradorganisationsdelsrelation:
    """En kontextualiserad relation med en orgenhet. Används i Organization.filterRelations. Taggen kan
    t.ex. representera filterkontexten "en del av", och peka ut alla orgenheter som en viss orgenhet
    kan anses vara "en del av".
    """
    # Den struktur där relationen gäller.
    type: "Tagg"

    # De organisatoriska delar som pekas ut av relationen i denna struktur.
    organisationsdelar: "list[Organisationsdel]"


@jsontype()
@dataclass(kw_only=True)
class Organisationsdel(MedObligatoriskIdentifierare, MedGiltighet, MedTaggning, MedLokalUtokning):
    """En organisatorisk enhet (orgenhet) - någon del av organisationen bestående av en grupp människor
    utpekade genom att de tilldelats roller på orgenheten. Kan vara delar i linjen, matrisorganisationer,
    projekt...
    """

    # Orgenhetens namn.
    namn: SprakhanteradText = None

    # Orgenhetens typ(er). Övriga taggningar som inte kan sägas vara dess typ läggs i stället i .tags.
    # "Institution" är tydligt en typ av organisation, men om "resultatenhet" är en typ eller en taggning
    # är upp till varje lärosäte att avgöra.
    typer: list[Tagg] = None

    # Kommunikationsvägar till orgenheten som abstrakt entitet, t.ex. en info@institution-epostadress.
    kommunikationsvagar: "Kommunikation" = None

    # Rolltilldelningar, som knyter personer till orgenheten i betydelsen att de utför arbete åt den.
    rolltilldelningar: "list[Rolltilldelning]" = None

    # Servicefunktioner (t.ex. expeditioner) som erbjuder tjänster för denna orgenhet.
    servicefunktioner: "list[Servicefunktion]" = None

    # Anknytningsavtal för vilka denna orgenhet är motpart. Används t.ex. för att hitta vem som är en persons
    # lönesättande chef.
    motpartForAnknytningsavtal: "list[Hemvistperiod]" = None

    # Personer med vissa ansvar för denna orgenhet, utpekade personligen eller via en rolltilldelning.
    ansvarshallare: "list[Organisationsdelsansvar]" = None

    # Relationer som definierar denna orgenhets förälder/föräldrar. Andra änden av
    # OrganizationalRelation.child.
    foralderrelationer: "list[OrganisatoriskRelation]" = None

    # Relationer som definierar denna orgenhets barn. Andra änden av OrganizationalRelation.parent.
    barnrelationer: "list[OrganisatoriskRelation]" = None

    # Orgenheter som är relevanta för filtrering, uppdelade per relationstyp. Vanligt är t.ex. relationen
    # 'en del av', där man för orgenhet X har en lista av alla orgenheter som X anses vara 'en del av'.
    filterrelationer: "list[Kontextualiseradorganisationsdelsrelation]" = None


@jsontype()
@dataclass(kw_only=True)
class OrganisatoriskRelation(MedObligatoriskIdentifierare, MedGiltighet, MedTaggning, MedLokalUtokning):
    """En relation mellan två organisatoriska enheter, som säger att i en viss struktur ligger den ena
    ovanför den andra. Vissa lärosäten har många olika strukturer/perspektiv som utgör separata träd,
    t.ex. linjeträd, grundutbildningsorganisation, programorganisation, och utvisningsträd för webben.
    """
    # Den/de strukturer/träd/perspektiv som denna relation gäller för.
    typer: list[Tagg]

    # Den orgenhet som är förälder/ovanför i denna relation. Andra änden av Organization.childRelations.
    foralder: "Organisationsdel" = None

    # Den orgenhet som är barn/under i denna relation. Andra änden av Organization.parentRelations.
    barn: "Organisationsdel" = None
