from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages
from one_time_gift_common.one_time_gift_constants import OTG_ERROR_CODES

def pushOTGErrorNotificationFromCode(errStr):
    if errStr == OTG_ERROR_CODES.NOT_ACTIVE:
        pushOTGNotActiveErrorNotification()
    elif errStr == OTG_ERROR_CODES.REWARD_RECEIVED:
        pushOTGRewardReceivedErrorNotification()
    else:
        pushOTGNotAvailableErrorNotification()


@dependency.replace_none_kwargs(systemMessages=ISystemMessages)
def pushOTGNotActiveErrorNotification(systemMessages=None):
    systemMessages.proto.serviceChannel.pushClientSysMessage(backport.text(R.strings.one_time_gift_messenger.serviceChannelMessages.eventEndedError.body()), SystemMessages.SM_TYPE.ErrorSimple, priority=NotificationPriorityLevel.MEDIUM)


@dependency.replace_none_kwargs(systemMessages=ISystemMessages)
def pushOTGRewardReceivedErrorNotification(systemMessages=None):
    systemMessages.proto.serviceChannel.pushClientSysMessage(backport.text(R.strings.one_time_gift_messenger.serviceChannelMessages.rewardReceived.body()), SystemMessages.SM_TYPE.ErrorSimple, priority=NotificationPriorityLevel.MEDIUM)


@dependency.replace_none_kwargs(systemMessages=ISystemMessages)
def pushOTGNotAvailableErrorNotification(systemMessages=None):
    systemMessages.proto.serviceChannel.pushClientSysMessage(backport.text(R.strings.one_time_gift_messenger.serviceChannelMessages.notAvailableError.body()), SystemMessages.SM_TYPE.ErrorSimple, priority=NotificationPriorityLevel.MEDIUM)