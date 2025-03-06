from comp7.gui.battle_control.arena_info.arena_vos import Comp7Keys
from gui.battle_control.arena_info.vos_collections import VehicleInfoSortKey

class Comp7SortKey(VehicleInfoSortKey):
    __slots__ = ()

    def _cmp(self, other):
        xvInfoVO = self.vInfoVO
        yvInfoVO = other.vInfoVO
        result = cmp(yvInfoVO.isAlive(), xvInfoVO.isAlive())
        if result:
            return result
        xvIsQual = xvInfoVO.gameModeSpecific.getValue(Comp7Keys.IS_QUAL_ACTIVE, default=False)
        yvIsQual = yvInfoVO.gameModeSpecific.getValue(Comp7Keys.IS_QUAL_ACTIVE, default=False)
        result = cmp(xvIsQual, yvIsQual)
        if result:
            return result
        xvRank = xvInfoVO.gameModeSpecific.getValue(Comp7Keys.RANK, default=(0, 0))
        yvRank = yvInfoVO.gameModeSpecific.getValue(Comp7Keys.RANK, default=(0, 0))
        result = cmp(xvRank, yvRank)
        if result:
            return result
        return cmp(xvInfoVO.player, yvInfoVO.player)