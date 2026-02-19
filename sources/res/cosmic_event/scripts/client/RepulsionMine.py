import BigWorld
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from cosmic_event.gui.shared.events import MineEvent

class RepulsionMine(BigWorld.Entity):

    def onEnterWorld(self, *args):
        if self.isPlaced:
            self.__sendEvent(MineEvent.APPEAR, {'entity': self})

    def set_isPlaced(self, prev):
        if self.isPlaced:
            self.__sendEvent(MineEvent.APPEAR, {'entity': self})

    def set_isDetonated(self, prev):
        if self.isDetonated:
            self.__sendEvent(MineEvent.EXPLODE, {'entity': self})

    def __sendEvent(self, event, ctx):
        g_eventBus.handleEvent(MineEvent(event, ctx=ctx), scope=EVENT_BUS_SCOPE.BATTLE)