from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import MedTaggning, MedObligatoriskIdentifierare, MedGiltighet, MedLokalUtokning

if TYPE_CHECKING:
    from top2.roll import Roll
    from top2.anknytningsavtal import Anknytningsavtal
    from top2.organisationsdel import Organisationsdel, Servicefunktion
    from top2.ersattningar import LopandeErsattning, Engangsersattning
    from top2.kommunikation import Kommunikation
    from top2.omfattningsperiod import Omfattningsperiod
    from top2.ansvar import Rolltilldelningsansvar, Organisationsdelsansvar


# personfunktion

@jsontype()
@dataclass(kw_only=True)
class Rolltilldelning(MedObligatoriskIdentifierare, MedGiltighet, MedTaggning, MedLokalUtokning):
    """En rolltilldelning säger att en person förväntas agera i en viss roll för en viss del av organisationen
    under viss tid. Förhoppningsvis har personen också tilldelats möjligheten att uppfylla de ansvar som rollen
    medför - eller så används Rolltilldelningen som bas för att automatiskt utdela sådana behörigheter.

    Det är rekommenderat (men inte tvingande) att peka ut det anknytningsavtal inom vilket denna rolltilldelning
    skett. Många personer agerar i flera olika roller på ett lärosäte i kontexten av t.ex. en anställning, och
    det ger tydlighet att peka ut den kontexten. Om ett avtal pekas ut, så begränsas rolltilldelningens
    giltighet både av sin egen giltighet men även av giltigheten på det utpekade anknytningsavtalet.
    """

    # Det anknytningsavtal som denna rolltilldelning detaljerar.
    # Reverse: Anknytningsavtal.rolltilldelningar
    anknyntningsavtal: "Anknytningsavtal" = None

    # Den del av organisationen där personen tilldelats rollen.
    organisationsdel: "Organisationsdel" = None

    # Kommunikationsvägar till personen i kontexten av denna rolltilldelning.
    kommunikationsvagar: "Kommunikation" = None

    # Den roll som personen tilldelas.
    roll: "Roll" = None

    # Omfattning(ar) för denna rolltilldelning.
    onfattningsperioder: "list[Omfattningsperiod]" = None

    # Lönetillägg eller andra extra ersättningar som personen får för denna rolltilldelning. Kan vara
    # flera, och kan variera under giltighetstiden. Lön läggs i avtalsperioden.
    lopandeErsattningsperioder: "list[LopandeErsattning]" = None

    # Engångsersättningar för denna rolltilldelning.
    engangsersattningar: "list[Engangsersattning]" = None

    # De ansvar som denna rolltilldelning medför (t.ex. linjechefsansvar för en orgenhet tilldelat av en
    # rolltilldelning som enhetschef. Andra änden av OrganizationResponsibility.deployment.
    ansvarsperioder: "list[Organisationsdelsansvar]" = None

    # Personliga ansvar tilldelade någon annan för denna rolltilldelning (t.ex. handledarskap för en
    # rolltilldelning som praktikant). Andra änden av DeploymentResponsibility.deployment.
    ansvarsperioderForTilldelningen: "list[Rolltilldelningsansvar]" = None

    # De servicefunktioner (om några) som bemannas via denna rolltilldelning. En specifik rolltilldelning
    # som studievägledare kan t.ex. innebära att man bemannar en studentmottagning.
    bemannarServicefunktioner: "list[Servicefunktion]" = None
