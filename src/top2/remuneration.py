import enum
from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Tag, TagsMixin, Identifier, EffectiveTimePeriodMixin

if TYPE_CHECKING:
    from top2.deployment import Deployment
    from top2.work_life_cycle import WorkLifeCycle


@jsontype()
class RemunerationCode(enum.Enum):
    Paid = "Paid"
    Unpaid = "Unpaid"


@jsontype()
@dataclass(kw_only=True)
class PostingSpecification:
    # En kontering, uttryckt som alla relevanta ID:n.
    posting: list[Identifier]
    # Den del av summan som konteras på detta sätt. Flyttal 0..1.
    partOfAmount: float


@jsontype()
@dataclass(kw_only=True)
class RemunerationOrDeduction(EffectiveTimePeriodMixin, TagsMixin):
    """Ersättningar, t.ex. lön eller tillägg.
    """

    # Ersättningstypen, t.ex. månadslön eller engångsersättning.
    type: Tag

    # Värde
    value: float

    # Valuta
    currency: str

    # Hur summan delas upp på olika konteringar.
    postings: list[PostingSpecification] = None

    # Den rolltilldelning som denna omfattningsperiod detaljerar.
    deployment: "Deployment" = None

    # Den anknytningsperiod som denna omfattningsperiod detaljerar.
    workLifeCycle: "WorkLifeCycle" = None
