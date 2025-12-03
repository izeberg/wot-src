import logging
from collections import OrderedDict
import typing, nations
from Event import Event, EventManager
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS
from frameworks.state_machine import StringEvent
from gui import GUI_NATIONS
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.lock_overlays import lockNotificationManager
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.shared.utils.scheduled_notifications import Notifiable, SimpleNotifier
from helpers import dependency, time_utils
from helpers.events_handler import EventsHandler
from helpers.server_settings import serverSettingsChangeListener
from one_time_gift.gui.shared.wdr_reward_helper import WDRRewardHelper
from shared_utils import findFirst, nextTick
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from one_time_gift.gui.gui_constants import OTG_LOCK_SOURCE_NAME
from one_time_gift.gui.impl.lobby.user_missions import getOneTimeGiftEventBanner
from one_time_gift.gui.shared.lock_overlays import lockAchievementsEarning, lockSteamShade
from one_time_gift.gui.state_machine import OTGEvent, OneTimeGiftStateMachine
from one_time_gift.helpers.server_settings import OneTimeGiftConfig
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController
from one_time_gift_common import one_time_gift_token
from one_time_gift_common.one_time_gift_branches_config import getOneTimeGiftBranchesCfg
from one_time_gift_common.one_time_gift_constants import MAX_OTG_VEH_LEVEL, OTG_ERROR_CODES, OTG_GAME_PARAMS_KEY, BranchListType, TechTreeBranch
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, List, Optional
    T_PROCESSOR_CALLBACK = Callable[([bool], None)]
_logger = logging.getLogger(__name__)
TRAINING_FLAGS = FUNCTIONAL_FLAG.TRAINING | FUNCTIONAL_FLAG.EPIC_TRAINING

