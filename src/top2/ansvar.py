from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Tagg, Taggning, FrivilligIdentifiering, Giltighet, LokalUtokning

if TYPE_CHECKING:
    from top2.person import Person
    from top2.rolltilldelning import Rolltilldelning
    from top2.organisationsdel import Organisationsdel


@jsontype()
@dataclass(kw_only=True)
class Organisationsdelsansvar:
    """Ansvar för viss orgenhet, antingen tilldelat personligen eller via en rolltilldelning.
    """

    # Identifiering av ansvaret.
    identifiering: FrivilligIdentifiering = None

    # Giltighet för detta ansvar.
    giltighet: Giltighet = None

    # Taggning av ansvaret.
    taggning: Taggning = None

    # Lokala utökningar.
    lokalUtokning: LokalUtokning = None

    # Ansvarstyp(er) (chef, ekonomiskt ansvarig, arbetsledare...)
    typ: Tagg

    # Den organisation för vilken ansvaret gäller.
    organisationsdel: "Organisationsdel" = None

    # Rolltilldelning(ar) via vilken ansvaret tilldelats (t.ex. tilldelning av chefsroll)
    viaRolltilldelningar: "list[Rolltilldelning]" = None

    # Individ(er) som fått ansvaret personligen tilldelat.
    direktUtpekade: "list[Person]" = None


@jsontype()
@dataclass(kw_only=True)
class Rolltilldelningsansvar:
    """Ansvar för person som har viss rolltilldelning, t.ex. att vara handledare för en viss praktikant.
    """

    # Identifiering av ansvaret.
    identifiering: FrivilligIdentifiering = None

    # Giltighet för detta ansvar.
    giltighet: Giltighet = None

    # Taggning av ansvaret.
    taggning: Taggning = None

    # Lokala utökningar.
    lokalUtokning: LokalUtokning = None

    # Ansvarstyp(er) (arbetsledare, handledare...)
    typ: Tagg

    # Den person som har ansvaret (t.ex. handledaren).
    ansvarig: "Person" = None

    # Rolltilldelningen som responsiblePerson ansvarar för (t.ex. rolltilldelningen som säger att
    # någon är praktikant).
    rolltilldelning: "Rolltilldelning" = None


@jsontype()
@dataclass(kw_only=True)
class BeraknatAnsvar:
    """Färdigberäknat ansvar mellan två personer, där den ena ('responsiblePerson' har ansvar av viss
    typ för en annan person ('affectedPerson').
    """

    # Giltighet för detta ansvar.
    giltighet: Giltighet = None

    # Taggning av ansvaret.
    taggning: Taggning = None

    # Lokala utökningar.
    lokalUtokning: LokalUtokning = None

    # Ansvarstyp (chef, ekonomiskt ansvarig, arbetsledare...)
    typ: Tagg

    # Den person som har ansvaret (t.ex. arbetsledaren).
    ansvarig: "Person" = None

    # Den person som ansvaret gäller för (t.ex. den arbetsledde).
    berord: "Person" = None
