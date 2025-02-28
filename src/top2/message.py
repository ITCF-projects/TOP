import dataclasses

from schemagen import jsontype

from top2.deployment import Deployment
from top2.job import Job
from top2.organization import Organization
from top2.person import Person, AccessCard, AccessPrivilege
from top2.work_life_cycle import WorkLifeCycle


@jsontype()
@dataclasses.dataclass(kw_only=True)
class Message:
    """Toppobjekt med enkla och listvärda referenser till samtliga värdeobjekt. Bra grund för meddelanden!"""

    accessCard: AccessCard = None
    accessCards: list[AccessCard] = None
    accessPrivilege: AccessPrivilege = None
    accessPrivileges: list[AccessPrivilege] = None
    deployment: Deployment = None
    deployments: list[Deployment] = None
    job: Job = None
    jobs: list[Job] = None
    organization: Organization = None
    organizations: list[Organization] = None
    person: Person = None
    persons: list[Person] = None
    work_life_cycle: WorkLifeCycle = None
    work_life_cycles: list[WorkLifeCycle] = None
