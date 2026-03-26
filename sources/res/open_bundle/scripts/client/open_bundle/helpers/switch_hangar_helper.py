from gui.prb_control.entities.listener import IGlobalListener
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG
from gui.shared import EVENT_BUS_SCOPE, g_eventBus, events

class SwitchHangarHelper(IGlobalListener):
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        self.__actionOnModeSwitched = None
        return

    def stop(self):
        self.__actionOnModeSwitched = None
        self.__hangarSpace.onSpaceCreate -= self.__tryCallAction
        return

    def onPrbEntitySwitched(self):
        self.__tryCallAction()

    def selectRandomBattle(self, callback):
        self.__actionOnModeSwitched = callback
        self.startGlobalListening()
        self.__hangarSpace.onSpaceCreate += self.__tryCallAction
        g_eventBus.handleEvent(events.PrbActionEvent(PrbAction(PREBATTLE_ACTION_NAME.RANDOM), events.PrbActionEvent.SELECT), EVENT_BUS_SCOPE.LOBBY)

    def isRandomPrbActive(self):
        if self.prbEntity is None:
            return False
        else:
            return bool(self.prbEntity.getModeFlags() & FUNCTIONAL_FLAG.RANDOM)

    def __tryCallAction(self):
        if self.isRandomPrbActive() and self.__actionOnModeSwitched is not None and callable(self.__actionOnModeSwitched):
            self.__actionOnModeSwitched()
            self.__actionOnModeSwitched = None
        self.__hangarSpace.onSpaceCreate -= self.__tryCallAction
        self.stopGlobalListening()
        return