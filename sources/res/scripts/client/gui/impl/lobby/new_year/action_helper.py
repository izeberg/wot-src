import typing
from gui.impl.gen.view_models.views.lobby.new_year.ny_constants import ButtonActionType
from gui.impl.lobby.new_year.states import GladeTownState, GuestDState, GuestCState, MarketplaceState, GiftMachineState, RewardsState
from gui.impl.new_year.new_year_helper import ADDITIONAL_BONUS_NAME_GETTERS
from items.components.ny_constants import NyATMReward
if typing.TYPE_CHECKING:
    from gui.server_events.bonuses import SimpleBonus
_FIRST_LVL = 1
ACTION_TO_STATES = {ButtonActionType.TOEVENT: (
                            GladeTownState, True), 
   ButtonActionType.TOGUESTD: (
                             GuestDState, True), 
   ButtonActionType.TOGUESTC: (
                             GuestCState, True), 
   ButtonActionType.TOMARKERTPLACE: (
                                   MarketplaceState, True), 
   ButtonActionType.TOGIFTMACHINE: (
                                  GiftMachineState, True), 
   ButtonActionType.TOREWARDS: (
                              RewardsState, False)}
BONUS_NAME_TO_BUTTON_ACTION = {NyATMReward.DOG: ButtonActionType.TOGUESTD, 
   NyATMReward.CAT: ButtonActionType.TOGUESTC, 
   NyATMReward.MARKETPLACE: ButtonActionType.TOMARKERTPLACE}

def getBonusesNames(bonuses):
    names = []
    for b in bonuses:
        bonusName = b.getName()
        getAdditionalName = ADDITIONAL_BONUS_NAME_GETTERS.get(bonusName)
        if getAdditionalName is not None:
            bonusName = getAdditionalName(b)
        names.append(bonusName)

    return names


def getButtonAction(level, bonuses):
    if level == _FIRST_LVL:
        return ButtonActionType.TOEVENT
    bonusesNames = getBonusesNames(bonuses)
    for bonusName, action in BONUS_NAME_TO_BUTTON_ACTION.iteritems():
        if bonusName in bonusesNames:
            return action

    return ButtonActionType.UNDEFINED