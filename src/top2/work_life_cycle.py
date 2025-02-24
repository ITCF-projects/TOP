from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import TagsMixin, MandatoryIdMixin, EffectiveTimePeriodMixin, Tag

if TYPE_CHECKING:
    from top2.person import Person
    from top2.organization import Organization
    from top2.remuneration import RemunerationOrDeduction
    from top2.work_schedule import Leave, WorkSchedule


class _Anstallningsform(Tag):
    def __init__(self, value: str, sv_name: str):
        super().__init__(schemeAgencyId="*", schemeId="anställningsform", value=value, name={"sv": sv_name})


class WorkLifeCycleTags:
    class Anstallningsformer(Tag):
        Tillsvidare = _Anstallningsform("tillsvidare", "Tillsvidareanställning")
        Visstid = _Anstallningsform("visstid", "Visstidsanställning")
        Vikariat = _Anstallningsform("vikariat", "Vikariat")
        Tidsbegransad = _Anstallningsform("tidsbegransad", "Tidsbegränsad anställning")
        Prov = _Anstallningsform("prov", "Provanställning")
        Pensionar = _Anstallningsform("pensionär", "Pensionär")
        Studentmedarbetare = _Anstallningsform("studentmedarbetare", "Studentmedarbetare")
        Intermittent = _Anstallningsform("intermittent", "Intermittent anställd (timanställd)")
        Stipendiat = _Anstallningsform("stipendiat", "Stipendiat")
        Emeriti = _Anstallningsform("emeriti", "Emeritus/emerita")
        Adjungerad = _Anstallningsform("adjungerad", "Adjungerad/affilierad")


@jsontype()
@dataclass(kw_only=True)
class OrganizationalHome(EffectiveTimePeriodMixin, TagsMixin):
    """Säger att den organisatoriska hemvisten för ett visst anknytningsavtal under viss period ligger
    på en viss orgenhet. Den organisatoriska hemvisten används för att beräkna var ansvaret för en
    person ligger (t.ex. chefsansvar).
    """

    # Den organisatoriska enhet som ansvarar för den person som anknyntningsavtalet gäller.
    organization: Annotated[
        "Organization", "Den organisatoriska enhet som ansvarar för den person som anknyntningsavtalet gäller."]
    # Det anknytningsavtal som denna orghemvist detaljerar.
    workLifeCycle: Annotated["WorkLifeCycle", "Det anknytningsavtal som denna orghemvist detaljerar."] = None


@jsontype()
@dataclass(kw_only=True)
class WorkLifeCycle(MandatoryIdMixin, TagsMixin, EffectiveTimePeriodMixin):
    """Anknytningsavtal, som berättar hur en viss person knutits till huvudorganisationen - allt ifrån
    anställningar till rent muntliga avtal.
    """
    _json_type_name = "WorkLifeCycle"

    person: "Person" = None

    # Den organisation (oftast lärosätet) som är motpart på kontraktet. Vilken del av lärosätet (t.ex.
    # insitution eller avdelning) personen har sin chef/ansvarige pekas ut via workerHomes.
    signingOrganization: "Organization" = None

    # Organisatorisk(a) hemvist(er). Bara en får vara giltig åt gången, men det går här att lägga in
    # både dåtida och framtida orghemvister om man kan och vill.
    workerHomes: "list[OrganizationalHome]" = None

    # Omfattningar för denna rolltilldelning.
    workSchedules: "list[WorkSchedule]" = None

    # Frånvaroperioder. Alla förhållanden som minskar omfattningen (.workSchedule) under någon period,
    # t.ex. semester, tjänstledighet eller sjukskrivning.
    leave: "list[Leave]" = None

    # Lön eller ersättning. Kan vara flera, och kan variera under giltighetstiden. Lönetillägg för
    # specifika rolltilldelningar (t.ex. prefekttillägg) läggs i rolltilldelningen Deployment.remunerations
    remunerations: "list[RemunerationOrDeduction]" = None
