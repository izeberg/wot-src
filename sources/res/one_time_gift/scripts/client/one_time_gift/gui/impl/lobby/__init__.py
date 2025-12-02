from gui.impl.gen import R
from gui.shared.system_factory import registerGamefaceNotifications
from one_time_gift.gui.impl.lobby.reward_available_notification_view import RewardAvailableNotificationView

def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()


OTG_REWARD_AVAILABLE_NOTIFICATION = 'OTGRewardAvailableNotification'
registerGamefaceNotifications({OTG_REWARD_AVAILABLE_NOTIFICATION: (
                                     R.views.one_time_gift.mono.lobby.reward_available_notification_view(), RewardAvailableNotificationView)})