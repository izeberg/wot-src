from open_bundle.gui.constants import GFNotificationTemplates
from open_bundle.gui.impl.lobby.notifications.start_notification import StartNotification
from open_bundle.gui.impl.lobby.notifications.special_rewards_notification import SpecialRewardsNotification
from open_bundle.notification.listeners import OpenBundleListener
from open_bundle.notification.actions_handlers import OpenBundleReminderHandler
from gui.shared.system_factory import registerGamefaceNotifications, registerNotificationsActionsHandlers, registerNotificationsListeners
from gui.impl.gen import R
__NOTIFICATION_LAYOUT = R.views.open_bundle.mono.lobby.notifications

def registerOpenBundleNotifications():
    registerNotificationsListeners((OpenBundleListener,))
    registerNotificationsActionsHandlers((OpenBundleReminderHandler,))
    registerGamefaceNotifications({GFNotificationTemplates.START_NOTIFICATION: (
                                                  __NOTIFICATION_LAYOUT.start_notification(), StartNotification), 
       GFNotificationTemplates.SPECIAL_REWARDS_NOTIFICATION: (
                                                            __NOTIFICATION_LAYOUT.special_rewards_notification(), SpecialRewardsNotification)})