from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Taggning, Tagg, FrivilligIdentifiering, Giltighet, LokalUtokning

if TYPE_CHECKING:
    from top2.rolltilldelning import Rolltilldelning
    from top2.ersattningar import RemunerationCode
    from top2.anknytningsavtal import Anknytningsavtal


@jsontype()
@dataclass(kw_only=True)
class Omfattningsperiod:
    """En mängd arbetstid som personen i kontexten av ett anknytningsavtal förväntas utföra (en
    omfattningsperiod). Kan antingen vara ett visst antal timmar (hours) eller en del av heltid
    (fullTimeEquivalentRatio). Kan alltså tillsammans med giltighetstider uttrycka '200 timmar under 2023',
    '20% under januari 2024' och '95% av en heltid löpande'. Syftet är att överföra förutsättningar,
    inte utfall. Avsikten är alltså inte att den skall representera en timrapport.
    """

    # Identifiering av omfattningsperioden.
    identifiering: FrivilligIdentifiering = None

    # Giltighet för denna omfattningsperiod.
    giltighet: Giltighet = None

    # Taggning av omfattningsperioden.
    taggning: Taggning = None

    # Typ av omfattningsperiod.
    typ: Tagg = None

    # Lokala utökningar.
    lokalUtokning: LokalUtokning = None

    # Andel av heltid, som ett flyttal.
    heltidsandel: float = None

    # Ett visst antal timmar.
    timmar: int = None

    # Fördelning av timmar över veckodagar.
    timmarPerDag: list[float] = None

    # Den rolltilldelning som denna omfattningsperiod detaljerar.
    rolltilldelning: "Rolltilldelning" = None

    # Den anknytningsperiod som denna omfattningsperiod detaljerar.
    anknytningsperiod: "Anknytningsavtal" = None


@jsontype()
@dataclass(kw_only=True)
class Franvaroperiod:
    """En frånvaroperiod uttrycker semester, föräldraledighet, sjukskrivningar med mera. Det finns möjlighet
    att ange en omfattning om man önskar.
    """

    # Identifiering av frånvaroperioden.
    identifiering: FrivilligIdentifiering = None

    # Giltighet för denna frånvaroperiod.
    giltighet: Giltighet = None

    # Taggning av frånvaroperioden.
    taggning: Taggning = None

    # Typ av frånvaro.
    typ: Tagg = None

    # Lokala utökningar.
    lokalUtokning: LokalUtokning = None

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
    anknytningsperiod: "Anknytningsavtal" = None
