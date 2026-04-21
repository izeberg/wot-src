from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE
from open_bundle.gui.shared.event_dispatcher import showOpenBundleMainView

class OpenBundleReminderHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('openBundle', )

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData and 'bundleID' in savedData and savedData['bundleID']:
            showOpenBundleMainView(savedData['bundleID'])