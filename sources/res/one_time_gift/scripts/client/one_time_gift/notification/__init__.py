from gui.shared.system_factory import registerNotificationsListeners
from one_time_gift.notification.listeners import RewardAvailableListener

def registerOTGNotificationsListeners():
    registerNotificationsListeners((RewardAvailableListener,))