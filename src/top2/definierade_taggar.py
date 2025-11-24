
from top2.common import Tagg


class Anstallningsformer:
    """
    TODO: "Anställningsform" är ett begrepp i Primula som omfattar t.ex. pensionärer som strikt talat inte
          är anställningar. "Bemanningspersonal" är en _starkare_ relation än Emeritus, men räknas inte som
          en anställningsform (förmodligen eftersom HR inte hanterar dem?)

          "Avtalstyp" nedan är mer generellt, men det finns ett överlapp här som måste definieras tydligare!
    """
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


class Organisationsdelstyper:
    class _Orgdelstyp(Tagg):
        def __init__(self, value: str, sv_name: str):
            super().__init__(namnrymd="*", typnamn="orgdelstyp", varde=value, namn={"sv": sv_name})

    University = _Orgdelstyp("universtiy", "lärosätet i sig. För de flesta bär exakt en organisatorisk enhet denna tagg - roten i linjeträdet.")
    Fakultet = _Orgdelstyp("fakultet", "Fakultet.")
    Institution = _Orgdelstyp("institution", "Institution.")
    Linje = _Orgdelstyp("linje", "Linjeorganisatorisk del.")


class Orghemviststyper:
    class _OrganizationalHomeType(Tagg):
        def __init__(self, value: str, sv_name: str):
            super().__init__(namnrymd="*", typnamn="hemviststyp", varde=value, namn={"sv": sv_name})

    Linje = _OrganizationalHomeType("linje", "Linjehemvist")


class Personkategorier:
    """I standarden definierar vi ett smalt urval av begrepp. Vi har medvetet undvikit att definiera standardtaggar
    för sådant som baseras på akademiska meriter eller som motsvarar akademiska titlar, eftersom dessa inte har
    identisk betydelse och dessutom inte kontrolleras av IT-sidan.
    """

    class _Personkategori(Tagg):
        def __init__(self, value: str, sv_name: str):
            super().__init__(namnrymd="*", typnamn="personkategori", varde=value, namn={"sv": sv_name})

    Anstallningsliknande = _Personkategori("anstallningsliknande", "någon vars förhållanden i de flesta avseenden kan likställas med personer som är formellt anställda av lärosätet, t.ex. bemanningspersonal eller företagsdoktorander.")
    Undervisande = _Personkategori("undervisande", "Undervisande personal")
    Forskande = _Personkategori("forskande", "Forskande personal")
    Stod = _Personkategori("stod", "Stödpersonal / TA-personal")
    Doktorand = _Personkategori("doktorand", "Doktorand (det finns flera olika avtalstyper för doktorander, den här taggen kan användas för att inte behöva sprida den kunskapen till mottagarna).")


class Anknytningsavtalstyper:
    class _Avtalstyp(Tagg):
        def __init__(self, value: str, sv_name: str):
            super().__init__(namnrymd="*", typnamn="avtalstyp", varde=value, namn={"sv": sv_name})

    Anstalld = _Avtalstyp("anstalld", "Avtal för fast anställd (tillsvidare, visstid, vikariat, tidsbegränsad)")
    Adjungerad = _Avtalstyp("adjungerad", "Adungerad")
    Pensionerad = _Avtalstyp("pensionerad", "Avtal för person som trots pension är kvar inom lärosätets organisation, dock utan att ha fått formell status som emeritus/emerita.")
    Emeriti = _Avtalstyp("emeriti", "Avtal som representerar den formella utnämningen av någon till emeritus/emerita på lärosätet.")
    Studentmedarbetare = _Avtalstyp("studentmedarbetare", "Avtal för studenter som får tidsbegränsad anställning för att t.ex. vara övningsledare eller rätta tentor. Inkluderar även amanuenser.")
    Intermittent = _Avtalstyp("intermittent", "avtal för tentavakter och andra som arbetar 'på timmar'.")
    Stipendiat = _Avtalstyp("stipendiat", "avtalstyp för doktorand som finaniseras genom stipendium hanterat av lärosätet. 'Vanliga' doktoranders avtal är anställningar.")
    AdjAffUtanLon = _Avtalstyp("adfaffutanlon", "Avtalstyp för adjungerad / affilierad utan lön.")
    Industridoktorand = _Avtalstyp("industridoktorand", "Avtal som knyter en person anställd av annat företag som doktorand (ofta kallat 'företagsdoktorand' eller 'industridoktorand').")
    Bemanningspersonal = _Avtalstyp("bemanningspersonal", "Avtal som knyter in en konsult på en generell roll som kunde varit en tillsvidareanställning. 'konsult' används för mer specifika uppdrag.")
    Konsult = _Avtalstyp("konsult", "Avtal för en konsult inhyrd för speciellt projekt/uppdrag. Jämför med 'bemanningspersonal', som knyter in personen på en generell plats bland personalen snarare än ett specifikt uppdrag.")

