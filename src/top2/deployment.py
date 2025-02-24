from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import TagsMixin, MandatoryIdMixin, EffectiveTimePeriodMixin

if TYPE_CHECKING:
    from top2.job import Job
    from top2.person import Person
    from top2.organization import Organization, ServiceFunction
    from top2.remuneration import RemunerationOrDeduction
    from top2.communication import Communication
    from top2.work_schedule import WorkSchedule
    from top2.responsibility import DeploymentResponsibility, OrganizationResponsibility


@jsontype()
@dataclass(kw_only=True)
class Deployment(MandatoryIdMixin, EffectiveTimePeriodMixin, TagsMixin):
    """En rolltilldelning - säger att en person förväntas agera i en viss roll för en viss
    del av organisationen under viss tid. Om man varken känner till start- eller slutdatum utelämnas
    effectiveTimePeriod.
    """

    person: "Person" = None

    # Den orgenhet där personen tilldelats rollen. Andra änden av Organisation.deployments.
    organization: "Organization" = None

    # Kommunikationsvägar till personen i kontexten av denna rolltilldelning.
    communications: "Communication" = None

    # Den roll som personen tilldelas.
    job: "Job" = None

    # Omfattning(ar) för denna rolltilldelning.
    workSchedules: "list[WorkSchedule]" = None

    # Lönetillägg eller andra extra ersättningar som personen får för denna rolltilldelning. Kan vara
    # flera, och kan variera under giltighetstiden. Lön läggs i avtalsperioden. Andra änden av
    # WorkLifeCycle.remunerations.
    remunerations: "list[RemunerationOrDeduction]" = None

    # De ansvar som denna rolltilldelning medför (t.ex. linjechefsansvar för en orgenhet tilldelat av en
    # rolltilldelning som enhetschef. Andra änden av OrganizationResponsibility.deployment.
    organizationResponsibilities: "list[OrganizationResponsibility]" = None

    # Personliga ansvar tilldelade någon annan för denna rolltilldelning (t.ex. handledarskap för en
    # rolltilldelning som praktikant). Andra änden av DeploymentResponsibility.deployment.
    explicitlyResponsible: "list[DeploymentResponsibility]" = None

    # De servicefunktioner (om några) som bemannas via denna rolltilldelning. En specifik rolltilldelning
    # som studievägledare kan t.ex. innebära att man bemannar en studentmottagning.

    staffsServiceFunctions: "list[ServiceFunction]" = None
