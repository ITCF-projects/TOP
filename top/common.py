import datetime
import enum
from dataclasses import dataclass
from typing import *

"""
Doesn't yet work with dataclasses:
* When __set__ raises an error on field "a", dataclasses raises an error that field "b" doesn't exist.
* @dataclass
  class A:
      a: str = None
      a = StringProperty(...)
  dataclass considers "a" to be mandatory, in spite of being given a default value.

class StringProperty:
    def __init__(self, regexp: str):
        self.raw_regexp = regexp
        self.rexp = re.compile(regexp)

    def __set_name__(self, owner, name):
        self.name = name
        self.storage_name = "_" + name

    def __get__(self, instance, owner) -> str:
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value: str):
        if not isinstance(value, str) or not self.rexp.fullmatch(value):
            raise ValueError(f"{instance}.{self.name} value must be a string matching regexp {self.raw_regexp}")
        setattr(instance, self.storage_name, value)

    def __delete__(self, instance):
        delattr(instance, self.storage_name)
"""

class Constraint:
    pass


class Regexp(Constraint):
    def __init__(self, regexp: str):
        self.regexp = regexp


class I18nText:
    """Språkhanterad text. Nycklar är språkkod enligt RFC4646/RFC4647 (t.ex. 'en' eller 'sv'), värdet är
    texten på det språket."""
    __json_schema__ = {
        "type": "object",
        "patternProperties": {
            "^[a-z]{2,3}$": {"type": "string"}
        }
    }

# I18nText = dict[str, str]


@dataclass(kw_only=True)
class EffectiveTimePeriod:
    """En tidsperiod inom vilken ett associerat värde är giltigt. Om invalidFrom """
    validFrom: datetime.datetime
    invalidFrom: Optional[datetime.datetime]


@dataclass(kw_only=True)
class Identifier:
    """Identifierare. Om Evry i sin Primula-applikation definierar ett begrepp 'aperson_id', och Chalmers vill
    förmedla att i just vår skarpa Primula-instans har en person värdet 42 på den identifieraren, så skulle
    man t.ex. använda:
        {schemeAgencyId='evry.se/primula' schemeId='aperson_id' value='42' valueScope='chalmers.se/skarp'}
    """

    # Värdets typ. Den som förstår denna typ vet också vad man skall göra med värdet.
    schemeId: str

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


@dataclass(kw_only=True)
class MandatoryIdMixin:
    id: Identifier
    correlationIds: list[Identifier] = None
    mergedFromIds: list[Identifier] = None
    previousCorrelationIds: list[Identifier] = None


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


@dataclass(kw_only=True)
class EffectiveTimePeriodMixin:
    # Giltighetsperiod. Om denna utelämnas så känner avsändaren varken till start- eller slutdatum,
    # bara att objektet är giltigt just nu.
    effectiveTimePeriod: EffectiveTimePeriod = None

    effectiveStatus: EffectiveStatusEnum = None


@dataclass(kw_only=True)
class TagWithEffectiveTimePeriod(EffectiveTimePeriodMixin):
    tag: list[Tag]


@dataclass(kw_only=True)
class TagsMixin:
    tags: list[Tag] = None
    tagsWithEffectiveTimePeriod: list[TagWithEffectiveTimePeriod] = None


@dataclass(kw_only=True)
class TypeMixin:
    # En ensam tag som representerar objektets typ.
    type: Tag


@dataclass(kw_only=True)
class VisibilityConfigurationMixin:
    # En ensam tag som beskriver det sätt ett objekt får spridas (t.ex. internt, intranät, extranät,
    # publikationer)
    visibility: Tag = None

    # Rangordning mellan objekt av samma typ med samma spridning. I dessa lägen 'vinner' objekt med
    # lägre värde över de med högre värden. Inget värde alls räknas som oändligheten, det vill säga lägst
    # i alla rangordningar. Om flera objekt har samma rangordning väljer mottagaren godtyckligt.
    rank: int = None
