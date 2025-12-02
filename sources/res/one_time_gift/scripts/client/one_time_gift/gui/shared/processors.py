import logging, typing, BigWorld
from gui.shared.gui_items.processors import Processor
from gui.shared.gui_items.processors.plugins import AsyncDialogConfirmator
from gui.Scaleform.Waiting import Waiting
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages
from one_time_gift.gui.gui_constants import SCH_CLIENT_MSG_TYPE
from one_time_gift.gui.shared.event_dispatcher import showConfirmSelectionDialog
if typing.TYPE_CHECKING:
    from typing import Callable
_logger = logging.getLogger(__name__)

class BaseOneTimeGiftRewardProcessor(Processor):
    _systemMessages = dependency.descriptor(ISystemMessages)

    def _response(self, code, callback, errStr='', ctx=None):
        Waiting.hide('updating')
        if code >= 0:
            _logger.debug('%s: Server success response: code=%r, error=%r, ctx=%r', self.__class__.__name__, code, errStr, ctx)
            return callback(self._successHandler(code, ctx=ctx))
        _logger.debug('%s: Server fail response: code=%r, error=%r, ctx=%r', self.__class__.__name__, code, errStr, ctx)
        return callback(self._errorHandler(code, errStr=errStr, ctx=ctx))


class OneTimeGiftBranchRewardProcessor(BaseOneTimeGiftRewardProcessor):

    def __init__(self, branchToReceive, parent=None):
        super(OneTimeGiftBranchRewardProcessor, self).__init__(plugins=[
         AsyncDialogConfirmator(self._getConfirmDialogFunc(), branchToReceive, parent=parent)])
        self._branchToReceive = branchToReceive

    def _request(self, callback):
        Waiting.show('updating')
        BigWorld.player().OneTimeGiftAccountComponent.requestOneTimeGift(self._branchToReceive, lambda code, errorStr='', ctx=None: self._response(code, callback, errorStr, ctx))
        return

    def _successHandler(self, code, ctx=None):
        for result in ctx:
            msg = {'vehicles': result.get('vehicles', {}), 'slots': result.get('slots', {}).get('count', 0), 
               'isPremium': False}
            self._systemMessages.proto.serviceChannel.pushClientMessage('', SCH_CLIENT_MSG_TYPE.OTG_VEHICLES_RECEIVED, auxData=msg)

        return super(OneTimeGiftBranchRewardProcessor, self)._successHandler(code, ctx)

    @staticmethod
    def _getConfirmDialogFunc():
        return showConfirmSelectionDialog


class OneTimeGiftWDRBranchRewardProcessor(OneTimeGiftBranchRewardProcessor):

    def _request(self, callback):
        Waiting.show('updating')
        BigWorld.player().OneTimeGiftAccountComponent.requestWDRBranch(self._branchToReceive, lambda code, errorStr='', ctx=None: self._response(code, callback, errorStr, ctx))
        return


class OneTimeGiftAdditionalRewardProcessor(BaseOneTimeGiftRewardProcessor):

    def _request(self, callback):
        Waiting.show('updating')
        BigWorld.player().OneTimeGiftAccountComponent.requestOneTimeGiftAdditionalReward(lambda code, errorStr='', ctx=None: self._response(code, callback, errorStr, ctx))
        return

    def _successHandler(self, code, ctx=None):
        for result in ctx:
            self._systemMessages.proto.serviceChannel.pushClientMessage('', SCH_CLIENT_MSG_TYPE.OTG_ADDITIONAL_REWARDS_RECEIVED, auxData=result[0])

        return super(OneTimeGiftAdditionalRewardProcessor, self)._successHandler(code, ctx)


class OneTimeGiftCollectorsCompensationProcessor(BaseOneTimeGiftRewardProcessor):

    def _request(self, callback):
        Waiting.show('updating')
        BigWorld.player().OneTimeGiftAccountComponent.requestCollectorsCompensation(lambda code, errorStr='', ctx=None: self._response(code, callback, errorStr, ctx))
        return

    def _successHandler(self, code, ctx=None):
        for result in ctx:
            self._systemMessages.proto.serviceChannel.pushClientMessage('', SCH_CLIENT_MSG_TYPE.OTG_COLLECTOR_REWARDS_RECEIVED, auxData=result)

        return super(OneTimeGiftCollectorsCompensationProcessor, self)._successHandler(code, ctx)


class OneTimeGiftWDRCompensationProcessor(BaseOneTimeGiftRewardProcessor):

    def _request(self, callback):
        Waiting.show('updating')
        BigWorld.player().OneTimeGiftAccountComponent.requestWDRBranchCompensation(lambda code, errorStr='', ctx=None: self._response(code, callback, errorStr, ctx))
        return