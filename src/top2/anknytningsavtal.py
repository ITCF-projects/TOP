from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import MedTaggning, MedObligatoriskIdentifierare, MedGiltighet, Tagg, MedLokalUtokning, MedTyptagg

if TYPE_CHECKING:
    from top2.person import Person
    from top2.organisationsdel import Organisationsdel
    from top2.ersattningar import LopandeErsattning, Engangsersattning
    from top2.omfattningsperiod import Franvaroperiod, Omfattningsperiod


@jsontype()
@dataclass(kw_only=True)
class Skatt(MedGiltighet):
    SINK: float
    tabell: str
    kolumn: str
    procskatt: float
    jamkning: float
    ungdomsskatt: bool


@jsontype()
@dataclass(kw_only=True)
class Hemvistperiod(MedGiltighet, MedTyptagg, MedTaggning, MedLokalUtokning):
    """Säger att den organisatoriska hemvisten för ett visst anknytningsavtal under viss period ligger
    på en viss orgenhet. Den organisatoriska hemvisten används för att beräkna var ansvaret för en
    person ligger (t.ex. chefsansvar).
    """

    # Den organisatoriska enhet som ansvarar för den person som anknyntningsavtalet gäller.
    organisationsdel: "Organisationsdel"

    # Det anknytningsavtal som denna orghemvist detaljerar.
    anknytningsperiod: "Anknytningsavtal" = None


@jsontype()
@dataclass(kw_only=True)
class Anknytningsavtal(MedObligatoriskIdentifierare, MedTaggning, MedGiltighet, MedLokalUtokning):
    """Anknytningsavtal, som berättar hur en viss person knutits till huvudorganisationen - allt ifrån
    anställningar till rent muntliga avtal.
    """
    person: "Person" = None

    # Typ av anknytningsavtal, t.ex. "anställning", "delegering" eller "muntligt avtal".
    typ: Tagg

    # Den organisationsdel som är motpart i avtalet. För anställningsavtal är detta lärosätet som helhet,
    # och vilken organisationsdel (t.ex. institution eller avdelning) personen har sin chef/ansvarige
    # pekas ut via hemvistperioder. För muntliga avtal är motparten den institution eller liknande vars
    # chef gjort överenskommelsen.
    organisationellAvtalspart: "Organisationsdel" = None

    # Organisatorisk(a) hemvist(er) - på vilken organisationsdel placerar detta avtal just nu personen.
    # Bara en får vara giltig åt gången, men det går här att lägga in både dåtida och framtida
    # orghemvister om man kan och vill.
    hemvistperioder: "list[Hemvistperiod]" = None

    # Omfattningar för denna rolltilldelning.
    omfattningsperioder: "list[Omfattningsperiod]" = None

    # Frånvaroperioder. Alla förhållanden som minskar omfattningen (.workSchedule) under någon period,
    # t.ex. semester, tjänstledighet eller sjukskrivning.
    franvaroperioder: "list[Franvaroperiod]" = None

    # Lön eller ersättning. Kan vara flera, och kan variera under giltighetstiden. Lönetillägg för
    # specifika rolltilldelningar (t.ex. prefekttillägg) läggs i rolltilldelningen.
    lopandeErsattningar: "list[LopandeErsattning]" = None

    # Engångsersättningar för denna rolltilldelning.
    engangsersattningar: "list[Engangsersattning]" = None

    # Begränsningskoden talar om varför någon inte har en fastanställning.
    begransningskod: str = None

    # Om du, av någon anledning, inte kan hantera att personer omfattas av mer än ett avtal,
    # ta det här avtalet.
    huvudavtal: bool = None

    # Detta avtal är underordnat ett annat (t.ex. kan en delegering vara underordnad en anställning),
    # det är ett "hängavtal". Giltigheten på detta avtal begränsas därmed av giltigheten på det
    # utpekade avtalet.
    underordnat: "Anknytningsavtal" = None

    # Andra avtal som är underordnade detta. De underordnade avtalen kan aldrig vara giltiga när detta
    # avtal inte är det.
    underordnade: "list[Anknytningsavtal]" = None

    # Om vi vill veta varför ett visst avtal har avslutats så kan vi skriva något om det här.
    avslutsorsak: str = None

    # aanstperiod.avslutdkod_id -> avslutskod.typ (typ är t.ex. "1" för S1).
    # Det finns för t.ex. anställningar formella koder till pensionsmyndigheten (S1-S9). Dessa är
    # taggar som man kan lägga in här.
    avslutsorsakskoder: list[Tagg] = None

    # Anställningsnummer används vid rapporter till Skatteverket med mera.
    anstallningsnummer: int = None

    # Befattningarna är lönenära och matchar nästan, men inte riktigt, rollen.
    befattningsnamn: str = None
    befattningskategori: str = None
    befattningskodSCB: str = None

    # BESTA-kod (9 tecken).
    BESTA: str = None

    skatt: Skatt = None
