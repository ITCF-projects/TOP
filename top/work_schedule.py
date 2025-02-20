from dataclasses import dataclass
from typing import *

from top.common import TagsMixin, TypeMixin, OptionalIdMixin, EffectiveTimePeriodMixin

if TYPE_CHECKING:
    from top.deployment import Deployment
    from top.remuneration import RemunerationCode
    from top.work_life_cycle import WorkLifeCycle


@dataclass(kw_only=True)
class WorkSchedule(EffectiveTimePeriodMixin, TagsMixin, TypeMixin, OptionalIdMixin):
    """En mängd arbetstid som personen i kontexten av ett anknytningsavtal förväntas utföra (en
    omfattningsperiod). Kan antingen vara ett visst antal timmar (hours) eller en del av heltid
    (fullTimeEquivalentRatio). Kan alltså tillsammans med giltighetstider uttrycka '200 timmar under 2023',
    '20% under januari 2024' och '95% av en heltid löpande'. Syftet är att överföra förutsättningar,
    inte utfall. Avsikten är alltså inte att den skall representera en timrapport.
    """

    # Andel av heltid, som ett flyttal.
    fullTimeEquivalentRatio: float = None

    # Ett visst antal timmar.
    hours: int = None

    # Den rolltilldelning som denna omfattningsperiod detaljerar.
    deployment: "Deployment" = None

    # Den anknytningsperiod som denna omfattningsperiod detaljerar.
    workLifeCycle: "WorkLifeCycle" = None


@dataclass(kw_only=True)
class Leave(EffectiveTimePeriodMixin, TagsMixin, OptionalIdMixin, TypeMixin):
    """En frånvaroperiod uttrycker semester, föräldraledighet, sjukskrivningar med mera. Det finns möjlighet
    att ange en omfattning om man önskar.
    """
    # Andel av heltid, som ett flyttal.
    fullTimeEquivalentRatio: float = None

    # Ett visst antal timmar.
    hours: int = None

    # Betald eller obetald frånvaro.
    remunerationCode: "RemunerationCode" = None

    # Om sann så är slutdatumet på perioden preliminärt, t.ex. slutdatum på en längre sjukskrivning som kan
    # få en fortsättning. Om falsk så förväntas personens frånvaro sluta enligt giltigheten, t.ex. en
    # beviljad semesterperiod.
    returnDateIsScheduled: bool = None

    # Den anknytningsperiod som denna frånvaroperiod detaljerar.
    workLifeCycle: "WorkLifeCycle" = None
