from gui.shared.system_factory import collectTrainingRoomExternalHandlers

class TrainingRoomBaseHandler(object):

    def getArenaFilter(self):
        return

    def getArenaData(self):
        return

    def getAdditionalInfo(self):
        return

    def getIcon(self):
        return

    def getMaxPlayersInTeam(self):
        return

    def getObserverValidator(self):
        return

    def getPlayerReadyHandler(self):
        return

    def getPrebattleLimits(self):
        return

    def getPrebattlePropertyChecker(self):
        return

    def getVehicleWatcherType(self):
        return

    def getClientMessageData(self, errorType=None):
        return

    def isEnabledForGuiTypeName(self, guiTypeName=None):
        return False


def getTrainingRoomHandler(guiType=None):
    handler = collectTrainingRoomExternalHandlers().get(guiType)
    if handler is not None:
        return handler()
    else:
        return TrainingRoomBaseHandler()


def getAllTrainingRoomHandlers():
    handlers = collectTrainingRoomExternalHandlers()
    return [ handler() for handler in handlers.values() ]