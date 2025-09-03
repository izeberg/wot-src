import logging
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from one_time_gift_common import one_time_gift_account_commands
_logger = logging.getLogger(__name__)

class OneTimeGiftAccountComponent(BaseAccountExtensionComponent):

    def requestOneTimeGift(self, branchToReceive, callback):
        _logger.debug('OneTimeGift: requestOneTimeGift %s', branchToReceive)
        self.entity._doCmdIntArr(one_time_gift_account_commands.CMD_ONE_TIME_GIFT_BRANCH, branchToReceive, lambda requestID, resultID, errorStr, ctx=None: callback(resultID, errorStr, ctx))
        return

    def requestCollectorsCompensation(self, callback):
        _logger.debug('OneTimeGift: requestCollectorsCompensation')
        self.entity._doCmdNoArgs(one_time_gift_account_commands.CMD_ONE_TIME_GIFT_COLLECTORS_COMPENSATION, lambda requestID, resultID, errorStr, ctx=None: callback(resultID, errorStr, ctx))
        return

    def requestOneTimeGiftAdditionalReward(self, callback):
        _logger.debug('OneTimeGift: requestOneTimeGiftAdditionalReward')
        self.entity._doCmdNoArgs(one_time_gift_account_commands.CMD_ONE_TIME_GIFT_ADDITIONAL_REWARD, lambda requestID, resultID, errorStr, ctx=None: callback(resultID, errorStr, ctx))
        return