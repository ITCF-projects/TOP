from dataclasses import dataclass
from typing import *

from schemagen import jsontype
from top2.common import I18nText, TagsMixin, MandatoryIdMixin, ExtendableMixin

if TYPE_CHECKING:
    from top2.deployment import Deployment

@jsontype()
@dataclass(kw_only=True)
class Job(MandatoryIdMixin, TagsMixin, ExtendableMixin):
    """En viss roll - en uppsättning arbetsuppgifter och ansvar t.ex. 'Studievägledare' eller 'Rektor'.
    Personer kan agera i en roll (d.v.s. utföra de arbetsuppgifter som rollen beskriver), men rollen
    i sig kan inte utföra något. De personer som förväntas agera i en viss roll på en viss orgenhet
    har en rolltilldelning (DeploymentType) där.
    """

    # Rollens namn, t.ex. {'sv': 'Studievägledare', 'en': 'Study counsellor'}
    title: I18nText = None

    # Beskrivning av rollen, t.ex. vilka arbetsuppgifter och ansvar som ingår i den.
    description: I18nText = None

    # Rolltilldelningar för denna roll.
    deployments: "Deployment" = None
