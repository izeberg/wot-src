from comp7_core.gui.battle_results.components.comp7_core_components import checkIfDeserter
from fairplay_violation_types import FairplayViolations
from gui.battle_results.components import base
from gui.impl import backport
from gui.impl.gen.resources import R

class IsDeserterFlag(base.StatsItem):

    def _convert(self, result, reusable):
        if checkIfDeserter(reusable, FairplayViolations.COMP7_LIGHT_DESERTER):
            return backport.text(R.strings.comp7_light.battleResult.header.deserter())