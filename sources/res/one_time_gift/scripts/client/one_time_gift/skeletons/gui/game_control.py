import typing
from one_time_gift.helpers.server_settings import OneTimeGiftConfig
from skeletons.gui.game_control import IGameController
from one_time_gift_common.one_time_gift_constants import BranchListType, TechTreeBranch
if typing.TYPE_CHECKING:
    from typing import Callable, Optional
    T_PROCESSOR_CALLBACK = Callable[([bool], None)]

class IOneTimeGiftController(IGameController):
    onSettingsChanged = None
    onEntryPointUpdated = None
    onPlayerOTGStatusChanged = None

    @property
    def isEntryPointEnabled(self):
        raise NotImplementedError

    @property
    def canReceiveBaseOTGRewards(self):
        raise NotImplementedError

    @property
    def isEntryPointActive(self):
        raise NotImplementedError

    @property
    def introShown(self):
        raise NotImplementedError

    @introShown.setter
    def introShown(self, value):
        raise NotImplementedError

    def areBaseRewardsReceived(self, *_):
        raise NotImplementedError

    def areWDRRewardsReceived(self, *_):
        raise NotImplementedError

    def getAvailabilityError(self):
        raise NotImplementedError

    def getBranchById(self, branchId, fromList):
        raise NotImplementedError

    def getBranchesSortedForNation(self, fromList):
        raise NotImplementedError

    def getConfig(self):
        raise NotImplementedError

    def getEndTime(self):
        raise NotImplementedError

    def getStartTime(self):
        raise NotImplementedError

    def getRemindTime(self):
        raise NotImplementedError

    def getRemindBattlesAmount(self):
        raise NotImplementedError

    def isAdditionalRewardReceived(self):
        raise NotImplementedError

    def isBranchListPurchased(self, branchListType):
        raise NotImplementedError

    def isCollectorsCompensationReceived(self):
        raise NotImplementedError

    def isWDRBranchCompensationReceived(self):
        raise NotImplementedError

    def isActive(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def isFullListBranchReceived(self):
        raise NotImplementedError

    def isWDRBranchReceived(self):
        raise NotImplementedError

    def isNewbieBranchReceived(self):
        raise NotImplementedError

    def isPlayerNewbie(self):
        raise NotImplementedError

    def enterOTGStateMachine(self):
        pass

    def onEntryPointClicked(self):
        raise NotImplementedError

    def onShowInfoClicked(self, ctx=None):
        raise NotImplementedError

    def onViewError(self):
        raise NotImplementedError