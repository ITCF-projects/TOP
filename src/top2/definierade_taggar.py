
from top2.common import Tagg


class Anstallningsformer:
    class _Anstallningsform(Tagg):
        def __init__(self, value: str, sv_name: str):
            super().__init__(namnrymd="*", typnamn="anställningsform", varde=value, namn={"sv": sv_name})

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


class Orghemviststyper:
    class _OrganizationalHomeType(Tagg):
        def __init__(self, value: str, sv_name: str):
            super().__init__(namnrymd="*", typnamn="hemviststyp", varde=value, namn={"sv": sv_name})

    Linje = _OrganizationalHomeType("linje", "Linjehemvist")


