import datetime
import enum
from dataclasses import dataclass
from typing import *

from schemagen import jsontype


@jsontype
class I18nText(dict):
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
class EffectiveTimePeriod:
    """En tidsperiod inom vilken ett associerat värde är giltigt. Om invalidFrom """
    validFrom: datetime.datetime
    invalidFrom: Optional[datetime.datetime]


@jsontype()
@dataclass(kw_only=True)
class Identifier:
    """Identifierare. Om Evry i sin Primula-applikation definierar ett begrepp 'aperson_id', och Chalmers vill
    förmedla att i just vår skarpa Primula-instans har en person värdet 42 på den identifieraren, så skulle
    man t.ex. använda:
        {schemeAgencyId='evry.se/primula' schemeId='aperson_id' value='42' valueScope='chalmers.se/skarp'}
    """

    schemeId: Annotated[str, "Värdets typ. Den som förstår denna typ vet också vad man skall göra med värdet."]

    # Den entitet som definierar schemeId, eller annorlunda uttryckt den namnrymd där schemeId är definierat.
    # Ofta den leverantör och applikation ur vilket värdet har lästs, t.ex. 'evry.se/primula' eller, om
    # leverantören bara har en produkt, t.ex. 'ladok.se'. Vissa schemeId definieras i TOP-standarden,
    # dessa har schemeAgencyId='*'
    schemeAgencyId: str

    # Värde
    value: str

    # Domännamn eller liknande identifierare som ger en kontext för kombinationen (schemeAgencyId, schemeId,
    # value) om samma typ+värde finns i olika kontexter (t.ex. olika instanser av samma applikation). Behöver
    # bara användas när det finns en risk att sådana värden möts i samma mottagare. Oftast på formen
    # "lärosäte.se/applikationsinstans"
    valueScope: str = None


@jsontype()
@dataclass(kw_only=True)
class Tag:
    """En tag - en egenskap uttryckt som en boolesk variabel med ett sant värde. Dessa definieras oftast av
    lärosätet själva för att uttrycka egenskaper som 'anställningsliknande förhållande' på en person eller
    'linjeorganisation' på en organisatorisk del.
    """
    # Den entitet som definierar schemeId, eller annorlunda uttryckt den namnrymd där schemeId är definierat.
    # Taggar som definieras i standarden har '*' som schemeAgencyId.
    schemeAgencyId: str

    # Taggens namnrymd (t.ex. "organisationstyper" eller "anställningsformer")
    schemeId: str

    # Taggens värde. En avtalsperiod som representerar en fast anställning kan t.ex. vara taggad med
    # {schemeAgencyId: "*", schemeId: "anställningsform", value: "fastanställd"}
    value: str

    # Beskrivning av taggen avsedd för mänsklig konsumtion. Inte värdebärande - varje avsändare kan egentligen
    # lägga lite vad de vill här. Mottagaren skall _inte_ agera på .name, bara på .value.
    name: I18nText = None

    # Domännamn eller liknande identifierare som ger en kontext för kombinationen (schemeAgencyId, schemeId, value)
    # om samma typ+värde finns i olika kontexter (t.ex. olika instanser av samma applikation). Behöver
    # bara användas när det finns en risk att sådana värden möts i samma mottagare. Oftast på formen
    # "lärosäte.se" eller "lärosäte.se/applikationsinstans",
    valueScope: str = None


@jsontype()
@dataclass(kw_only=True)
class MandatoryIdMixin:
    id: Identifier
    correlationIds: list[Identifier] = None
    mergedFromIds: list[Identifier] = None
    previousCorrelationIds: list[Identifier] = None


@jsontype()
@dataclass(kw_only=True)
class OptionalIdMixin:
    id: Identifier = None
    correlationIds: list[Identifier] = None
    mergedFromIds: list[Identifier] = None
    previousCorrelationIds: list[Identifier] = None


class EffectiveStatusEnum(enum.Enum):
    PAST = "past"
    PRESENT = "present"
    FUTURE = "future"


@jsontype()
@dataclass(kw_only=True)
class EffectiveTimePeriodMixin:
    # Giltighetsperiod. Om denna utelämnas så känner avsändaren varken till start- eller slutdatum,
    # bara att objektet är giltigt just nu.
    effectiveTimePeriod: EffectiveTimePeriod = None

    effectiveStatus: EffectiveStatusEnum = None


@jsontype()
@dataclass(kw_only=True)
class TagWithEffectiveTimePeriod(EffectiveTimePeriodMixin):
    tag: list[Tag]


@jsontype()
@dataclass(kw_only=True)
class TagsMixin:
    tags: list[Tag] = None
    tagsWithEffectiveTimePeriod: list[TagWithEffectiveTimePeriod] = None


@jsontype()
@dataclass(kw_only=True)
class TypeMixin:
    # En ensam tag som representerar objektets typ.
    type: Tag


@jsontype()
@dataclass(kw_only=True)
class VisibilityConfigurationMixin:
    # En ensam tag som beskriver det sätt ett objekt får spridas (t.ex. internt, intranät, extranät,
    # publikationer)
    visibility: Tag = None

    # Rangordning mellan objekt av samma typ med samma spridning. I dessa lägen 'vinner' objekt med
    # lägre värde över de med högre värden. Inget värde alls räknas som oändligheten, det vill säga lägst
    # i alla rangordningar. Om flera objekt har samma rangordning väljer mottagaren godtyckligt.
    rank: int = None