class OneTimeGiftController(Notifiable, IOneTimeGiftController, IGlobalListener, EventsHandler):
    __itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(OneTimeGiftController, self).__init__()
        self.__eventsManager = EventManager()
        self.onEntryPointUpdated = Event(self.__eventsManager)
        self.onPlayerOTGStatusChanged = Event(self.__eventsManager)
        self.onSettingsChanged = Event(self.__eventsManager)
        self.__serverSettings = None
        self.__oneTimeGiftSettings = None
        self.__stateMachine = None
        self.__isEntryPointActive = True
        self.__branchesConfig = self.__readBranchesFromConfig()
        self.__wdrHelper = None
        _logger.debug('OneTimeGift: branches config: %s', self.__branchesConfig)
        self.__branchSets = None
        return

    @property
    def isEntryPointEnabled(self):
        return self.isActive() and (not self.areBaseRewardsReceived() or not self.areWDRRewardsReceived())

    @property
    def canReceiveBaseOTGRewards(self):
        return self.isActive() and not self.areBaseRewardsReceived()

    @property
    def isEntryPointActive(self):
        if self.prbEntity and (self.prbEntity.isInQueue() or self.prbEntity.getModeFlags() & TRAINING_FLAGS):
            return False
        if self.prbDispatcher and self.prbDispatcher.getFunctionalState().isInUnit():
            if self.prbEntity and self.prbEntity.getPlayerInfo().isReady:
                return False
        return True

    @property
    def introShown(self):
        return self.__settingsCore.serverSettings.getUIStorage2().get(UI_STORAGE_KEYS.ONE_TIME_GIFT_INTRO_SHOWN)

    @introShown.setter
    def introShown(self, value):
        self.__settingsCore.serverSettings.saveInUIStorage2({UI_STORAGE_KEYS.ONE_TIME_GIFT_INTRO_SHOWN: value})

    def init(self):
        super(OneTimeGiftController, self).init()
        self.__stateMachine = OneTimeGiftStateMachine()
        self.__wdrHelper = WDRRewardHelper()
        g_clientUpdateManager.addCallbacks({'tokens': self.__onTokensUpdated})
        g_techTreeDP.load()
        self.addNotificator(SimpleNotifier(self.__getEntryPointTimerDelta, self.__timerUpdate))
        _logger.debug('OneTimeGiftController::init')

    def fini(self):
        self._unsubscribe()
        self.stopGlobalListening()
        self.__eventsManager.clear()
        self.__wdrHelper = None
        if self.__stateMachine is not None:
            self.__stateMachine.stop()
            self.__stateMachine = None
        self.__branchesConfig = None
        self.__branchSets = None
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.clearNotification()
        self.__serverSettings = None
        self.__oneTimeGiftSettings = None
        super(OneTimeGiftController, self).fini()
        return

    def onAccountBecomePlayer(self):
        self.__onServerSettingsChanged(self.__lobbyContext.getServerSettings())
        super(OneTimeGiftController, self).onAccountBecomePlayer()

    def onAccountBecomeNonPlayer(self):
        if self.__stateMachine is not None and self.__stateMachine.isRunning():
            self.__stateMachine.stop()
        self._unsubscribe()
        self.stopGlobalListening()
        return

    def onLobbyInited(self, event):
        self._subscribe()
        self.__startStateMachine()
        self.startGlobalListening()

    def onDisconnected(self):
        self._unsubscribe()
        self.__stateMachine.stop()
        lockNotificationManager(False, OTG_LOCK_SOURCE_NAME)
        lockAchievementsEarning(False)
        lockSteamShade(False)
        self.stopGlobalListening()

    def onPrbEntitySwitched(self):
        self.onEntryPointUpdated()

    def onUnitPlayerRemoved(self, pInfo):
        self.onEntryPointUpdated()

    def onUnitPlayerStateChanged(self, pInfo):
        self.onEntryPointUpdated()

    def areBaseRewardsReceived(self):
        return self.isAdditionalRewardReceived() and (self.isFullListBranchReceived() or self.isCollectorsCompensationReceived())

    def areWDRRewardsReceived(self):
        return self.isWDRBranchReceived() or self.isWDRBranchCompensationReceived()

    def getAvailabilityError(self):
        if not self.isEnabled():
            return OTG_ERROR_CODES.NOT_AVAILABLE
        else:
            if not self.isActive():
                return OTG_ERROR_CODES.NOT_ACTIVE
            return

    def getBranchById(self, branchId, fromList):
        return findFirst(lambda branch: branch.branchId == branchId, self.__getBranches(fromList))

    def getBranchesSortedForNation(self, fromList):
        branches = self.__getBranches(fromList)
        return self.__groupAndSortBranches([ branch for branch in branches if self.__validateBranchToReceive(branch)
                                           ])

    def getConfig(self):
        return self.__oneTimeGiftSettings

    def getEndTime(self):
        return self.__oneTimeGiftSettings.endTime

    def getStartTime(self):
        return self.__oneTimeGiftSettings.startTime

    def getRemindTime(self):
        return self.__oneTimeGiftSettings.remindTime

    def getRemindBattlesAmount(self):
        return self.__oneTimeGiftSettings.remindBattlesAmount

    def isActive(self):
        return self.isEnabled() and self.getStartTime() <= time_utils.getServerUTCTime() < self.getEndTime()

    def isAdditionalRewardReceived(self):
        return self.__itemsCache.items.tokens.isTokenAvailable(one_time_gift_token.ADDITIONAL_REWARD_BLOCKER)

    def isCollectorsCompensationReceived(self):
        return self.__itemsCache.items.tokens.isTokenAvailable(one_time_gift_token.COLLECTOR_REWARD_BLOCKER)

    def isWDRBranchCompensationReceived(self):
        return self.__itemsCache.items.tokens.isTokenAvailable(one_time_gift_token.WDR_COMPENSATION_BLOCKER)

    def isBranchListPurchased(self, branchListType):
        inventoryVehsSet = set(self.__itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY))
        return self.__getBranchSets()[branchListType.value] <= inventoryVehsSet

    def isEnabled(self):
        return self.__oneTimeGiftSettings.isEnabled

    def isNewbieBranchReceived(self):
        return self.__itemsCache.items.tokens.isTokenAvailable(one_time_gift_token.NEWBIE_BRANCH_BLOCKER)

    def isFullListBranchReceived(self):
        return self.__itemsCache.items.tokens.isTokenAvailable(one_time_gift_token.FULL_BRANCH_BLOCKER)

    def isWDRBranchReceived(self):
        return self.__itemsCache.items.tokens.isTokenAvailable(one_time_gift_token.WDR_BRANCH_BLOCKER)

    def isPlayerNewbie(self):
        return self.__getAccountCreationTime() >= self.__oneTimeGiftSettings.newbieDistinctionTime

    def enterOTGStateMachine(self):
        if self.__stateMachine is None or not self.__stateMachine.isRunning():
            _logger.debug('Trying to enter state without running state machine')
            return
        else:
            if self.introShown:
                self.__stateMachine.post(StringEvent(OTGEvent.ENTRY_POINT_CLICK))
            else:
                self.__stateMachine.post(StringEvent(OTGEvent.INTRO_START))
                self.introShown = True
            return

    def onEntryPointClicked(self):
        _logger.info('OneTimeGift: onEntryPointClicked')
        if self.__wdrHelper is not None and not self.areWDRRewardsReceived():
            self.__wdrHelper.process()
            return
        else:
            self.enterOTGStateMachine()
            return

    def onShowInfoClicked(self, ctx=None):
        _logger.info('OneTimeGift: onShowIntroClicked')
        if self.__stateMachine is not None:
            self.__stateMachine.post(StringEvent(OTGEvent.INFO_CLICK, ctx=ctx))
        return

    def onViewError(self):
        _logger.info('OneTimeGift: onViewError')
        if self.__stateMachine is not None:
            nextTick(self.__stateMachine.post)(StringEvent(OTGEvent.ERROR, error=OTG_ERROR_CODES.NOT_AVAILABLE))
        return

    def __getAccountCreationTime(self):
        dossierDescr = self.__itemsCache.items.getAccountDossier().getDossierDescr()
        return dossierDescr['total']['creationTime']

    def __getBranches(self, fromList):
        return self.__branchesConfig[fromList.value]

    def __getBranchSets(self):
        if not self.__branchSets:
            self.__branchSets = {}
            for branchListType in (BranchListType.NEWBIE, BranchListType.ALL):
                self.__branchSets[branchListType.value] = set()
                for branch in self.__getBranches(branchListType):
                    self.__branchSets[branchListType.value].update(branch.vehCDs)

        return self.__branchSets

    @staticmethod
    def __groupAndSortBranches(branches):
        result = OrderedDict()
        for nationName, nationIdx in sorted(nations.INDICES.items(), key=lambda (key, value): GUI_NATIONS.index(key)):
            orderedBranches = []
            nationTopVehiclesOrdered = [ item[0].nodeCD for item in g_techTreeDP.getNationTreeIterator(nationIdx) if item[1]['column'] == MAX_OTG_VEH_LEVEL
                                       ]
            for branch in branches:
                if branch.vehCDs[(-1)] in nationTopVehiclesOrdered:
                    orderedBranches.append(branch)

            result[nationName] = sorted(orderedBranches, key=lambda nationBranch: nationTopVehiclesOrdered.index(nationBranch.vehCDs[(-1)]))

        return result

    @staticmethod
    def __hasOTGToken(mapping):
        return any(key.startswith(one_time_gift_token.PREFIX) for key in mapping)

    def __onTokensUpdated(self, diff):
        if self.__hasOTGToken(diff):
            _logger.debug('OneTimeGift: Player rewards status changed, %s', diff)
            self.onPlayerOTGStatusChanged()

    def __onServerSettingsChanged(self, serverSettings):
        if self.__serverSettings is not None:
            self.__serverSettings.onServerSettingsChange -= self.__updateOTGSettings
        self.__serverSettings = serverSettings
        newRawSettings = serverSettings.getSettings().get(OTG_GAME_PARAMS_KEY, {})
        self.__oneTimeGiftSettings = OneTimeGiftConfig(**newRawSettings)
        self.__serverSettings.onServerSettingsChange += self.__updateOTGSettings
        return

    @staticmethod
    def __readBranchesFromConfig():
        result = {}
        for branchListType, branches in getOneTimeGiftBranchesCfg().items():
            result[branchListType] = [ TechTreeBranch(branchId, branch) for branchId, branch in enumerate(branches)
                                     ]

        return result

    def __startStateMachine(self):
        if not self.isActive():
            return
        if not self.__stateMachine.isRunning():
            _logger.debug('Start OTG state machine due to active event')
            self.__stateMachine.configure()
            self.__stateMachine.start()

    @serverSettingsChangeListener(OTG_GAME_PARAMS_KEY)
    def __updateOTGSettings(self, diff):
        self.__oneTimeGiftSettings = self.__oneTimeGiftSettings.replace(diff[OTG_GAME_PARAMS_KEY].copy())
        self.__resetTimer()
        self.__startStateMachine()
        self.onSettingsChanged()

    def __validateBranchToReceive(self, branch):
        branchVehicles = [ self.__itemsCache.items.getItemByCD(vehCD) for vehCD in branch.vehCDs ]
        return not all(vehicle.isPurchased for vehicle in branchVehicles)

    def __getEntryPointTimerDelta(self):
        currentTime = time_utils.getServerUTCTime()
        startTime = self.getStartTime()
        remindTime = self.getRemindTime()
        if currentTime < startTime:
            return max(0, startTime - currentTime)
        if currentTime < remindTime:
            return max(0, remindTime - currentTime)
        return max(0, self.getEndTime() - currentTime)

    def __resetTimer(self):
        self.startNotification()
        self.__timerUpdate()

    def __timerUpdate(self):
        self.__startStateMachine()
        self.onEntryPointUpdated()
        umgBanner = getOneTimeGiftEventBanner()
        if self.isEntryPointEnabled and umgBanner and not umgBanner.isVisible:
            umgBanner.update()