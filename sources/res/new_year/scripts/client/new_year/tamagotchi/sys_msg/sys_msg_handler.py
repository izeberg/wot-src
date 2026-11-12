from gui.impl import backport
from gui.impl.gen import R
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency, int2roman
from helpers.events_handler import EventsHandler
from helpers.time_utils import ONE_MINUTE, getServerUTCTime
from messenger import MessengerEntry
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from new_year.ny_constants import NY_CUMULATIVE_LEADERBOARD_SEASON_ID
from new_year.gui.shared.formatters import formatPurchaseItems, formatPurchasedItems, formatActivatedItem
from new_year.gui.impl.new_year.new_year_bonus_packer import getNewYearBonusPacker
from new_year.skeletons.new_year import ITamagotchiDataProvider
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.new_year_main_widget_model import State
from new_year_common.items.components.ny_constants import YEARS_INFO
from shared_utils import findFirst
from gui.SystemMessages import SM_TYPE
from gui import SystemMessages
MINUTES_TO_SHOW_NOTIF = {5: False, 15: False, 30: False, 60: False}
START_SHOW_LEADERBOARD_NOTIF_END = 60

class TamagotchiSysMsgHandler(EventsHandler):
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    _systemMessages = MessengerEntry.g_instance.protos.BW.serviceChannel
    __slots__ = ('__isFirstEntry', )

    def __init__(self):
        self.__isFirstEntry = True

    def init(self):
        self._subscribe()

    def fini(self):
        self.__isFirstEntry = True
        self._unsubscribe()

    def _getEvents(self):
        return (
         (
          self._dataProvider.onItemsActivated, self._onItemsActivated),
         (
          self._dataProvider.onItemsPurchased, self._onItemsPurchased),
         (
          self._dataProvider.onSimulationEnd, self.__onLeaderboardUpdate),
         (
          self._dataProvider.onSimulationEnd, self.__onCheckTamagotchiState),
         (
          self._dataProvider.onSeasonEnded, self.__onSeasonEnded))

    @classmethod
    def pushClientSysMessage(cls, message, msgType, msgName, priority=None, messageData=None, savedData=None):
        return cls._systemMessages.pushClientMessage(message, msgType, isAlert=False, auxData=[msgName, priority, messageData, savedData])

    @classmethod
    def showSkipMsg(cls):
        cls.pushClientSysMessage(backport.text(R.strings.ny.notification.tamagotchi.tutor.skip.msg()), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_TUTORIAL, msgName='NYTamagotchiTutorSkip', priority=NotificationPriorityLevel.LOW)

    def _onItemsActivated(self, isSuccess, itemId, count, isRecalculation):
        if isRecalculation:
            return
        if isSuccess:
            itemName, item = findFirst(lambda (name, indicator): indicator.item.id == itemId, self._dataProvider.config.indicators.iteritems())
            extraScalePoints = int(item.item.scalePoint * count)
            potentialLoyaltyPoints = 0 if self._dataProvider.isLeaderboardFinished else int(item.item.leaderboardPoint * count)
            self.pushClientSysMessage(formatActivatedItem(itemName, count, extraScalePoints, potentialLoyaltyPoints), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_TUTORIAL, msgName='NYTamagotchiItemsActivated', priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.racoon.activated.header.dyn(itemName)())})
        else:
            SystemMessages.pushMessage(backport.text(R.strings.ny.notification.racoon.activated.error()), type=SM_TYPE.ErrorSimple, priority=NotificationPriorityLevel.MEDIUM)
            if self._dataProvider.isOnboarding:
                self.pushClientSysMessage(backport.text(R.strings.ny.notification.tamagotchi.tutor.error.msg()), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_TUTORIAL, msgName='NYTamagotchiTutorError', priority=NotificationPriorityLevel.MEDIUM)

    def _onItemsPurchased(self, isSuccess, itemsDict):
        if isSuccess:
            itemsDictByName = {}
            for name, indicator in self._dataProvider.config.indicators.iteritems():
                if indicator.item.id not in itemsDict:
                    continue
                itemsDictByName[name] = itemsDict[indicator.item.id]

            self.pushClientSysMessage(formatPurchasedItems(itemsDictByName), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_TUTORIAL, msgName='NYTamagotchiPurchased', priority=NotificationPriorityLevel.MEDIUM)
        else:
            SystemMessages.pushMessage(text=backport.text(R.strings.ny.notification.racoon.purchased.error.text()), type=SM_TYPE.ErrorSimple, priority=NotificationPriorityLevel.MEDIUM)

    def __onCheckTamagotchiState(self):
        self._dataProvider.onSimulationEnd -= self.__onCheckTamagotchiState
        petState = self._dataProvider.playerInfo.state
        if self._dataProvider.isOnboarding or petState == State.PAUSE:
            return
        if petState != State.FUN.value:
            self.pushClientSysMessage(backport.text(R.strings.ny.notification.tamagotchi.check_state.text()), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_TUTORIAL, msgName='NYTamagotchiCheckState', priority=NotificationPriorityLevel.MEDIUM)

    def __onLeaderboardUpdate(self):
        if not self._dataProvider.isValidConfig:
            return
        else:
            currentSeason = self._dataProvider.config.currentSeason
            if currentSeason is None:
                return
            endTime = int(round((currentSeason.endTime - getServerUTCTime()) / ONE_MINUTE))
            seasonId = currentSeason.id
            if endTime > START_SHOW_LEADERBOARD_NOTIF_END:
                for time, isShowed in MINUTES_TO_SHOW_NOTIF.items():
                    MINUTES_TO_SHOW_NOTIF[time] = False

                return
            if self.__isFirstEntry:
                self.pushEndTimeMessage(seasonId, endTime)
                self.__isFirstEntry = False
                return
            for time, isShowed in MINUTES_TO_SHOW_NOTIF.items():
                if endTime == time and not isShowed:
                    MINUTES_TO_SHOW_NOTIF[time] = True
                    self.pushEndTimeMessage(seasonId, time)

            return

    def __onSeasonEnded(self, seasonId):
        if not self._dataProvider.raccoonState:
            return
        isFinalSeason = seasonId == NY_CUMULATIVE_LEADERBOARD_SEASON_ID
        self.sendSeasonEndNotification(seasonId, isFinalSeason)

    @classmethod
    def pushEndTimeMessage(cls, seasonId, endTime):
        if endTime < 0:
            return
        timeLeftDyn = R.strings.ny.notification.leaderboard.timeLeft
        if endTime == 0:
            text = backport.text(timeLeftDyn.lessOneMin(), seasonId=int2roman(seasonId))
        else:
            text = backport.ntext(timeLeftDyn.minutes(), endTime, minutes=endTime, seasonId=int2roman(seasonId))
        SystemMessages.pushMessage(text, type=SM_TYPE.InformationHeader, priority=NotificationPriorityLevel.HIGH, messageData={'header': backport.text(R.strings.ny.notification.leaderboard.header())})

    @classmethod
    def sendRewardNotification(cls, rewards, seasonId, isFinalSeason=False):
        rewardsText = formatPurchaseItems(rewards, getNewYearBonusPacker())
        leaderboardReward = R.strings.ny.notification.leaderboard.reward
        description = leaderboardReward.finalDescription() if isFinalSeason else leaderboardReward.description()
        SystemMessages.pushMessage(text=backport.text(description, seasonId=seasonId, rewards=rewardsText), type=SM_TYPE.InformationHeader, priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(leaderboardReward.title())})

    @classmethod
    def sendSeasonEndNotification(cls, seasonId, isFinalSeason=False):
        leaderboard = R.strings.ny.notification.leaderboard
        description = leaderboard.finalEnd() if isFinalSeason else leaderboard.seasonId.end()
        SystemMessages.pushMessage(text=backport.text(description, seasonId=seasonId), type=SM_TYPE.Information, priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.header(), year=YEARS_INFO.CURRENT_YEAR_FULL)})

    @classmethod
    def sendLeaderboardNotAvailableMessage(cls):
        SystemMessages.pushMessage(text=backport.text(R.strings.ny.notification.leaderboard.unavailable()), type=SM_TYPE.ErrorHeader, priority=NotificationPriorityLevel.HIGH, messageData={'header': backport.text(R.strings.ny.notification.leaderboard.header())})

    @classmethod
    def sendRaidStartError(cls, isNotEnoughResources):
        text = R.strings.ny.notification.racoon.raid.start.errorResources() if isNotEnoughResources else R.strings.ny.notification.racoon.raid.start.error()
        SystemMessages.pushMessage(backport.text(text), type=SM_TYPE.ErrorSimple, priority=NotificationPriorityLevel.MEDIUM)

    @classmethod
    def sendRaidStarted(cls):
        cls.pushClientSysMessage(backport.text(R.strings.ny.notification.racoon.raid.start.text()), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_RAID_REWARDS, msgName='NYRaidStarted', priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.racoon.raid.start.header())})

    @classmethod
    def sendRaidFinished(cls):
        cls.pushClientSysMessage(backport.text(R.strings.ny.notification.racoon.raid.end.text()), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_RAID_REWARDS, msgName='NYRaidFinished', priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.racoon.raid.end.header())})

    @classmethod
    def sendRaidRewardError(cls):
        SystemMessages.pushMessage(backport.text(R.strings.ny.notification.racoon.raid.reward.error()), type=SM_TYPE.ErrorSimple, priority=NotificationPriorityLevel.MEDIUM)

    @classmethod
    def sendRaidRewardsAutoOpen(cls, rewardsText):
        cls.pushClientSysMessage(rewardsText, msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_RAID_REWARDS, msgName='NYRaccoonRaidRewardsAutoOpen', priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.racoon.raid.rewards.autoOpen.header())})

    @classmethod
    def sendRaidRewardsOpened(cls, rewardsText):
        cls.pushClientSysMessage(rewardsText, msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_RAID_REWARDS, msgName='NYRaccoonRaidRewardsOpened', priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.racoon.raid.rewards.opened.header())})

    @classmethod
    def sendRaidDisabled(cls):
        if not cls._dataProvider.isTamagotchiRaidViewEnabled:
            return
        cls.pushClientSysMessage(backport.text(R.strings.ny.notification.racoon.raid.disabled.text()), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_RAID_REWARDS, msgName='NYRaidDisabled', priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.racoon.raid.disabled.header())})

    @classmethod
    def sendRaidEnabled(cls):
        if not cls._dataProvider.isTamagotchiRaidViewEnabled:
            return
        cls.pushClientSysMessage(backport.text(R.strings.ny.notification.racoon.raid.enabled.text()), msgType=SCH_CLIENT_MSG_TYPE.NY_TAMAGOTCHI_RAID_REWARDS, msgName='NYRaidEnabled', priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.racoon.raid.enabled.header())})

    @classmethod
    def sendRaidAccelerationError(cls):
        SystemMessages.pushMessage(backport.text(R.strings.ny.notification.racoon.raid.acceleration.error.text()), type=SM_TYPE.ErrorSimple, priority=NotificationPriorityLevel.MEDIUM)