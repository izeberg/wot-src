from script_component.DynamicScriptComponent import DynamicScriptComponent

class GrinchBotOwnershipController(DynamicScriptComponent):

    def _onAvatarReady(self):
        super(GrinchBotOwnershipController, self)._onAvatarReady()
        self._sendOwnershipStateChangedEvent()

    def set_slavesLimit(self, _):
        self._sendOwnershipStateChangedEvent()

    def set_slaves(self, _):
        self._sendOwnershipStateChangedEvent()

    @property
    def slavesCount(self):
        if self.slaves:
            return len(self.slaves)
        return 0

    def _sendOwnershipStateChangedEvent(self):
        from grinch.gui.shared.events import BotOwnershipEvent
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        if self.entity.isPlayerVehicle:
            g_eventBus.handleEvent(BotOwnershipEvent(BotOwnershipEvent.OWNERSHIP_STATE_CHANGED, slavesLimit=self.slavesLimit, slavesCount=self.slavesCount), scope=EVENT_BUS_SCOPE.BATTLE)