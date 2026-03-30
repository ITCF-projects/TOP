from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import SprakhanteradText, Taggning, Identifiering, LokalUtokning

if TYPE_CHECKING:
    from top2.rolltilldelning import Rolltilldelning

@jsontype()
@dataclass(kw_only=True)
class Roll:
    """En viss roll - en uppsättning arbetsuppgifter och ansvar t.ex. 'Studievägledare' eller 'Rektor'.
    Personer kan agera i en roll (d.v.s. utföra de arbetsuppgifter som rollen beskriver), men rollen
    i sig kan inte utföra något. De personer som förväntas agera i en viss roll på en viss orgenhet
    har en rolltilldelning där.
    """

    # Identifiering av rollen.
    identifiering: Identifiering

    # Taggning av rollen.
    taggning: Taggning = None

    # Lokala utökningar.
    lokalUtokning: LokalUtokning = None

    # Rollens namn, t.ex. {'sv': 'Studievägledare', 'en': 'Study counsellor'}
    namn: SprakhanteradText = None

    # Beskrivning av rollen, t.ex. vilka arbetsuppgifter och ansvar som ingår i den.
    beskrivning: SprakhanteradText = None

    # Rolltilldelningar för denna roll.
    rolltilldelningar: "Rolltilldelning" = None
