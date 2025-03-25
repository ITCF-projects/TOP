import datetime
import enum
from dataclasses import dataclass

from typing import *
from schemagen import jsontype


@jsontype
@dataclass(kw_only=True)
class SprakhanteradText(dict):
    """Språkhanterad text. Nycklar är språkkod enligt RFC4646/RFC4647 (t.ex. 'en' eller 'sv'), värdet är
    texten på det språket."""
    __json_schema__ = {
        "type": "object",
        "patternProperties": {
            "^[a-z]{2,3}$": {"type": "string"}
        }
    }


@jsontype()
@dataclass(kw_only=True)
class Identifierare:
    """Identifierare med typ och värde. Två identifierare är identiska endast om namnrymd, typnamn, varde
    och varderymd (om den är angiven) är identiska.

    Syftet med namnrymden är att vi är många som kanske vill definiera en typ "person-id", och om sådana
    identifierare riskerar att mötas i något system skulle man kunna missta dem som samma identifierare.

    På samma sätt finns varderymd som är en namnrymd för värdet. Dess syfte är att kunna förmedla
    identifierare från t.ex. testinstanser utan risk att de misstas för skarpa värden.
    """

    # Namnrymd för typen, väsentligen är detta den som definierat typnamnet. Det möjliggör att
    # t.ex. både Chalmers och GU kan ha typer som heter "person-id". Skall vara '*' om TOP definierar
    # typen, annars något URL-liknande med minst ett domännamn för den som definierat semantiken för
    # typen.
    namnrymd: str

    # Kombinationen av (typDefinieradAv, typnamn) är en unikt definierad typ av identifierare, med
    # semantik enligt vad typDefinieradAv bestämt.
    typnamn: str

    # Värde
    varde: str

    # Domännamn eller liknande identifierare som ger en kontext för kombinationen (schemeAgencyId, schemeId,
    # value) om samma typ+värde finns i olika kontexter (t.ex. olika instanser av samma applikation). Behöver
    # bara användas när det finns en risk att sådana värden möts i samma mottagare. Oftast på formen
    # "lärosäte.se/applikationsinstans"
    varderymd: str = None


@jsontype()
@dataclass(kw_only=True)
class MedObligatoriskIdentifierare:
    # Huvudsakligt ID. Skall "aldrig" ändras, eller i alla fall så sällan det går. Personnummer är dåligt
    # (ändras ofta), medan ett UUID i en lokal personalkatalog kan vara finfint.
    postid: Identifierare

    # ID som kan återfinnas i andra applikationer eller externa system.
    korrelationsidn: list[Identifierare] = None

    # Om denna post är resultatet av att andra poster slagits samman, så ligger ID:na för de därmed
    # borttagna posterna här.
    sammanslagnaIdn: list[Identifierare] = None

    # Om ett korrelations-id försvinner, t.ex. vid ett personnummerbyte, så skickas det id som tidigare
    # varit korrelations-id här under en tid.
    tidigareKorrelationsidn: list[Identifierare] = None


@jsontype()
@dataclass(kw_only=True)
class MedFrivilligIdentifierare:
    # Huvudsakligt ID (om något finns). Skall "aldrig" ändras, eller i alla fall så sällan det går.
    # Personnummer är dåligt (ändras ofta), medan ett UUID i en lokal personalkatalog kan vara finfint.
    postid: Identifierare = None

    # ID:n som kan återfinnas i andra applikationer eller externa system.
    korrelationsidn: list[Identifierare] = None

    # Om denna post är resultatet av att andra poster slagits samman, så ligger ID:na för de därmed
    # borttagna posterna här.
    sammanslagnaIdn: list[Identifierare] = None

    # Om ett korrelations-id försvinner, t.ex. vid ett personnummerbyte, så skickas det id som tidigare
    # varit korrelations-id här under en tid.
    tidigareKorrelationsidn: list[Identifierare] = None


@jsontype()
@dataclass(kw_only=True)
class Giltighetsperiod:
    """En tidsperiod inom vilken ett associerat värde är giltigt. Om invalidFrom """
    giltigFrom: datetime.datetime
    ogiltigFrom: Optional[datetime.datetime]


class Giltighetsenum(enum.Enum):
    TIDIGARE = "tidigare"
    AKTUELLT = "aktuellt"
    FRAMTIDA = "framtida"


@jsontype()
@dataclass(kw_only=True)
class MedGiltighet:
    # Giltighet. Kan innehålla både en giltighetsperiod och en giltighetsenum. Om värdet utelämnas helt
    # så känner avsändaren varken till start- eller slutdatum, bara att objektet är giltigt just nu.
    giltighetsperiod: Giltighetsperiod = None
    utvarderadGiltighet: Giltighetsenum = None


