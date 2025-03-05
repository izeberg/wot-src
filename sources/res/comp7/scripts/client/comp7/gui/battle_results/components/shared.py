from account_helpers.AccountSettings import STATS_COMP7_SORTING
from gui.battle_results.components.shared import SortingBlock

class Comp7SortingBlock(SortingBlock):
    __slots__ = ()

    def __init__(self, meta=None, field='', *path):
        super(Comp7SortingBlock, self).__init__(STATS_COMP7_SORTING, meta, field, *path)