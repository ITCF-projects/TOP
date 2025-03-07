from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import MedTaggning, MedTyptagg, MedFrivilligIdentifierare, MedGiltighet, MedLokalUtokning

if TYPE_CHECKING:
    from top2.rolltilldelning import Rolltilldelning
    from top2.ersattningar import RemunerationCode
    from top2.anknytningsperiod import Anknytningsperiod


@jsontype()
@dataclass(kw_only=True)
class Omfattningsperiod(MedGiltighet, MedTaggning, MedTyptagg, MedFrivilligIdentifierare, MedLokalUtokning):
    """En mängd arbetstid som personen i kontexten av ett anknytningsavtal förväntas utföra (en
    omfattningsperiod). Kan antingen vara ett visst antal timmar (hours) eller en del av heltid
    (fullTimeEquivalentRatio). Kan alltså tillsammans med giltighetstider uttrycka '200 timmar under 2023',
    '20% under januari 2024' och '95% av en heltid löpande'. Syftet är att överföra förutsättningar,
    inte utfall. Avsikten är alltså inte att den skall representera en timrapport.
    """

    # Andel av heltid, som ett flyttal.
    heltidsandel: float = None

    # Ett visst antal timmar.
    timmar: int = None

    # Fördelning av timmar över veckodagar.
    timmarPerDag: list[float] = None

    # Den rolltilldelning som denna omfattningsperiod detaljerar.
    rolltilldelning: "Rolltilldelning" = None

    # Den anknytningsperiod som denna omfattningsperiod detaljerar.
    anknytningsperiod: "Anknytningsperiod" = None


@jsontype()
@dataclass(kw_only=True)
class Franvaroperiod(MedGiltighet, MedTaggning, MedFrivilligIdentifierare, MedTyptagg, MedLokalUtokning):
    """En frånvaroperiod uttrycker semester, föräldraledighet, sjukskrivningar med mera. Det finns möjlighet
    att ange en omfattning om man önskar.
    """
    # Andel av heltid, som ett flyttal.
    heltidsandel: float = None

    # Ett visst antal timmar.
    timmar: int = None

    # Betald eller obetald frånvaro.
    betaldFranvaro: bool = None

    # Om sann så är slutdatumet på perioden preliminärt, t.ex. slutdatum på en längre sjukskrivning som kan
    # få en fortsättning. Om falsk så förväntas personens frånvaro sluta enligt giltigheten, t.ex. en
    # beviljad semesterperiod.
    slutdatumArPreliminart: bool = None

    # Den anknytningsperiod som denna frånvaroperiod detaljerar.
    anknyntningsperiod: "Anknytningsperiod" = None
