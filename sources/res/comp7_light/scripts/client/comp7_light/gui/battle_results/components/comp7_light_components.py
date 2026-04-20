from comp7_core.gui.battle_results.components.comp7_core_components import checkIfDeserter
from account_helpers.AccountSettings import STATS_COMP7_LIGHT_SORTING
from fairplay_violation_types import FairplayViolations
from gui.battle_results.components import base
from gui.battle_results.components.shared import SortingBlock
from gui.impl import backport
from gui.impl.gen.resources import R

class IsDeserterFlag(base.StatsItem):

    def _convert(self, result, reusable):
        if checkIfDeserter(reusable, FairplayViolations.COMP7_LIGHT_DESERTER):
            return backport.text(R.strings.comp7_light.battleResult.header.deserter())


class Comp7LightSortingBlock(SortingBlock):
    __slots__ = ()

    def __init__(self, meta=None, field='', *path):
        super(Comp7LightSortingBlock, self).__init__(STATS_COMP7_LIGHT_SORTING, meta, field, *path)