from __future__ import absolute_import
import typing
from fun_random.gui.battle_results.sub_presenters.fun_personal_info import FunPersonalInfoSubPresenter
from lunar_possession.gui.battle_results.packers.lunar_packers import LunarPersonalInfo
if typing.TYPE_CHECKING:
    from gui.battle_results.stats_ctrl import BattleResults

class LunarPersonalInfoSubPresenter(FunPersonalInfoSubPresenter):

    def packBattleResults(self, battleResults):
        with self.getViewModel().transaction() as (model):
            LunarPersonalInfo.packModel(model, battleResults)