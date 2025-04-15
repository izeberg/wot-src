from gui.shared.system_factory import registerNotificationsActionsHandlers, registerNotificationsListeners
from resource_well.notification.actions_handlers import OpenResourceWellProgressionStartWindow, OpenResourceWellProgressionWindow
from resource_well.notification.listeners import ResourceWellListener

def registerResourceWellNotifications():
    registerNotificationsListeners((ResourceWellListener,))
    registerNotificationsActionsHandlers((
     OpenResourceWellProgressionStartWindow, OpenResourceWellProgressionWindow))