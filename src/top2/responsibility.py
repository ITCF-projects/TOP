from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import Tag, TagsMixin, OptionalIdMixin, EffectiveTimePeriodMixin, ExtendableMixin

if TYPE_CHECKING:
    from top2.person import Person
    from top2.deployment import Deployment
    from top2.organization import Organization


@jsontype()
@dataclass(kw_only=True)
class OrganizationResponsibility(EffectiveTimePeriodMixin, TagsMixin, OptionalIdMixin, ExtendableMixin):
    """Ansvar för viss orgenhet, antingen tilldelat personligen eller via en rolltilldelning.
    """

    # Ansvarstyp(er) (chef, ekonomiskt ansvarig, arbetsledare...)
    type: Tag

    # Den organisation för vilken ansvaret gäller.
    organization: "Organization" = None

    # Rolltilldelning(ar) via vilken ansvaret tilldelats (t.ex. tilldelning av chefsroll)
    deployments: "list[Deployment]" = None

    # Individ(er) som fått ansvaret personligen tilldelat.
    individual: "list[Person]" = None


@jsontype()
@dataclass(kw_only=True)
class DeploymentResponsibility(EffectiveTimePeriodMixin, TagsMixin, OptionalIdMixin, ExtendableMixin):
    """Ansvar för person som har viss rolltilldelning, t.ex. att vara handledare för en viss praktikant.
    """
    # Ansvarstyp(er) (arbetsledare, handledare...)
    type: Tag

    # Den person som har ansvaret (t.ex. handledaren).
    responsiblePerson: "Person" = None

    # Rolltilldelningen som responsiblePerson ansvarar för (t.ex. rolltilldelningen som säger att
    # någon är praktikant).
    deployment: "Deployment" = None


@jsontype()
@dataclass(kw_only=True)
class CalculatedResponsibility(EffectiveTimePeriodMixin, TagsMixin, ExtendableMixin):
    desc = (
        "Färdigberäknat ansvar mellan två personer, där den ena ('responsiblePerson' har ansvar av viss "
        "typ för en annan person ('affectedPerson')."
    )

    # Ansvarstyp (chef, ekonomiskt ansvarig, arbetsledare...)
    type: Tag

    # Den person som har ansvaret (t.ex. arbetsledaren).
    responsiblePerson: "Person" = None

    # Den person som ansvaret gäller för (t.ex. den arbetsledde).
    affectedPerson: "Person" = None
