from __future__ import absolute_import
import typing
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from fall_tanks.gui.fall_tanks_gui_constants import BATTLE_CTRL_ID
from fall_tanks.gui.battle_control.arena_info.arena_vos import FallTanksVehicleInfo
if typing.TYPE_CHECKING:
    from fall_tanks.gui.battle_control.arena_info.interfaces import IFallTanksBattleController, IFallTanksVehicleInfo

class FallTanksBattleMixin(object):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    @classmethod
    def getFallTanksAttachedVehicleInfo(cls):
        ctrl = cls._getFallTanksBattleCtrl()
        if ctrl is not None:
            return ctrl.getFallTanksAttachedVehicleInfo()
        else:
            return FallTanksVehicleInfo()

    @classmethod
    def getFallTanksPlayerVehicleInfo(cls):
        ctrl = cls._getFallTanksBattleCtrl()
        if ctrl is not None:
            return ctrl.getFallTanksPlayerVehicleInfo()
        else:
            return FallTanksVehicleInfo()

    @classmethod
    def startFallTanksAttachedListening(cls, listener):
        ctrl = cls._getFallTanksBattleCtrl()
        if ctrl is not None:
            ctrl.onFallTanksAttachedInfoUpdate += listener
        return

    @classmethod
    def stopFallTanksAttachedListening(cls, listener):
        ctrl = cls._getFallTanksBattleCtrl()
        if ctrl is not None:
            ctrl.onFallTanksAttachedInfoUpdate -= listener
        return

    @classmethod
    def _getFallTanksBattleCtrl(cls):
        return cls.__sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.FALL_TANKS_BATTLE_CTRL)


class PostmortemMixin(object):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    @classmethod
    def isInPostmortem(cls):
        ctrl = cls.__sessionProvider.shared.vehicleState
        if ctrl is not None:
            return ctrl.isInPostmortem
        else:
            return False

    @classmethod
    def startPostmortemListening(cls, switchedListener, movingListener):
        ctrl = cls.__sessionProvider.shared.vehicleState
        if ctrl:
            ctrl.onPostMortemSwitched += switchedListener
            ctrl.onRespawnBaseMoving += movingListener

    @classmethod
    def stopPostmortemListening(cls, switchedListener, movingListener):
        ctrl = cls.__sessionProvider.shared.vehicleState
        if ctrl:
            ctrl.onPostMortemSwitched -= switchedListener
            ctrl.onRespawnBaseMoving -= movingListener