from collections import namedtuple
from grinch_progression.gui.shared.event_dispatcher import showGrinchResultsView
from gui.battle_results.composer import RegularStatsComposer
BattleResult = namedtuple('BattleResult', ('results', 'reusable'))

class GrinchBattleStatsComposer(RegularStatsComposer):

    def __init__(self, reusable):
        super(GrinchBattleStatsComposer, self).__init__(reusable)
        self._results = None
        return

    def setResults(self, results, reusable):
        self._results = BattleResult(results=results, reusable=reusable)

    def getVO(self):
        return self._results

    @staticmethod
    def onShowResults(arenaUniqueID):
        pass

    @staticmethod
    def onResultsPosted(arenaUniqueID):
        showGrinchResultsView(arenaUniqueID)