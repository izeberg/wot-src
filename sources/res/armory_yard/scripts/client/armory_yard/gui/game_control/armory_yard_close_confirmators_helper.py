from gui.shared import events
from gui.shared.close_confiramtor_helper import CloseConfirmatorsHelper
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

class ArmoryYardCloseConfirmatorsHelper(CloseConfirmatorsHelper):

    def __init__(self):
        super(ArmoryYardCloseConfirmatorsHelper, self).__init__()
        self.__restrictionsActive = False

    def start(self, closeConfirmator):
        if self.__restrictionsActive:
            super(ArmoryYardCloseConfirmatorsHelper, self).stop()
        super(ArmoryYardCloseConfirmatorsHelper, self).start(closeConfirmator)
        self.__restrictionsActive = True

    def stop(self):
        if not self.__restrictionsActive:
            return
        super(ArmoryYardCloseConfirmatorsHelper, self).stop()
        self.__restrictionsActive = False

    def getRestrictedEvents(self):
        result = super(ArmoryYardCloseConfirmatorsHelper, self).getRestrictedEvents()
        result.remove(events.PrbActionEvent.LEAVE)
        result.remove(events.PrbActionEvent.SELECT)
        return result

    def getRestrictedSfViews(self):
        result = super(ArmoryYardCloseConfirmatorsHelper, self).getRestrictedSfViews()
        result.append(VIEW_ALIAS.LOBBY_CUSTOMIZATION)
        return result