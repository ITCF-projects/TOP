import datetime
import enum
from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Tagg, MedTaggning, Identifierare, MedGiltighet, MedLokalUtokning

if TYPE_CHECKING:
    from top2.rolltilldelning import Rolltilldelning
    from top2.anknytningsavtal import Anknytningsavtal


@jsontype()
class RemunerationCode(enum.Enum):
    Paid = "Paid"
    Unpaid = "Unpaid"


@jsontype()
@dataclass(kw_only=True)
class Kontering(MedLokalUtokning):
    # Alla relevanta ID:n för att göra en tillräckligt detaljerad specifikation (konto, kostnadsställe, mm)
    konton: list[Identifierare]
    # Den del av värdet som konteras på detta sätt. När en ersättning konteras skall summan av alla
    # Kontering bli samma som ersättnings totalvärde. Valutan är samma som ersättningens valuta.
    varde: float


@jsontype()
@dataclass(kw_only=True)
class Engangsersattning(MedTaggning, MedLokalUtokning):
    """Engångsersättning, t.ex. ett arvode."""

    # Typen av ersättning, t.ex. arvode.
    typ: Tagg

    utbetalningsdatum: datetime.date

    # Monetärt värde, per utbetalning.
    varde: float

    # Valuta
    valuta: str

    # Hur summan delas upp på olika konteringar.
    konteringar: list[Kontering] = None

    # Den rolltilldelningsperiod som denna ersättning detaljerar.
    detaljerarRolltilldelning: "Rolltilldelning" = None

    # Den anknytningsperiod som denna ersättning detaljerar.
    detaljerarAnknytningsperiod: "Anknytningsavtal" = None


@jsontype()
@dataclass(kw_only=True)
class LopandeErsattning(MedGiltighet, MedTaggning, MedLokalUtokning):
    """Löpande ersättningar, t.ex. lön eller tillägg. Vilken typ av ersättning, liksom hur ofta
    och när den utbetalas, måste förstås av typtaggen.
    """

    # Ersättningstypen, t.ex. månadslön eller lönetillägg.
    typ: Tagg

    # Monetärt värde, per utbetalning.
    varde: float

    # Valuta
    valuta: str

    # Hur summan delas upp på olika konteringar.
    konteringar: list[Kontering] = None

    # Den rolltilldelning som denna period detaljerar.
    detaljerarRolltilldelning: "Rolltilldelning" = None

    # Den anknytningsperiod som denna period detaljerar.
    detaljerarAnknytningsperiod: "Anknytningsavtal" = None

