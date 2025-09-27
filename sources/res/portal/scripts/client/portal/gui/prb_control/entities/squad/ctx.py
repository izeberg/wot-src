from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('_battleLevel', ))
class SetUnitBattleLevelCtx(UnitRequestCtx):
    __slots__ = ('_battleLevel', )

    def __init__(self, battleLevel, waitingID=''):
        super(SetUnitBattleLevelCtx, self).__init__(waitinID=waitingID)
        self._battleLevel = battleLevel

    def getBattleLevel(self):
        return self._battleLevel