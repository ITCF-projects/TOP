from dataclasses import dataclass
import datetime
from typing import *

from schemagen import jsontype
from top2.common import Identifierare, MedObligatoriskIdentifierare, MedFrivilligIdentifierare, MedGiltighet, MedTaggning, MedLokalUtokning, Tagg

if TYPE_CHECKING:
    from top2.rolltilldelning import Rolltilldelning
    from top2.kommunikation import Kommunikation
    from top2.ansvar import BeraknatAnsvar, Organisationsdelsansvar
    from top2.anknytningsavtal import Anknytningsavtal


@jsontype()
@dataclass(kw_only=True)
class Passerbehorighet(MedGiltighet, MedLokalUtokning):
    """En passerbehörighet, identifierad av ett för mottagaren meningsfullt ID. Tilldelningen av behörigheten
    görs till en person eller ett passerkort."""

    # Behörighetens ID (inte resursen behörigheten gäller för).
    postid: Identifierare
    # ID på den resurs som behörigheten gäller för (inte behörighetens egna ID om ett sådant finns).
    resursId: Identifierare
    # De person(er) som tilldelats behörigheten.
    tilldeladPersoner: "list[Person]"
    # De passerkort som tilldelats behörigheten.
    tilldeladPasserkort: "list[Passerkort]"


@jsontype()
@dataclass(kw_only=True)
class Passerkort(MedFrivilligIdentifierare, MedGiltighet, MedLokalUtokning):
    """Ett passerkort och de behörigheter detta kort skall vara försedda med. Om behörigheter knyts till
    personen snarare än till dennes kort så används istället PersonType.accessPrivileges. Notera att
    giltighetstider i detta objekt rör passerkortet i sig, behörigheterna har egna giltighetstider.
    """
    # Kortets id.
    postid: Identifierare

    # Behörigheter som kortet skall förknippas med (behörigheter för individ läggs i Person.accessPrivileges)
    passerbehorigheter: list[Passerbehorighet] = None


@jsontype()
@dataclass(kw_only=True)
class Bisyssla:
    # BEMANNINGAR är alla formulär
    # BEMANNINGSFALT är alla fälten med namn och kopplat till id i bemanningar
    # BISYSSLA-tabellerna är kopior av BEMANNING-tabellernas innehåll för just bisysslor.
    # För typ combobox är BUFFER kommaseparerade värden...
    # GBEMANNINGSARENDE / GBEMANNINGSARENDEFALT.arende_id aanstallning_id/aperson_id kopplar till individ
    foretag: str
    organisationsnummer: str
    forvantadFortsattning: str  # t.ex. "<1 år"
    person: "Person" = None


@jsontype()
@dataclass(kw_only=True)
class Person(MedObligatoriskIdentifierare, MedTaggning, MedLokalUtokning, MedGiltighet):
    """En person av kött och blod. Datat är så normaliserat som avsändaren klarar av - i normalfallet
    motsvaras varje fysisk person av som mest _en_ datapost. Ingen avsändare skall t.ex. skicka flera
    personposter med olika ID:n när en person har flera parallella anställningar.

    Personobjekt innehåller vissa rena individegenskaper, t.ex. namn och diverse identifierare
    (t.ex. personnummer). Kontaktinformation till personen, både i professionell och privat kontext
    kan också finnas med här. Den främsta informationen framkommer dock i hur personen hänger ihop
    med lärosätets organisation, vilket beskrivs av _anknytningsavtal_ och _rolltilldelningar_.
    """

    # APERSON fornamn/efternamn

    # Förnamn (alla)
    fornamn: str = None

    # Tilltalsnamn. Om vi har alla namn så skickas samtliga i fornamn, och tilltalsnamnet här. Får
    # vara ett smeknamn.
    tilltalsnamn: str = None

    # Efternamn (inklusive eventuella mellannamn).
    efternamn: str = None

    # Färdigformatterat namn, med stora/små bokstäver (t.ex. "Stefan Ponzi von Tillman och Ovar mcPherson"
    formatteratNamn: str = None

    # aperson.adress_id -> primulaadress
    # Kommunikationsvägar till personen som individ
    kommunikationsvagar: "Kommunikation" = None

    # Accessbehörigheter som personen skall ha, oavsett vilket passerkort hen använder.
    passerbehorigheter: list[Passerbehorighet] = None

    # Passerkort inklusive eventuella behörigheter för kortet i sig snarare än för personen.
    passerkort: list[Passerkort] = None

    # Anknytningsavtal för denna person.
    anknytningsavtal: "list[Anknytningsavtal]" = None

    # Rolltilldelningar för denna person.
    rolltilldelningar: "list[Rolltilldelning]" = None

    avliden: bool = None

    # personkompetens.kompskikt_id -> kompskikt (t.ex. docent)
    # Uppnådd utbildningsnivå (t.ex. vid rekrytering)
    utbildningsniva: Tagg = None

    # personkompetens.kompskikt_id -> kompskikt (t.ex. docent)
    # Är du inte docent, pojk?!
    docentLarosate: str = None

    # personkompetens.kompinriktning_id -> kompinriktning.text
    docentAmne: str = None

    # aperson
    # Statlig anställning fortsätter när du byter lärosäte t.ex.
    statligAnstallningFrom: datetime.date = None

    # aanstallning.amnestillhor -> amnestillhor.kod/text1
    # Forskningsämnen behöver rapporteras som ämneskoder för jämförelser mellan lärosäten.
    # Lista på "SCB forskningsämnen"
    # LiU använder 3 första (101 Matematik) andra alla 5.
    forskningsamne: str = None
    forskningsamneSCB: str = None

    # aperson.arbetsstallenr_id -> arbetsstallekod
    # Arbetsställe-ID fås från och rapporteras till SCB.
    arbetsstalleID: int = None

    # aperson.arbetsstallenr_id -> arbetsstallekod
    # Arbetsplatsadress skall rapporteras till Skatteverket kräver gatuadress eller GPS-koordinat.
    arbetsplatsAdress: str = None

    # Personligt tilldelade ansvar.
    personligaAnsvar: "list[Organisationsdelsansvar]" = None

    # Alla ansvar denna person kan beräknas ha för andra personer.
    beraknadeAnsvar: "list[BeraknatAnsvar]" = None

    # Alla ansvar andra personer kan beräknas ha över denna person",
    omfattasAvAnsvar: "list[BeraknatAnsvar]" = None

    # Registrerade bisysslor
    bisysslor: list[Bisyssla] = None
