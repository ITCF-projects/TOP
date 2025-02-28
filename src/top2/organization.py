from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Tag, I18nText, TagsMixin, OptionalIdMixin, MandatoryIdMixin, EffectiveTimePeriodMixin, ExtendableMixin

if TYPE_CHECKING:
    from top2.deployment import Deployment
    from top2.communication import Communication
    from top2.responsibility import OrganizationResponsibility
    from top2.work_life_cycle import OrganizationalHome


@jsontype()
@dataclass(kw_only=True)
class ServiceFunction(OptionalIdMixin, EffectiveTimePeriodMixin, TagsMixin, ExtendableMixin):
    """En servicefunktion, t.ex. en expedition, handläggargrupp, eller annat sätt att utföra arbete som inte
    direkt relaterar till en specifik rolltilldelning. Servicefunktionerna kan tillhöra en eller flera
    orgenheter. Både fysiska expeditioner med besökstider och handläggargrupper i ett ärendehanteringssystem
    kan representeras som servicefunktioner.
    """

    # Servicefunktionens namn, t.ex. "Datatekniska institutionens expedition".
    name: I18nText

    # En beskrivning, t.ex. "Hjälper dig att klaga på tentor och säger nej till passerkortsbehörigheter"
    description: I18nText = None

    # Kommunikationsvägar till servicefunktionen (inklusive eventuella besökstider).
    communications: "Communication" = None

    # Den eller de rolltilldelningar via vilka servicefunktionen bemannas. För en studentmottagning kan man
    # t.ex. peka ut de rolltilldelningar som studievägledare som gör att vissa personer förväntas bemanna
    # mottagningen.
    staffedViaDeployments: "list[Deployment]" = None

    # De orgenheter för vilka denna servicefunktion tillhandahåller tjänster.
    organizations: "list[Organization]" = None


@jsontype()
@dataclass(kw_only=True)
class ScopedOrganizationalRelation:
    """En kontextualiserad relation med en orgenhet. Används i Organization.filterRelations. Taggen kan
    t.ex. representera filterkontexten "en del av", och peka ut alla orgenheter som en viss orgenhet
    kan anses vara "en del av".
    """
    # Den struktur där relationen gäller.
    type: "Tag"
    # De orgenheter som pekas ut av relationen i denna struktur.
    organizations: "list[Organization]"


@jsontype()
@dataclass(kw_only=True)
class Organization(MandatoryIdMixin, EffectiveTimePeriodMixin, TagsMixin, ExtendableMixin):
    """En organisatorisk enhet (orgenhet) - någon del av organisationen bestående av en grupp människor
    utpekade genom att de tilldelats roller på orgenheten. Kan vara delar i linjen, matrisorganisationer,
    projekt...
    """

    # Orgenhetens namn.
    name: I18nText = None

    # Orgenhetens typ(er). Övriga taggningar som inte kan sägas vara dess typ läggs i stället i .tags.
    # "Institution" är tydligt en typ av organisation, men om "resultatenhet" är en typ eller en taggning
    # är upp till varje lärosäte att avgöra.
    types: list[Tag] = None

    # Kommunikationsvägar till orgenheten som abstrakt entitet, t.ex. en info@institution-epostadress.
    communications: "Communication" = None

    # Rolltilldelningar, som knyter personer till orgenheten i betydelsen att de utför arbete åt den.
    deployments: "list[Deployment]" = None

    # Servicefunktioner (t.ex. expeditioner) som erbjuder tjänster för denna orgenhet.
    serviceFunctions: "list[ServiceFunction]" = None

    # Anknytningsavtal för vilka denna orgenhet är motpart. Används t.ex. för att hitta vem som är en persons
    # lönesättande chef.
    homed: "list[OrganizationalHome]" = None

    # Personer med vissa ansvar för denna orgenhet, utpekade personligen eller via en rolltilldelning.
    responsible: "list[OrganizationResponsibility]" = None

    # Relationer som definierar denna orgenhets förälder/föräldrar. Andra änden av
    # OrganizationalRelation.child.
    parentRelations: "list[OrganizationalRelation]" = None

    # Relationer som definierar denna orgenhets barn. Andra änden av OrganizationalRelation.parent.
    childRelations: "list[OrganizationalRelation]" = None

    # Orgenheter som är relevanta för filtrering, uppdelade per relationstyp. Vanligt är t.ex. relationen
    # 'en del av', där man för orgenhet X har en lista av alla orgenheter som X anses vara 'en del av'.
    filterRelations: "list[ScopedOrganizationalRelation]" = None


@jsontype()
@dataclass(kw_only=True)
class OrganizationalRelation(MandatoryIdMixin, EffectiveTimePeriodMixin, TagsMixin, ExtendableMixin):
    """En relation mellan två organisatoriska enheter, som säger att i en viss struktur ligger den ena
    ovanför den andra. Vissa lärosäten har många olika strukturer/perspektiv som utgör separata träd,
    t.ex. linjeträd, grundutbildningsorganisation, programorganisation, och utvisningsträd för webben.
    """
    # Den/de strukturer/träd/perspektiv som denna relation gäller för.
    types: list[Tag]

    # Den orgenhet som är förälder/ovanför i denna relation. Andra änden av Organization.childRelations.
    parent: "Organization" = None

    # Den orgenhet som är barn/under i denna relation. Andra änden av Organization.parentRelations.
    child: "Organization" = None
