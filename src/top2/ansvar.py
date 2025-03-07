from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Tagg, MedTaggning, MedFrivilligIdentifierare, MedGiltighet, MedLokalUtokning

if TYPE_CHECKING:
    from top2.person import Person
    from top2.rolltilldelning import Rolltilldelning
    from top2.organisationsdel import Organisationsdel


@jsontype()
@dataclass(kw_only=True)
class Organisationsdelsansvar(MedGiltighet, MedTaggning, MedFrivilligIdentifierare, MedLokalUtokning):
    """Ansvar för viss orgenhet, antingen tilldelat personligen eller via en rolltilldelning.
    """

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
class Rolltilldelningsansvar(MedGiltighet, MedTaggning, MedFrivilligIdentifierare, MedLokalUtokning):
    """Ansvar för person som har viss rolltilldelning, t.ex. att vara handledare för en viss praktikant.
    """
    # Ansvarstyp(er) (arbetsledare, handledare...)
    typ: Tagg

    # Den person som har ansvaret (t.ex. handledaren).
    ansvarig: "Person" = None

    # Rolltilldelningen som responsiblePerson ansvarar för (t.ex. rolltilldelningen som säger att
    # någon är praktikant).
    rolltilldelning: "Rolltilldelning" = None


@jsontype()
@dataclass(kw_only=True)
class BeraknatAnsvar(MedGiltighet, MedTaggning, MedLokalUtokning):
    desc = (
        "Färdigberäknat ansvar mellan två personer, där den ena ('responsiblePerson' har ansvar av viss "
        "typ för en annan person ('affectedPerson')."
    )

    # Ansvarstyp (chef, ekonomiskt ansvarig, arbetsledare...)
    typ: Tagg

    # Den person som har ansvaret (t.ex. arbetsledaren).
    ansvarig: "Person" = None

    # Den person som ansvaret gäller för (t.ex. den arbetsledde).
    berord: "Person" = None
