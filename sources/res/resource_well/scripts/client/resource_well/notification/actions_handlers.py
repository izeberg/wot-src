from __future__ import absolute_import
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE
from resource_well.gui.shared.event_dispatcher import showMainWindow

class OpenResourceWellProgressionStartWindow(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.RESOURCE_WELL_START

    @classmethod
    def getActions(cls):
        return ('openResourceWellProgressionStartWindow', )

    def doAction(self, model, entityID, action):
        showMainWindow()


class OpenResourceWellProgressionWindow(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('OpenResourceWellProgressionWindow', )

    def doAction(self, model, entityID, action):
        showMainWindow()