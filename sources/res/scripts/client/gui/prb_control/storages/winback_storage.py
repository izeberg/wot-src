from constants import QUEUE_TYPE
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IWinbackController

class WinbackStorage(SessionStorage):
    __winbackController = dependency.descriptor(IWinbackController)

    def isModeSelected(self):
        return super(WinbackStorage, self).isModeSelected() and self.isModeAvailable()

    def isModeAvailable(self):
        return self.__winbackController.isModeAvailable()

    def shouldBeSelectedByDefault(self):
        return self.isModeAvailable()

    def getQueueTypeToReplace(self):
        return QUEUE_TYPE.RANDOMS

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.isWinback()