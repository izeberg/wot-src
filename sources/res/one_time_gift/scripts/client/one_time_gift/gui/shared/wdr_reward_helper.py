import logging
from adisp import adisp_process
from helpers import dependency
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController
from one_time_gift.gui.shared import event_dispatcher as otg_event_dispatcher, processors as otg_processors
from one_time_gift_common.one_time_gift_constants import BranchListType
from one_time_gift.gui.messages import pushOTGErrorNotificationFromCode
_logger = logging.getLogger(__name__)

class WDRRewardHelper(object):
    __otgCtrl = dependency.descriptor(IOneTimeGiftController)

    def process(self):
        if self.__otgCtrl.isBranchListPurchased(BranchListType.ALL):
            self.__processWDRCompensation()
        else:
            self.__processWDRBranchSelection()

    def __processWDRBranchSelection(self):
        otg_event_dispatcher.showWDRBranchSelectionWindow(onConfirmCallback=self.__onWDRBranchReceived, onCloseCallback=self.__onWDRBranchSelectionClosed, onErrorCallback=self.__onWDRBranchRequestError)

    def __onWDRBranchReceived(self, *args, **kwargs):
        _logger.info('__onWDRBranchReceived, %s, %s', args, kwargs)
        rewards = kwargs.get('rewards')
        if rewards:
            otg_event_dispatcher.showWDRBranchRewardWindow(rewards=rewards, onCloseCallback=self.__exitWDRFlow)
            return
        self.__exitWDRFlow()

    def __onWDRBranchSelectionClosed(self, *args, **kwargs):
        _logger.debug('__onWDRBranchSelectionClosed, %s, %s', args, kwargs)
        self.__exitWDRFlow()

    def __onWDRBranchRequestError(self, *args, **kwargs):
        _logger.info('__onWDRBranchRequestError, %s, %s', args, kwargs)
        otg_event_dispatcher.closeOneTimeGiftWindow()
        errStr = kwargs.get('error')
        pushOTGErrorNotificationFromCode(errStr)

    def __processWDRCompensation(self):
        otg_event_dispatcher.processWDRCompensation(self.__requestWDRCompensation)

    @adisp_process
    def __requestWDRCompensation(self):
        result = yield otg_processors.OneTimeGiftWDRCompensationProcessor().request()
        if result.success:
            otg_event_dispatcher.showWDRCompensationWindow(onCloseCallback=self.__onWDRCompensationScreenClosed)
        else:
            self.__onWDRCompensationRequestError(error=result.userMsg)

    def __onWDRCompensationScreenClosed(self, *args, **kwargs):
        _logger.info('__onWDRCompensationScreenClosed, %s, %s', args, kwargs)
        self.__exitWDRFlow()

    def __onWDRCompensationRequestError(self, *args, **kwargs):
        _logger.info('__onWDRCompensationRequestError, %s, %s', args, kwargs)
        otg_event_dispatcher.closeOneTimeGiftWindow()
        errStr = kwargs.get('error')
        pushOTGErrorNotificationFromCode(errStr)

    def __exitWDRFlow(self, *_, **__):
        if self.__otgCtrl.areBaseRewardsReceived():
            otg_event_dispatcher.closeOneTimeGiftWindow()
        else:
            self.__otgCtrl.enterOTGStateMachine()