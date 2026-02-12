import typing, Event
from gui.battle_control import avatar_getter
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.battle_control.arena_info.settings import ARENA_LISTENER_SCOPE as _SCOPE
from gui.battle_control.view_components import ViewComponentsController
from helpers import dependency
from lunar_possession.gui.lunar_possession_gui_constants import BATTLE_CTRL_ID
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from skeletons.gui.battle_session import IBattleContext, IClientArenaVisitor
_UNKNOWN_VEHICLE_ID = 0

class ILunarPossessionListener(object):

    def updateSpiritPossession(self, vehicleId, isEnemy, hasSpirit):
        raise NotImplementedError


class LunarPossessionBattleController(IArenaVehiclesController, ViewComponentsController):
    __slots__ = ('__playerVehicleID', '__currentVehicleID', '__eManager')
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(LunarPossessionBattleController, self).__init__()
        self.__playerVehicleID = _UNKNOWN_VEHICLE_ID
        self.__currentVehicleID = _UNKNOWN_VEHICLE_ID
        self.__eManager = Event.EventManager()

    def getControllerID(self):
        return BATTLE_CTRL_ID.LUNAR_POSSESSION_BATTLE_CTRL

    def getCtrlScope(self):
        return _SCOPE.VEHICLES

    def startControl(self, battleCtx, arenaVisitor):
        vStateCtrl = self.__sessionProvider.shared.vehicleState
        self.__currentVehicleID = vStateCtrl.getControllingVehicleID() if vStateCtrl else _UNKNOWN_VEHICLE_ID
        self.__playerVehicleID = avatar_getter.getPlayerVehicleID()
        self.__addListeners()

    def updateSpiritPossession(self, vehicleId, isEnemy, hasSpirit):
        for component in self._viewComponents:
            component.updateSpiritPossession(vehicleId, isEnemy, hasSpirit)

    def __addListeners(self):
        pass


def createLunarPossessionBattleController():
    return LunarPossessionBattleController()