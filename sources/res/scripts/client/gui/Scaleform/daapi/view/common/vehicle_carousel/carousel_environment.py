import constants
from CurrentVehicle import g_currentVehicle
from PlayerEvents import g_playerEvents
from account_helpers.settings_core import settings_constants
from gui.Scaleform import getButtonsAssetPath
from gui.Scaleform.daapi.view.common.filter_contexts import FilterSetupContext
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import CarouselDataProvider
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import CarouselFilter
from gui.Scaleform.daapi.view.meta.CarouselEnvironmentMeta import CarouselEnvironmentMeta
from gui.prb_control.ctrl_events import g_prbCtrlEvents
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared.formatters import text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency, i18n
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IRentalsController, IIGRController, IClanLockController, IEpicBattleMetaGameController, IRankedBattlesController, IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
_CAROUSEL_FILTERS = ('bonus', 'favorite', 'elite', 'premium')
if constants.IS_KOREA:
    _CAROUSEL_FILTERS += ('igr', )

def formatCountString(currentVehiclesCount, totalVehiclesCount):
    style = text_styles.error if currentVehiclesCount == 0 else text_styles.stats
    return ('{} / {}').format(style(currentVehiclesCount), text_styles.main(totalVehiclesCount))


class ICarouselEnvironment(object):

    @property
    def filter(self):
        return

    def applyFilter(self):
        pass

    def blinkCounter(self):
        pass

    def formatCountVehicles(self):
        pass

    def hasRentedVehicles(self):
        return False

    def hasEventVehicles(self):
        return False

    def setPopoverCallback(self, callback=None):
        pass

    def setRowCount(self, value):
        pass

    def hasRoles(self):
        return False

    def getCustomParams(self):
        return dict()

    def updateHotFilters(self):
        pass