@jsontype()
@dataclass(kw_only=True)
class Tagg:
    """En tag - en egenskap uttryckt som en boolesk variabel med ett sant värde. Dessa definieras oftast av
    lärosätet själva för att uttrycka egenskaper som 'anställningsliknande förhållande' på en person eller
    'linjeorganisation' på en organisatorisk del.

    Upplägget är i princip identiskt med identifierare, med utökningen att man kan skicka med en
    språkhanterad text för att visa taggen för människor. "varderymden" används för att lärosätena
    skall kunna skapa lokala taggar av en gemensamt överenskommen typ. Till exempel kan vi komma
    överens om att ha en tagtyp "anställningsform", där Chalmers vill ha någon egen variant. Då sätter
    Chalmers "chalmers.se" som värderymd på den taggen.
    """
    # Namnrymd för typen, väsentligen är detta den som definierat typnamnet. Det möjliggör att
    # t.ex. både Chalmers och GU kan ha typer som heter "person-id". Skall vara '*' om TOP definierar
    # typen, annars något URL-liknande med minst ett domännamn för den som definierat semantiken för
    # typen.
    namnrymd: str

    # Kombinationen av (typDefinieradAv, typnamn) är en unikt definierad typ av identifierare, med
    # semantik enligt vad typDefinieradAv bestämt.
    typnamn: str

    # Värde
    varde: str

    # Domännamn eller liknande identifierare som ger en kontext för kombinationen (schemeAgencyId, schemeId,
    # value) om samma typ+värde finns i olika kontexter (t.ex. olika instanser av samma applikation). Behöver
    # bara användas när det finns en risk att sådana värden möts i samma mottagare. Oftast på formen
    # "lärosäte.se/applikationsinstans"
    varderymd: str = None

    # Beskrivning av taggen avsedd för mänsklig konsumtion. Inte värdebärande - varje avsändare kan egentligen
    # lägga lite vad de vill här. Mottagaren skall _inte_ agera på .name, bara på kombinationen
    # namnrymd/typnamn/varde/varderymd.
    namn: SprakhanteradText = None


@jsontype()
@dataclass(kw_only=True)
class MedGiltighetsbegransadTaggning(MedGiltighet):
    # Lista över taggar som sitter/satt/kommer sitta på posten under giltigheten.
    tagg: Tagg


@jsontype()
@dataclass(kw_only=True)
class MedTaggning:
    # Lista över taggar som sitter på posten just nu, där vi inte känner till någon historik/framtid.
    taggar: list[Tagg] = None

    # Lista över taggar som suttit/sitter/kommer att sitta på posten, där vi känner till
    # historik/framtid.
    giltighetsbegransadeTaggar: list[MedGiltighetsbegransadTaggning] = None


@jsontype()
@dataclass(kw_only=True)
class MedTyptagg:
    # En ensam tag som representerar objektets typ.
    typ: Tagg


@jsontype()
@dataclass(kw_only=True)
class Spridning:
    # En tag som beskriver ett sätt posten får spridas (t.ex. internt, intranät, extranät...)
    synlighet: Tagg

    # Om flera poster av samma typ möts i ovanstående medium (t.ex. att flera rolltilldelningar för samma
    # person är synliga på en personsida på intranätet), så sorteras de utifrån rankingvärdet. Lägst
    # värde vinner. Om flera objekt har samma ranking så väljer mottagaren godtyckligt.
    ranking: int = None


@jsontype()
@dataclass(kw_only=True)
class MedSpridning:
    # Postens synligheter, med postlokal ranking per synlighet.
    synligheter: list[Spridning] = None


@jsontype()
class LokalUtokning(dict):
    """En extension nycklas med en URI. För konsumentens avsikter finns ingen speciell betydelse i
    någon del av URI:n - den är bara ett universellt sätt att skriva en identifierare på. TOP-standarden
    säger dock att URI:n som minimum skall inehålla domännamn på den som definierar de attribut som
    ligger i respektive extension. En initial rekommendation är att lärosätena använder http://<lärosätesdomän>/TOP
    som extension-nyckel.
    """
    __json_schema__ = {
        "type": "object",
        "patternProperties": {
            "^[-_a-zA-Z0-9:/?.@]+$": {"type": "object"}
        }
    }


@jsontype()
class MedLokalUtokning:
    """Plats att lägga alla sina coola extensions på. Se Extension-typen för en beskrivning av innehållet."""
    lokalUtokning: LokalUtokning


