from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Identifier, MandatoryIdMixin, OptionalIdMixin, EffectiveTimePeriodMixin, TagsMixin, ExtendableMixin

if TYPE_CHECKING:
    from top2.deployment import Deployment
    from top2.communication import Communication
    from top2.responsibility import CalculatedResponsibility, OrganizationResponsibility
    from top2.work_life_cycle import WorkLifeCycle


@jsontype()
@dataclass(kw_only=True)
class AccessPrivilege(EffectiveTimePeriodMixin, OptionalIdMixin, ExtendableMixin):
    """En passerbehörighet, identifierad av ett för mottagaren meningsfullt ID. Tilldelningen av behörigheten
    görs till en person eller ett passerkort."""

    # Behörighetens ID (inte resursen behörigheten gäller för).
    privilegeId: Identifier
    # ID på den resurs som behörigheten gäller för (inte behörighetens egna ID om ett sådant finns).
    resourceId: Identifier
    # De person(er) som tilldelats behörigheten.
    assignedToPersons: "list[Person]"
    # De passerkort som tilldelats behörigheten.
    assignedToAccessCards: "list[AccessCard]"


@jsontype()
@dataclass(kw_only=True)
class AccessCard(OptionalIdMixin, EffectiveTimePeriodMixin, ExtendableMixin):
    """Ett passerkort och de behörigheter detta kort skall vara försedda med. Om behörigheter knyts till
    personen snarare än till dennes kort så används istället PersonType.accessPrivileges. Notera att
    giltighetstider i detta objekt rör passerkortet i sig, behörigheterna har egna giltighetstider.
    """
    # Kortets id.
    cardId: Identifier

    # Behörigheter som kortet skall förknippas med (behörigheter för individ läggs i Person.accessPrivileges)
    accessPrivileges: list[AccessPrivilege] = None


@jsontype()
@dataclass(kw_only=True)
class Name(ExtendableMixin):
    given: str
    family: str
    formattedName: str
    familyList: list[str] = None
    preferred: str = None


@jsontype()
@dataclass(kw_only=True)
class Person(MandatoryIdMixin, TagsMixin, ExtendableMixin, EffectiveTimePeriodMixin):
    """A Person."""
    _json_type_name = "Person"

    name: Name = None

    # Kommunikationsvägar till personen som individ
    communications: "Communication" = None

    # Accessbehörigheter som personen skall ha, oavsett passerkort.
    accessPrivileges: list[AccessPrivilege] = None

    # Passerkort inklusive eventuella behörigheter för kortet i sig snarare än för personen.
    accessCards: list[AccessCard] = None

    # Anknytningsavtal för denna person.
    workLifeCycles: "list[WorkLifeCycle]" = None

    # Rolltilldelningar för denna person.
    deployments: "list[Deployment]" = None

    deceased: bool = None

    # Personligt tilldelade ansvar.
    personalOrganizationalResponsibiltites: "list[OrganizationResponsibility]" = None

    # Alla ansvar denna person kan beräknas ha för andra personer.
    calculatedResponsibilities: "list[CalculatedResponsibility]" = None

    # Alla ansvar andra personer kan beräknas ha över denna person",
    affectedByResponsibilities: "list[CalculatedResponsibility]" = None
