from constants import IS_DEVELOPMENT
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicTeleportPlugin, ClassicMinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import ArenaVehiclesPlugin
from gui.battle_control import matrix_factory
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from lunar_possession_common.component_helpers import isSpiritCarrier
from lunar_possession.gui.shared.events import BuffEvents, MatchRoundsEvents
from lunar_possession.gui.lunar_possession_gui_constants import VEHICLE_SPIRIT_INDICATOR

class LunarMinimapComponent(ClassicMinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(LunarMinimapComponent, self)._setupPlugins(arenaVisitor)
        if IS_DEVELOPMENT:
            setup['teleport'] = ClassicTeleportPlugin
        setup['vehicles'] = LunarMinimapVehiclesPlugin
        return setup


class LunarMinimapVehiclesPlugin(ArenaVehiclesPlugin):
    _POSSESSED_SYMBOL = VEHICLE_SPIRIT_INDICATOR
    _CONTAINER_NAME = 'lunar'

    def __init__(self, parentObj):
        super(LunarMinimapVehiclesPlugin, self).__init__(parentObj)
        self.__spiritCarrierID = None
        return

    def start(self):
        super(LunarMinimapVehiclesPlugin, self).start()
        g_eventBus.addListener(BuffEvents.VEHICLE_GET_BUFF, self.__updateSpiritCarrierEntry, EVENT_BUS_SCOPE.BATTLE)
        g_eventBus.addListener(BuffEvents.VEHICLE_LOSE_BUFF, self.__updateSpiritCarrierEntry, EVENT_BUS_SCOPE.BATTLE)
        g_eventBus.addListener(MatchRoundsEvents.ROUND_START, self.__onRoundStart, EVENT_BUS_SCOPE.BATTLE)
        ctrl = self.sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onMinimapVehicleRemoved += self.__HideSpiritIcon
        return

    def stop(self):
        g_eventBus.removeListener(BuffEvents.VEHICLE_GET_BUFF, self.__updateSpiritCarrierEntry, EVENT_BUS_SCOPE.BATTLE)
        g_eventBus.removeListener(BuffEvents.VEHICLE_LOSE_BUFF, self.__updateSpiritCarrierEntry, EVENT_BUS_SCOPE.BATTLE)
        g_eventBus.removeListener(MatchRoundsEvents.ROUND_START, self.__onRoundStart, EVENT_BUS_SCOPE.BATTLE)
        ctrl = self.sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onMinimapVehicleRemoved -= self.__HideSpiritIcon
        super(LunarMinimapVehiclesPlugin, self).stop()
        return

    def __updateSpiritCarrierEntry(self, event):
        vehicleID = event.vehicleID
        hasSpiritBuff = isSpiritCarrier(vehicleID)
        carrierMatrix = matrix_factory.getEntityMatrix(vehicleID)
        if self.__spiritCarrierID is not None:
            self._setActive(self.__spiritCarrierID, active=hasSpiritBuff)
            self._setMatrix(self.__spiritCarrierID, carrierMatrix)
        else:
            self.__spiritCarrierID = self._addEntry(self._POSSESSED_SYMBOL, self._CONTAINER_NAME, matrix=carrierMatrix, active=hasSpiritBuff)
        return

    def __onRoundStart(self, event):
        for _, entry in self._entries.iteritems():
            if entry.isEnemy() and entry.wasSpotted():
                entry.setActive(False)
                entry.setInAoI(False)
                self._setActive(entry.getID(), False)

    def __HideSpiritIcon(self, vehicleID):
        if self.__spiritCarrierID is not None and isSpiritCarrier(vehicleID):
            self._setActive(self.__spiritCarrierID, active=False)
        return

    def hideMinimapHP(self):
        self.setShowMinimapHP(False)