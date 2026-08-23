from gui.impl.gen import R
from gui.shared.system_factory import registerGamefaceNotifications
from journey_marathon.gui.impl.lobby.gf_notifications.constants import JMGFNotificationTemplates
from journey_marathon.gui.impl.lobby.gf_notifications.daily_reward_notification import JMDailyRewardNotification

def registerJMNotifications():
    registerGamefaceNotifications({JMGFNotificationTemplates.DAILY_REWARD: (
                                              R.views.journey_marathon.mono.lobby.notifications.daily_reward(), JMDailyRewardNotification)})