from adisp import adisp_process
from debug_utils import LOG_WARNING, LOG_ERROR
from gui.clientgw.ny_tamagotchi.contexts import NyTamagotchiGetPlayerInfoCtx, NyTamagotchiGetLeaderboardPageCtx, NyTamagotchiGetCurrentStateCtx, NyTamagotchiBuyItemsCtx, NyTamagotchiActivateItemCtx, NyTamagotchiGetPlayerStatsCtx
from helpers import dependency
from new_year.helpers.server_settings import getNewYearGeneralConfig
from new_year.skeletons.new_year import ITamagotchiDataProvider, ITamagotchiWebRequester
from skeletons.gui.web import IWebController

class TamagotchiWebRequester(ITamagotchiWebRequester):
    __slots__ = ()
    _RECALCULATION_CODE = 409
    _webController = dependency.descriptor(IWebController)
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)

    @adisp_process
    def requestPlayerInfo(self, callback=None):
        notRecalc = getNewYearGeneralConfig().getEnableTamagotchiSimulation()
        if not self._dataProvider.isValidConfig or notRecalc:
            result = yield self._webController.sendRequest(ctx=NyTamagotchiGetCurrentStateCtx(notRecalc=notRecalc))
        else:
            result = yield self._webController.sendRequest(ctx=NyTamagotchiGetPlayerInfoCtx())
        if not result.isSuccess():
            LOG_ERROR('[Tamagotchi] Failed to request player info', result.getExtraCode())
            self._dataProvider.playerInfo = None
            return
        else:
            self._dataProvider.config = result.data.get('config')
            self._dataProvider.playerInfo = result.data
            self._dataProvider.syncOpenedIndicators()
            if callback is not None:
                callback()
            return

    @adisp_process
    def requestLeaderboardPage(self, page=0, isUserPage=False, cumulative=False):
        result = yield self._webController.sendRequest(ctx=NyTamagotchiGetLeaderboardPageCtx(page=page, isUserPage=isUserPage, cumulative=cumulative))
        if result.isSuccess():
            if cumulative:
                self._dataProvider.cumulativeLeaderboard = result.data
            else:
                self._dataProvider.leaderboard = result.data
            return
        LOG_WARNING('[Tamagotchi] Failed to retrieve leaderboard info', result.getExtraCode())
        if cumulative:
            self._dataProvider.cumulativeLeaderboard = None
        else:
            self._dataProvider.leaderboard = None
        return

    @adisp_process
    def requestPlayerStats(self, forFinalCache=False):
        asFinalCache = forFinalCache and self._dataProvider.canCacheFinalPlayerStats()
        if asFinalCache and not self._dataProvider.tryStartFinalPlayerStatsRequest():
            if self._dataProvider.hasFinalPlayerStatsCache:
                self._dataProvider.onPlayerStatsUpdated(True)
            return
        requestGeneration = self._dataProvider.playerStatsGeneration
        requestSeq = self._dataProvider.allocatePlayerStatsRequestSeq()
        startedWhenFinalReady = self._dataProvider.hasFinalPlayerStatsCache or self._dataProvider.canCacheFinalPlayerStats()
        result = yield self._webController.sendRequest(ctx=NyTamagotchiGetPlayerStatsCtx())
        if result.isSuccess():
            self._dataProvider.applyPlayerStats(result.data, asFinalCache=asFinalCache, startedWhenFinalReady=startedWhenFinalReady, requestGeneration=requestGeneration, requestSeq=requestSeq)
            return
        else:
            LOG_ERROR('[Tamagotchi] Failed to request player stats', result.getExtraCode())
            self._dataProvider.applyPlayerStats(None, asFinalCache=asFinalCache, startedWhenFinalReady=startedWhenFinalReady, requestGeneration=requestGeneration, requestSeq=requestSeq)
            return

    @adisp_process
    def buyItems(self, itemsDict):
        result = yield self._webController.sendRequest(ctx=NyTamagotchiBuyItemsCtx(items=itemsDict))
        if not result.isSuccess():
            LOG_ERROR('[Tamagotchi] Failed to buy items', result.getExtraCode())
        self._dataProvider.onItemsPurchased(result.isSuccess(), itemsDict)

    @adisp_process
    def activateItem(self, itemId, count):
        self._dataProvider.onItemsActivateRequested(itemId, count)
        result = yield self._webController.sendRequest(ctx=NyTamagotchiActivateItemCtx(itemId=itemId, count=count))
        isRecalculation = result.getExtraCode() == self._RECALCULATION_CODE
        if result.isSuccess():
            self._dataProvider.playerInfo = result.data
        elif not isRecalculation:
            LOG_ERROR('[Tamagotchi] Failed to activate items', result.getExtraCode())
        self._dataProvider.onItemsActivated(result.isSuccess(), itemId, count, isRecalculation)