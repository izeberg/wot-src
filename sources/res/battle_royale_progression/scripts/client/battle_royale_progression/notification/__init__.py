from battle_royale_progression.notification.actions_handlers import ShowBRProgressionActionHandler
from gui.shared.system_factory import registerNotificationsActionsHandlers

def registerClientNotificationHandlers():
    registerNotificationsActionsHandlers((ShowBRProgressionActionHandler,))