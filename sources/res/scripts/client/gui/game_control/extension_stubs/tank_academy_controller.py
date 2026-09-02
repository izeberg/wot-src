import typing, Event
from skeletons.gui.game_control import ITankAcademyController
if typing.TYPE_CHECKING:
    from typing import Optional, List, Callable
    from gui.Scaleform.daapi.view.lobby.hangar.entry_points.gf_header_widget import GFWidgetAliases
    from gui.server_events.event_items import Quest, ITankAcademyQuest, ITankAcademyGroup
    from gui.shared.gui_items import Vehicle

class TankAcademyController(ITankAcademyController):
    onStateChanged = Event.Event()
    onFinish = Event.Event()

    def __init__(self):
        ITankAcademyController.__init__(self)

    def isEnabled(self):
        return False

    def isFinished(self):
        return False

    def isActive(self):
        return False

    def isValidConfiguration(self):
        return False

    def hasUnobtainedDelayedRewards(self):
        return False

    def hasDelayedRewardToken(self, delayedRewardToken):
        return False

    def hasDelayedRewardsInQuest(self, quest):
        return False

    def isFinalQuest(self, quest):
        return False

    def getFinalQuest(self):
        return

    def getFirstQuest(self):
        return

    def isTankAcademyQuestID(self, questID):
        return False

    def getQuestByIdx(self, questIdx):
        return

    def getCompletedTankAcademyQuests(self):
        return []

    def getCompletedTankAcademyQuestsCount(self):
        return 0

    def markPostBattleAutoShowSuppressed(self, arenaUniqueID):
        pass

    def consumePostBattleAutoShowSuppressed(self, arenaUniqueID):
        return False

    def getNotCompletedTankAcademyQuests(self):
        return []

    def getTankAcademyQuestsByGroup(self, questGroup):
        return []

    def getTankAcademyQuests(self, filterFunc=None):
        return []

    def getTankAcademyQuestGroups(self, filterFunc=None):
        return []

    def getCountTankAcademyQuests(self):
        return 0

    def showAwardView(self, questsData, clientCtx=None):
        pass

    def getCurrentQuest(self):
        return

    def getCurrentQuestOrder(self):
        return

    def getQuestProgress(self, quest):
        return (0, 0)

    def getSelectedVehicle(self, delayedRewardToken):
        return

    def hasAccessToken(self):
        return False

    def getDelayedRewardCurrencyTokens(self):
        return []

    def getVehicleOfferTokensWithUnobtainedGifts(self):
        return []

    def getDelayedRewardExpirationTime(self):
        return 0

    def isDelayedRewardToken(self, token):
        return False

    def isTAOfferToken(self, token):
        return False

    def hasOfferToken(self, offerToken):
        return False

    def isDelayedRewardObtained(self, delayedRewardToken):
        return False

    def isOfferRewardObtained(self, offerToken):
        return False

    def getOfferProperties(self, offerToken):
        return {}

    def getOfferTokenByDelayedRewardCurrencyToken(self, delayedRewardCurrencyToken):
        return ''

    def getABTestConfiguration(self):
        return 'default'

    def getHangarWidgetAlias(self):
        return

    def isFirstQuestCompleted(self):
        return False