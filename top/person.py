from dataclasses import dataclass
from typing import *

from top.common import Identifier, MandatoryIdMixin, EffectiveTimePeriodMixin, TagsMixin

if TYPE_CHECKING:
    from top.deployment import Deployment
    from top.communication import Phone, Communication
    from top.responsibility import CalculatedResponsibility, OrganizationResponsibility
    from top.work_life_cycle import WorkLifeCycle


@dataclass(kw_only=True)
class AccessPrivilege(EffectiveTimePeriodMixin):
    """En passerbehörighet, identifierad av ett för mottagaren meningsfullt ID."""

    # Behörighetens ID (inte resursen behörigheten gäller för).
    privilegeId: Identifier
    # ID på den resurs som behörigheten gäller för (inte behörighetens egna ID om ett sådant finns).
    resourceId: Identifier


@dataclass(kw_only=True)
class AccessCard(EffectiveTimePeriodMixin):
    """Ett passerkort och de behörigheter detta kort skall vara försedda med. Om behörigheter knyts till
    personen snarare än till dennes kort så används istället PersonType.accessPrivileges. Notera att
    giltighetstider i detta objekt rör passerkortet i sig, behörigheterna har egna giltighetstider.
    """
    # Kortets id.
    cardId: Identifier

    # Behörigheter som kortet skall förknippas med (behörigheter för individ skickas i Person.accessPrivileges)
    accessPrivileges: list[AccessPrivilege] = None


@dataclass(kw_only=True)
class Name:
    given: str
    family: str
    formattedName: str
    familyList: list[str] = None
    preferred: str = None


@dataclass(kw_only=True)
class Person(MandatoryIdMixin, TagsMixin):
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


if __name__ == "__main__":
    from communication import Communication
    from work_life_cycle import WorkLifeCycle

    from top import to_json

    p = Person(name=Name(given="Viktor", family="Fougstedt", formattedName="Viktor Fougstedt"),
               communications=Communication(phone=[Phone(number="0317725011a", formattedNumber="+46 (0)31 775 50 11")]),
               id=Identifier(schemeAgencyId="chalmers.se", schemeId="pdb.person.nid", value="1231900001231"))

    w = WorkLifeCycle(id=Identifier(schemeAgencyId="chalmers.se", schemeId="primula.avtal", value="13381992"),
                      person=p)

    print(to_json(p))
    print(to_json(w))

    # @dataclass(kw_only=True)
    # class X:
    #     a: str
    #     a = StringProperty(regexp="[a-z]+")
    #     b: int
    #
    # x = X(a="abc", b=1)
    # print(to_json(x))
    # x = X(a="123", b=3)
    # print(to_json(x))
