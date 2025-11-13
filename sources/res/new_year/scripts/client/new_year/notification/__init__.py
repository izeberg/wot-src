from new_year.notification.actions_handlers import registerNewYearActionHandlers
from new_year.notification.listeners import registerNewYearNotificationListeners

def registerNewYearNotifications():
    registerNewYearNotificationListeners()
    registerNewYearActionHandlers()