class CarouselEnvironment(CarouselEnvironmentMeta, IGlobalListener, ICarouselEnvironment):
    rentals = dependency.descriptor(IRentalsController)
    igrCtrl = dependency.descriptor(IIGRController)
    clanLock = dependency.descriptor(IClanLockController)
    settingsCore = dependency.descriptor(ISettingsCore)
    itemsCache = dependency.descriptor(IItemsCache)
    epicController = dependency.descriptor(IEpicBattleMetaGameController)
    rankedController = dependency.descriptor(IRankedBattlesController)
    lobbyContext = dependency.descriptor(ILobbyContext)
    __battleSession = dependency.descriptor(IBattleSessionProvider)
    wotPlusController = dependency.descriptor(IWotPlusController)
    _DISABLED_FILTERS = []

    def __init__(self):
        super(CarouselEnvironment, self).__init__()
        self._usedFilters = self._getFilters()
        self._carouselDPConfig = {'carouselFilter': None, 
           'itemsCache': None}
        self._carouselDPCls = CarouselDataProvider
        self._carouselFilterCls = CarouselFilter
        self._carouselDP = None
        self._currentVehicle = None
        self.__filterPopoverRemoveCallback = None
        return

    def setPopoverCallback(self, callback=None):
        self.__filterPopoverRemoveCallback = callback

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        if accountInfo.isCurrentPlayer():
            self.updateAviability()

    def onUnitPlayerStateChanged(self, pInfo):
        if pInfo.isCurrentPlayer():
            self.updateAviability()

    def onPrbEntitySwitched(self):
        self.updateAviability()

    def onEnqueued(self, queueType, *args):
        self.updateAviability()

    def onDequeued(self, queueType, *args):
        self.updateAviability()

    def onUnitAutoSearchStarted(self, timeLeft):
        self.updateAviability()

    def onUnitAutoSearchFinished(self):
        self.updateAviability()

    @property
    def filter(self):
        if self._carouselDP is not None:
            return self._carouselDP.filter
        else:
            return

    def getTotalVehiclesCount(self):
        return self._carouselDP.getTotalVehiclesCount()

    def getCurrentVehiclesCount(self):
        return self._carouselDP.getCurrentVehiclesCount()

    def hasRentedVehicles(self):
        return self._carouselDP.hasRentedVehicles()

    def hasEventVehicles(self):
        return self._carouselDP.hasEventVehicles()

    def resetFilters(self):
        self.filter.reset()
        self.applyFilter()
        self.updateHotFilters()

    def updateHotFilters(self):
        hotFilters = [ False if key in self._DISABLED_FILTERS else self.filter.get(key) for key in self._usedFilters ]
        self.as_setCarouselFilterS({'hotFilters': hotFilters})

    def applyFilter(self):
        self._carouselDP.applyFilter()
        if not self.filter.isDefault():
            drawAttention = self._carouselDP.getCurrentVehiclesCount() == 0
            self.as_showCounterS(self.formatCountVehicles(), drawAttention)
        else:
            self.as_hideCounterS()

    def formatCountVehicles(self):
        return formatCountString(self._carouselDP.getCurrentVehiclesCount(), self._carouselDP.getTotalVehiclesCount())

    def blinkCounter(self):
        self.as_blinkCounterS()

    def selectVehicle(self, idx):
        if self.__battleSession.isReplayPlaying:
            return
        vInvID = self._carouselDP.selectVehicle(idx)
        if vInvID:
            self._currentVehicle.selectVehicle(vInvID)

    def updateVehicles(self, vehicles=None, filterCriteria=None):
        if self._carouselDP is not None:
            self._carouselDP.updateVehicles(vehicles, filterCriteria)
            self.applyFilter()
        return

    def updateAviability(self):
        if not self.isDisposed():
            state = self._currentVehicle.getViewState()
            self.as_setEnabledS(not state.isLocked())

    def _populate(self):
        super(CarouselEnvironment, self)._populate()
        self._currentVehicle = g_currentVehicle
        self._initDataProvider()
        setting = self.settingsCore.options.getSetting(settings_constants.GAME.VEHICLE_CAROUSEL_STATS)
        self._carouselDP.setShowStats(setting.get())
        self._carouselDP.setEnvironment(self.app)
        self._carouselDP.setFlashObject(self.as_getDataProviderS())
        self._carouselDP.buildList()
        self.rentals.onRentChangeNotify += self.__updateRent
        self.igrCtrl.onIgrTypeChanged += self.__updateIgrType
        self.clanLock.onClanLockUpdate += self.__updateClanLocks
        self.itemsCache.onSyncCompleted += self.__onCacheResync
        self._currentVehicle.onChanged += self.__onCurrentVehicleChanged
        self.epicController.onUpdated += self.__updateEpicSeasonRent
        self.rankedController.onUpdated += self.__updateRankedBonusBattles
        self.wotPlusController.onDataChanged += self.__onWotPlusChanged
        self.settingsCore.onSettingsChanged += self._onCarouselSettingsChange
        self.lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        g_playerEvents.onVehicleBecomeElite += self.__onVehicleBecomeElite
        g_prbCtrlEvents.onVehicleClientStateChanged += self.__onVehicleClientStateChanged
        self.startGlobalListening()
        self.applyFilter()
        self.updateAviability()
        self.as_setInitDataS({'counterCloseTooltip': makeTooltip('#tooltips:tanksFilter/counter/close/header', '#tooltips:tanksFilter/counter/close/body')})

    def _dispose(self):
        self.rentals.onRentChangeNotify -= self.__updateRent
        self.igrCtrl.onIgrTypeChanged -= self.__updateIgrType
        self.clanLock.onClanLockUpdate -= self.__updateClanLocks
        self.itemsCache.onSyncCompleted -= self.__onCacheResync
        self._currentVehicle.onChanged -= self.__onCurrentVehicleChanged
        self.epicController.onUpdated -= self.__updateEpicSeasonRent
        self.rankedController.onUpdated -= self.__updateRankedBonusBattles
        self.wotPlusController.onDataChanged -= self.__onWotPlusChanged
        self.lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        self.settingsCore.onSettingsChanged -= self._onCarouselSettingsChange
        g_playerEvents.onVehicleBecomeElite -= self.__onVehicleBecomeElite
        g_prbCtrlEvents.onVehicleClientStateChanged -= self.__onVehicleClientStateChanged
        self.stopGlobalListening()
        self._currentVehicle = None
        self._carouselDP.fini()
        self._carouselDP = None
        self._carouselDPConfig.clear()
        self.__callPopoverCallback()
        super(CarouselEnvironment, self)._dispose()
        return

    def _initDataProvider(self):
        self._carouselDPConfig.update({'carouselFilter': self._carouselFilterCls(), 
           'itemsCache': self.itemsCache})
        self._carouselDP = self._carouselDPCls(**self._carouselDPConfig)

    def _onCarouselSettingsChange(self, diff):
        if settings_constants.GAME.VEHICLE_CAROUSEL_STATS in diff:
            setting = self.settingsCore.options.getSetting(settings_constants.GAME.VEHICLE_CAROUSEL_STATS)
            self._carouselDP.setShowStats(setting.get())
            self._carouselDP.updateVehicles()

    @classmethod
    def _makeFilterVO(cls, filterID, contexts, filters):
        filterCtx = contexts.get(filterID, FilterSetupContext())
        return {'id': filterID, 
           'value': getButtonsAssetPath(filterCtx.asset or filterID), 
           'selected': filters[filterID], 
           'enabled': True, 
           'tooltip': makeTooltip(('#tank_carousel_filter:tooltip/{}/header').format(filterID), i18n.makeString(('#tank_carousel_filter:tooltip/{}/body').format(filterID), **filterCtx.ctx))}

    def __updateRent(self, vehicles):
        self.updateVehicles(vehicles)

    def __updateEpicSeasonRent(self, diff):
        self.updateVehicles(filterCriteria=REQ_CRITERIA.VEHICLE.SEASON_RENT)

    def __updateRankedBonusBattles(self):
        self.updateVehicles()

    def __updateIgrType(self, roomType, xpFactor):
        self.updateVehicles(filterCriteria=REQ_CRITERIA.VEHICLE.IS_PREMIUM_IGR)

    def __updateClanLocks(self, vehicles, isFull):
        if isFull:
            self.updateVehicles()
        else:
            self.updateVehicles(vehicles)

    def __onServerSettingChanged(self, diff):
        if constants.Configs.CRYSTAL_REWARDS_CONFIG in diff or constants.RENEWABLE_SUBSCRIPTION_CONFIG in diff:
            self.updateVehicles()
        if constants.RENEWABLE_SUBSCRIPTION_CONFIG in diff:
            self.updateAviability()

    def __onCacheResync(self, reason, diff):
        if reason in (CACHE_SYNC_REASON.SHOP_RESYNC, CACHE_SYNC_REASON.DOSSIER_RESYNC):
            self.updateVehicles()
            self.updateAviability()
            return
        if reason in (CACHE_SYNC_REASON.STATS_RESYNC,
         CACHE_SYNC_REASON.INVENTORY_RESYNC,
         CACHE_SYNC_REASON.CLIENT_UPDATE):
            self.updateAviability()
        if GUI_ITEM_TYPE.VEHICLE in diff:
            self.updateVehicles(diff.get(GUI_ITEM_TYPE.VEHICLE))

    def __onCurrentVehicleChanged(self):
        self.updateAviability()
        if self._carouselDP is not None:
            filteredIndex = self._carouselDP.findVehicleFilteredIndex(g_currentVehicle.item)
            if self._carouselDP.pyGetSelectedIdx() != filteredIndex and filteredIndex > -1:
                self._carouselDP.selectVehicle(filteredIndex)
                self._carouselDP.refresh()
            elif filteredIndex == -1:
                self._carouselDP.selectFilteredVehicle(g_currentVehicle.item)
        return

    def __onVehicleBecomeElite(self, *vehicles):
        self.updateVehicles(vehicles)

    def __onVehicleClientStateChanged(self, vehicles):
        self.updateVehicles(vehicles)

    def __onWotPlusChanged(self, diff):
        if 'isEnabled' in diff:
            self.updateVehicles()
            self.updateAviability()

    def __callPopoverCallback(self):
        if callable(self.__filterPopoverRemoveCallback):
            callback = self.__filterPopoverRemoveCallback
            self.__filterPopoverRemoveCallback = None
            callback()
        return

    def _getFilters(self):
        return _CAROUSEL_FILTERS