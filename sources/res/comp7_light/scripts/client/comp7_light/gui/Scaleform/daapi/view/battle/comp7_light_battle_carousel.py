from account_helpers.AccountSettings import COMP7_LIGHT_CAROUSEL_FILTER_1, COMP7_LIGHT_CAROUSEL_FILTER_2
from account_helpers.AccountSettings import COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1
from comp7_core.gui.Scaleform.daapi.view.battle.battle_carousel import PrebattleTankCarousel

class Comp7LightPrebattleTankCarousel(PrebattleTankCarousel):
    _FILTER_SERVER_SECTIONS = (
     COMP7_LIGHT_CAROUSEL_FILTER_1, COMP7_LIGHT_CAROUSEL_FILTER_2)
    _FILTER_CLIENT_SECTIONS = (COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1,)