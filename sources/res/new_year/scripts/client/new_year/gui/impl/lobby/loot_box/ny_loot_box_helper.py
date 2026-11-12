import typing, BigWorld
from collections import namedtuple
from gui import SystemMessages
from gui.impl import backport
from gui.impl.auxiliary.rewards_helper import getRewardTooltipContent
from gui.impl.gen import R
from new_year.gui.impl.lobby.new_year.tooltips.ny_decoration_tooltip import NyDecorationTooltip
from new_year.gui.impl.lobby.new_year.tooltips.ny_guaranteed_reward_tooltip import NyGuaranteedRewardTooltip
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency
from shared_utils import first
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.loot_box import LootBox
MAX_PREMIUM_BOXES_TO_OPEN = 5
SpecialRewardData = namedtuple('SpecialRewardData', ('sourceName', 'congratsType',
                                                     'congratsSourceId', 'vehicleName',
                                                     'vehicleLvl', 'vehicleIsElite',
                                                     'vehicleType', 'backToSingleOpening',
                                                     'isGuaranteedReward'))

def showRestrictedSysMessage():

    def _showRestrictedSysMessage():
        SystemMessages.pushMessage(text=backport.text(R.strings.lootboxes.restrictedMessage.body()), type=SystemMessages.SM_TYPE.ErrorHeader, priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.lootboxes.restrictedMessage.header())})

    BigWorld.callback(0.0, _showRestrictedSysMessage)


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def isLootboxValid(boxType, itemsCache=None):
    return any(box.getType() == boxType for box in itemsCache.items.tokens.getLootBoxes().itervalues())


def getTooltipContent(event, storedTooltipData):
    tooltipContent = getRewardTooltipContent(event, storedTooltipData)
    if tooltipContent is not None:
        return tooltipContent
    else:
        tooltipContentRes = R.views.new_year.lobby.new_year.tooltips
        if event.contentID == tooltipContentRes.NyDecorationTooltip():
            toyID = event.getArgument('toyID')
            return NyDecorationTooltip(toyID, isToyIconEnabled=False)
        if event.contentID == R.views.new_year.lobby.new_year.tooltips.NyGuaranteedRewardTooltip():
            return NyGuaranteedRewardTooltip()
        return


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getOpenedLootBoxFromRewards(resultData, itemsCache=None):
    openedLootBoxes = resultData.get('extData', {}).get('openedLootBoxes', {})
    if not openedLootBoxes:
        return None
    else:
        boxID = first(openedLootBoxes.keys())
        return itemsCache.items.tokens.getLootBoxByID(boxID)