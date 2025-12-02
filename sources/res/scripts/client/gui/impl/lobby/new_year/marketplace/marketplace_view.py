import BigWorld, logging, typing
from functools import partial
from itertools import chain
from operator import itemgetter
from ClientSelectableCameraObject import ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle, g_currentVehicle
from gui import SystemMessages
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.game_control.wallet import WalletController
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.ny_constants import Resource
from gui.impl.gen.view_models.views.lobby.new_year.views.marketplace.card_model import CardModel
from gui.impl.gen.view_models.views.lobby.new_year.views.marketplace.card_groups_model import CardGroupsModel
from gui.impl.gen.view_models.views.lobby.new_year.views.marketplace.ny_marketplace_view_model import KitState, VehicleState, NyMarketplaceViewModel
from gui.impl.lobby.new_year.dialogs.marketplace.market_purchase_dialog import MarketPurchaseDialogView
from gui.impl.lobby.new_year.ho_sidebar_component import ViewWithSidebarStateObserver
from gui.impl.lobby.new_year.marketplace import getMarketRewards, getMarketItemBonusesFromItem, getSettingsName, bonusChecker, showStyleFromMarketPlace
from gui.impl.lobby.new_year.scene_rotatable_view import SceneRotatableView
from gui.impl.lobby.new_year.states import MarketplaceState
from gui.impl.lobby.new_year.tooltips.ny_market_card_tooltip import NyMarketCardTooltip
from gui.impl.lobby.new_year.tooltips.ny_market_discount_tooltip import NyMarketDiscountTooltip
from gui.impl.lobby.new_year.tooltips.ny_market_lack_the_res_tooltip import NyMarketLackTheResTooltip
from gui.impl.lobby.new_year.tooltips.ny_resource_tooltip import NyResourceTooltip
from gui.impl.new_year.new_year_helper import backportTooltipDecorator
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
from gui.server_events.bonuses import CustomizationsBonus
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.shared.events import NyMarketPlaceRewardEvent, HangarCustomizationEvent, LobbySimpleEvent
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.notifications import NotificationPriorityLevel
from gui.shared.utils import decorators
from gui.shared.view_helpers.blur_manager import CachedBlur
from helpers import dependency
from items import vehicles
from items.components.ny_constants import NY_CURRENCY_NAME_TO_IDX, NyCurrency
from new_year.ny_constants import Collections, NyTabBarMarketplaceView, SyncDataKeys, RESOURCES_ORDER
from new_year.ny_marketplace_helper import getNYMarketplaceConfig, isCollectionItemReceived, getCollectionCompleteInfo, isCollectionReceived
from new_year.ny_processor import BuyMarketplaceItemProcessor
from new_year.ny_preview import getVehiclePreviewID
from shared_utils import findFirst, first
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.new_year import INewYearController
from skeletons.gui.game_control import IWalletController
_logger = logging.getLogger(__name__)
_DEFAULT_VEHICLE = 'germany:G42_Maus'
_DEFAULT_VEHICLES_2018 = {'soviet': 'ussr:R45_IS-7', 
   'traditionalWestern': 'france:F10_AMX_50B', 
   'modernWestern': 'japan:J20_Type_2605', 
   'asian': 'china:Ch41_WZ_111_5A'}
_EASING_TRANSITION_DURATION = 0.8

class _KitSettings(object):

    def __init__(self):
        self.__yearName = ''
        self.__kitId = 0
        self.__resource = Resource.CRYSTAL
        self.__styleID = None
        self.__openStyleOnVehicleInvID = None
        self.__findNotRecived = True
        return

    @property
    def yearName(self):
        return self.__yearName

    @property
    def kitId(self):
        return self.__kitId

    @property
    def resource(self):
        return self.__resource

    @property
    def resourceValue(self):
        return self.__resource.value

    @property
    def styleID(self):
        return self.__styleID

    @property
    def openStyleOnVehicle(self):
        return self.__openStyleOnVehicleInvID

    @property
    def findNotRecived(self):
        return self.__findNotRecived

    def getCategoryIndex(self):
        return NyTabBarMarketplaceView.REVERSED_ALL.index(self.__yearName)

    def getResourceIndex(self):
        return NY_CURRENCY_NAME_TO_IDX.get(self.resourceValue)

    def setYearName(self, value):
        self.__yearName = value

    def setKitId(self, value):
        self.__kitId = value

    def setResource(self, value):
        self.__resource = value

    def setStyleID(self, value):
        self.__styleID = value

    def setOpenStyleOnVehicle(self, value):
        self.__openStyleOnVehicleInvID = value

    def setFindNotRecived(self, value):
        self.__findNotRecived = value


class MarketplaceView(SceneRotatableView, SubModelPresenter):
    _VEHICLE_COLLISION_AUTO_ACTIVATE = True
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __service = dependency.descriptor(ICustomizationService)
    __nyController = dependency.descriptor(INewYearController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __c11n = dependency.descriptor(ICustomizationService)
    _wallet = dependency.descriptor(IWalletController)

    def __init__(self, model, parent):
        super(MarketplaceView, self).__init__(model, parent)
        self._tooltips = {}
        self.__settings = _KitSettings()
        self.__needToResetAppearance = False
        self.__needResetBloor = False
        self.__cameraCallbackId = None
        self.__blur = None
        self.__currentPreviewVehicle = None
        self.__currentPreviewStyle = None
        self.__stateObserver = None
        _, self.__tabName = self.__nyController.getFirstNonReceivedMarketPlaceCollectionData()
        self.__currentYearName = None
        return

    def initialize(self, *args, **kwargs):
        self.__stateObserver = ViewWithSidebarStateObserver(MarketplaceState)
        super(MarketplaceView, self).initialize(args, kwargs)
        self.__blur = CachedBlur(fadeTime=_EASING_TRANSITION_DURATION)
        tabName = self.__tabName
        self.__settings.setResource(max([ (r, self.__nyController.currencies.getResouceBalance(r.value)) for r in RESOURCES_ORDER
                                        ], key=itemgetter(1))[0])
        lsm = getLobbyStateMachine()
        lsm.connect(self.__stateObserver)
        self.__onTabSelect(tabName, kitIdx=self.__settings.kitId)

    def finalize(self):
        super(MarketplaceView, self).finalize()
        self.__currentPreviewVehicle = None
        g_eventBus.removeListener(LobbySimpleEvent.VEHICLE_PREVIEW_HIDDEN, self.__closeHeroTank, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__closeC11n, scope=EVENT_BUS_SCOPE.LOBBY)
        self.__clearCalbackId()
        self.__unsubscribeVehicleChange()
        self._tooltips.clear()
        self.__resetAppearance()
        if self.__blur:
            self.__resetBlur()
            self.__blur.fini()
            self.__blur = None
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__stateObserver)
        self.__stateObserver.clear()
        self.__stateObserver = None
        return

    @backportTooltipDecorator()
    def createToolTip(self, event):
        return super(MarketplaceView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.mono.holiday_ops.tooltips.ho_market_discount_tooltip():
            return NyMarketDiscountTooltip(int(event.getArgument('discount')), str(event.getArgument('collection')), str(event.getArgument('year')), int(event.getArgument('prevNYLevel')), int(event.getArgument('currentToysCount')), int(event.getArgument('totalToysCount')))
        if contentID == R.views.mono.holiday_ops.tooltips.ho_market_lack_the_res_tooltip():
            return NyMarketLackTheResTooltip(str(event.getArgument('resourceType')), int(event.getArgument('price')))
        if contentID == R.views.mono.holiday_ops.tooltips.ho_market_card_tooltip():
            return NyMarketCardTooltip(str(event.getArgument('kitState')), str(event.getArgument('kitName')), str(event.getArgument('currentTabName')), int(event.getArgument('kitIndex')), str(event.getArgument('currentResource')), int(event.getArgument('prevNYLevel')), int(event.getArgument('currentToysCount')), int(event.getArgument('totalToysCount')))
        if contentID == R.views.mono.holiday_ops.tooltips.ho_resource_tooltip():
            resourceType = event.getArgument('type')
            return NyResourceTooltip(resourceType)
        return super(MarketplaceView, self).createToolTipContent(event, contentID)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _getEvents(self):
        events = super(MarketplaceView, self)._getEvents()
        return events + (
         (
          self.viewModel.kit.onBuy, self.__onKitBuy),
         (
          self.viewModel.kit.onSwitchResource, self.__onKitSwitchResource),
         (
          self.viewModel.kit.onOpenStyle, self.__onKitOpenStyle),
         (
          self.viewModel.onSwitchKit, self.__onCardsSwitchKit),
         (
          self.__stateObserver.onSidebarSelected, self.__onSideBarSelected),
         (
          self.__hangarSpace.onVehicleChangeStarted, self.__onVehicleChangeStarted),
         (
          self.__hangarSpace.onVehicleChanged, self.__onVehicleChanged),
         (
          self.__nyController.onDataUpdated, self.__onNyDataUpdate),
         (
          self.__nyController.currencies.onBalanceUpdated, self.__onBalanceUpdated),
         (
          self._wallet.onWalletStatusChanged, self.__onWalletStatusChanged))

    def _getCallbacks(self):
        return (
         (
          'inventory', self.__onInventoryUpdate),
         (
          'cache', self.__onCacheUpdated))

    def _getListeners(self):
        listeners = super(MarketplaceView, self)._getListeners()
        return listeners + (
         (
          NyMarketPlaceRewardEvent.ON_VEHICLE_APPEARANCE_RESET, self.__onTryStyleOpen, EVENT_BUS_SCOPE.LOBBY),)

    def __onTryStyleOpen(self, event):
        self.__needToResetAppearance = False

    def __unsubscribeVehicleChange(self):
        entity = self.__hangarSpace.getVehicleEntity()
        if entity and entity.appearance:
            entity.appearance.loadState.unsubscribe(self.__onVehicleLoadFinished, self.__onVehicleLoadStarted)

    def __subscribeVehicleChange(self):
        entity = self.__hangarSpace.getVehicleEntity()
        if entity and entity.appearance:
            entity.appearance.loadState.subscribe(self.__onVehicleLoadFinished, self.__onVehicleLoadStarted)

    def __onVehicleLoadStarted(self):
        pass

    def __onVehicleLoadFinished(self):
        self.__resetBlur()

    def __onSideBarSelected(self, tabName, _):
        if tabName == self.__tabName or tabName == 'entry':
            return
        self.__settings.setFindNotRecived(True)
        self.__onTabSelect(tabName, kitIdx=0)

    def __onTabSelect(self, tabName, kitIdx=0):
        self.__tabName = tabName
        self.__updateModel(tabName, kitIdx)

    def __updateModel(self, tabName, kitIdx=0):
        if tabName == NyTabBarMarketplaceView.PREVIOUS_CATEGORY:
            years = NyTabBarMarketplaceView.REVERSED_PREVIOUS_CATEGORIES
            self.__settings.setYearName(self.__getFirstNotReceivedYearForPrevCategory())
            self.__selectCard(self.__getFirstNotReceivedYearForPrevCategory(), kitIdx)
        else:
            years = [
             tabName]
            self.__settings.setYearName(tabName)
            self.__selectCard(tabName, kitIdx)
        with self.viewModel.transaction() as (model):
            model.setCurrentTabName(tabName)
            cardGroups = model.getCardGroups()
            cardGroups.clear()
            for year in years:
                cards = CardGroupsModel()
                cards.setYearName(year)
                self.__setCards(year, cards)
                cardGroups.addViewModel(cards)

            cardGroups.invalidate()

    @staticmethod
    def __getFirstNotReceivedYearForPrevCategory():
        for year in NyTabBarMarketplaceView.REVERSED_PREVIOUS_CATEGORIES:
            if not isCollectionReceived(year):
                return year

        return NyTabBarMarketplaceView.REVERSED_PREVIOUS_CATEGORIES[0]

    def __setCards(self, yearName, model):
        config = getNYMarketplaceConfig()
        items = config.getCategoryItems(yearName)
        cards = model.getCards()
        cards.clear()
        prevNYLevel = self.__itemsCache.items.festivity.getPrevNYLevel(yearName)
        collectionDistributions = self.__itemsCache.items.festivity.getCollectionDistributions()
        for index, item in enumerate(items):
            kitState = self.__getKitState(item, yearName)
            kitName = getSettingsName(item)
            discount = item.calculateDiscount(collectionDistributions, bonusChecker, prevNYLevel)
            card = CardModel()
            card.setKitIndex(index)
            card.setKitState(kitState.value)
            card.setKitName(kitName)
            card.setDiscount(discount)
            current, total = getCollectionCompleteInfo(item)
            card.setCurrentToysCount(current)
            card.setTotalToysCount(total)
            cards.addViewModel(card)

        cards.invalidate()

    def __selectCard(self, yearName, kitIdx):
        self.__currentYearName = yearName
        self.__settings.setYearName(yearName)
        isCamMoving = self.__cameraCallbackId is not None
        self.__clearCalbackId()
        kitIdx = self.__tryFindNotRecived(yearName, kitIdx)
        config = getNYMarketplaceConfig()
        item = config.getCategoryItem(yearName, kitIdx)
        if item is None:
            return
        else:
            self.__settings.setKitId(kitIdx)
            styleId = self.__getStyleFromRewards(item)
            prevStyle = self.__settings.styleID
            self.__settings.setStyleID(styleId)
            collectionName = getSettingsName(item)
            if styleId:
                self.__needResetBloor = prevStyle is None
                if isCamMoving:
                    self.__resetBlur()
                self.__showStyle(yearName, collectionName, styleId)
                self.__updateKitModel(collectionName, item, styleId, False)
            else:
                self.viewModel.setIsInteractive(False)
                self._resetCamera(duration=_EASING_TRANSITION_DURATION)
                self.__cameraCallbackId = BigWorld.callback(_EASING_TRANSITION_DURATION, partial(self.__updateKitModel, collectionName, item, None, True))
                self.__blur.enable()
            return

    def __updateKitModel(self, collectionName, item, styleId, removeVehicle):
        self.__cameraCallbackId = None
        prevNYLevel = self.__itemsCache.items.festivity.getPrevNYLevel(self.__currentYearName)
        if removeVehicle:
            self.__hangarSpace.removeVehicle()
            g_currentPreviewVehicle.destroy()
            g_currentPreviewVehicle.resetAppearance()
        kitState = self.__getKitState(item, self.__currentYearName)
        kitRewards = getMarketRewards(item, isMerge=True)
        installedOn = ''
        if styleId:
            style = self.__service.getItemByID(GUI_ITEM_TYPE.STYLE, styleId)
            vehicleIntCDs = style.getInstalledVehicles()
            if vehicleIntCDs:
                vehNames = map(self.__getVehicleShortName, vehicleIntCDs)
                installedOn = (',').join(vehNames)
        with self.viewModel.transaction() as (model):
            kit = model.kit
            kit.setStyleOnVehicle(installedOn)
            rewards = kit.getRewards()
            rewards.clear()
            for index, (bonus, tooltip) in enumerate(kitRewards):
                tooltipId = str(index)
                bonus.setTooltipId(tooltipId)
                bonus.setIndex(index)
                self._tooltips[tooltipId] = tooltip
                rewards.addViewModel(bonus)

            rewards.invalidate()
            resources = kit.getResources()
            resources.clear()
            for currency in NyCurrency.ALL:
                resources.addString(currency)

            resources.invalidate()
            model.setKitState(kitState)
            model.setCurrentKitName(collectionName)
            model.setCurrentYear(self.__currentYearName)
            model.setIsInteractive(True)
            model.setPrevNYLevel(prevNYLevel)
        self.__updatePrice()
        return

    def __updatePrice(self):
        collectionDistributions = self.__itemsCache.items.festivity.getCollectionDistributions()
        prevNYLevel = self.__itemsCache.items.festivity.getPrevNYLevel(self.__currentYearName)
        config = getNYMarketplaceConfig()
        item = config.getCategoryItem(self.__currentYearName, self.__settings.kitId)
        if item is None:
            return
        else:
            with self.viewModel.transaction() as (model):
                priceWithDiscount = item.getTotalPrice(collectionDistributions, bonusChecker, prevNYLevel)
                currency = self.__settings.resourceValue
                balance = self.__nyController.currencies.getResouceBalance(currency)
                self.__updateWalletStatus(model)
                kit = model.kit
                kit.setCurrentResource(currency)
                kit.setPrice(item.getPrice())
                kit.setPriceWithDiscount(priceWithDiscount)
                kit.setDiscount(item.calculateDiscount(collectionDistributions, bonusChecker, prevNYLevel))
                kit.setNotEnoughResource(priceWithDiscount > balance)
            return

    @staticmethod
    def __getStyleFromRewards(item):
        rewards = []
        bonuses = [ bonus for bonus in getMarketItemBonusesFromItem(item) if isinstance(bonus, CustomizationsBonus) ]
        for bonus in bonuses:
            rewards.extend(bonus.getCustomizations())

        style = findFirst(lambda r: r.get('custType') == 'style', rewards)
        if style:
            return style.get('id')
        else:
            return

    def __showStyle(self, yearName, collectionName, styleId):
        style = self.__service.getItemByID(GUI_ITEM_TYPE.STYLE, styleId)
        if not style:
            return
        vehicleIntCDs = style.getInstalledVehicles()
        if vehicleIntCDs:
            vehicleIntCD = first(vehicleIntCDs)
        else:
            vehicleIntCD = getVehiclePreviewID(style, inInventory=True)
        if not vehicleIntCD:
            if yearName != Collections.NewYear18:
                vehTypeName = _DEFAULT_VEHICLE
            else:
                vehTypeName = _DEFAULT_VEHICLES_2018.get(collectionName)
            if vehTypeName:
                vehDescr = vehicles.VehicleDescr(typeName=vehTypeName)
                vehicleIntCD = vehDescr.type.compactDescr
        if not vehicleIntCD:
            return
        vehicleEntity = self.__hangarSpace.getVehicleEntity()
        isVehicleLoaded = vehicleEntity.isVehicleLoaded
        if g_currentPreviewVehicle.item and g_currentPreviewVehicle.item.intCD == vehicleIntCD and style.mayInstall(g_currentPreviewVehicle.item):
            if isVehicleLoaded:
                g_currentPreviewVehicle.previewStyle(style)
            else:
                self.__loadVehicle(g_currentPreviewVehicle.item, style)
        else:
            vehicle = self.__itemsCache.items.getItemByCD(vehicleIntCD)
            if style.mayInstall(vehicle):
                self.__loadVehicle(vehicle, style)

    def __loadVehicle(self, vehicle, style=None):
        self.__currentPreviewVehicle = vehicle
        self.__currentPreviewStyle = style
        if self.__c11n.getCtx():
            g_eventBus.addListener(HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__closeC11n, scope=EVENT_BUS_SCOPE.LOBBY)
            return
        if g_currentPreviewVehicle.isHeroTank:
            g_eventBus.addListener(LobbySimpleEvent.VEHICLE_PREVIEW_HIDDEN, self.__closeHeroTank, EVENT_BUS_SCOPE.LOBBY)
            return
        self.__updateVehicle(vehicle, style)

    def __updateVehicle(self, vehicle, style):
        ClientSelectableCameraObject.deselectAll()
        self.__needToResetAppearance = True
        g_currentPreviewVehicle.selectHeroTank(False)
        g_currentPreviewVehicle.selectVehicle(vehicle.intCD, None, style, showWaitingBg=False)
        return

    def __closeC11n(self, *_):
        g_eventBus.removeListener(HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__closeC11n, scope=EVENT_BUS_SCOPE.LOBBY)
        if self.__currentPreviewVehicle:
            self.__updateVehicle(self.__currentPreviewVehicle, self.__currentPreviewStyle)
        self.__currentPreviewVehicle = None
        self.__currentPreviewStyle = None
        return

    def __closeHeroTank(self, *_):
        g_eventBus.removeListener(LobbySimpleEvent.VEHICLE_PREVIEW_HIDDEN, self.__closeHeroTank, EVENT_BUS_SCOPE.LOBBY)
        if self.__currentPreviewVehicle:
            self.__updateVehicle(self.__currentPreviewVehicle, self.__currentPreviewStyle)
        self.__currentPreviewVehicle = None
        self.__currentPreviewStyle = None
        return

    def __onKitBuy(self):
        self.__buyCollectionKit(self.__settings)

    def __onKitSwitchResource(self, args):
        resourceValue = args.get('resource')
        resource = first([ item for item in Resource if item.value == resourceValue ], Resource.CRYSTAL)
        self.__settings.setResource(resource)
        self.__updatePrice()

    def __onKitOpenStyle(self):
        vehicle = g_currentPreviewVehicle.item
        actualVehicle = self.__itemsCache.items.getItemByCD(vehicle.intCD) if vehicle else None
        if not actualVehicle or not actualVehicle.isCustomizationEnabled():
            return
        if g_currentVehicle.isInBattle():
            g_currentVehicle.selectVehicle(actualVehicle.invID, callback=self.__onKitOpenStyle)
            return
        else:
            self.__settings.setOpenStyleOnVehicle(actualVehicle.invID)
            self.__hangarSpace.onVehicleChanged += self.__delayedShowCustomization
            self.__hangarSpace.onSpaceChanged += self.__delayedShowCustomization
            self.__resetAppearance()
            return

    def __delayedShowCustomization(self):
        self.__hangarSpace.onVehicleChanged -= self.__delayedShowCustomization
        self.__hangarSpace.onSpaceChanged -= self.__delayedShowCustomization
        showStyleFromMarketPlace(self.__settings.styleID, self.__settings.openStyleOnVehicle)

    def __onCardsSwitchKit(self, args):
        kitIdx = int(args.get('kitIndex'))
        yearName = str(args.get('year'))
        self.__currentYearName = yearName
        if kitIdx >= 0:
            self.__selectCard(self.__currentYearName, kitIdx)

    def __getKitState(self, item, year):
        if isCollectionItemReceived(item, year):
            return KitState.RECEIVED
        if self.__nyController.isMaxAtmosphereLevel():
            return KitState.AVAILABLE
        return KitState.UNAVAILABLE

    def __tryFindNotRecived(self, yearName, kitIdx):
        if self.__settings.findNotRecived:
            config = getNYMarketplaceConfig()
            items = config.getCategoryItems(yearName)
            for index in chain(xrange(0, kitIdx), xrange(kitIdx, len(items))):
                if self.__getKitState(items[index], yearName) != KitState.RECEIVED:
                    kitIdx = index
                    break

            self.__settings.setFindNotRecived(False)
        return kitIdx

    @decorators.adisp_process('newYear/buyCollectionWaiting')
    def __buyCollectionKit(self, kitSettings):
        config = getNYMarketplaceConfig()
        item = config.getCategoryItem(kitSettings.yearName, kitSettings.kitId)
        dialog = MarketPurchaseDialogView(kitSettings.yearName, kitSettings.kitId, kitSettings.resource)
        self.__settings.setFindNotRecived(True)
        result = yield BuyMarketplaceItemProcessor(item, kitSettings.getCategoryIndex(), kitSettings.kitId, kitSettings.resourceValue, dialog).request()
        if result.userMsg:
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType, priority=NotificationPriorityLevel.MEDIUM)
        else:
            self.__settings.setFindNotRecived(False)

    def __onNyDataUpdate(self, diff, _):
        if SyncDataKeys.POINTS in diff:
            self.__updateKitState()

    def __onInventoryUpdate(self, invDiff):
        if GUI_ITEM_TYPE.CUSTOMIZATION in invDiff:
            self.__updateModel(self.__tabName, self.__settings.kitId)

    def __onCacheUpdated(self, diff):
        if 'vehsLock' in diff:
            self.__updateVehicleState()

    def __resetAppearance(self):
        if self.__needToResetAppearance:
            g_currentPreviewVehicle.selectNoVehicle()
            g_currentPreviewVehicle.resetAppearance()
            self.__needToResetAppearance = False

    def __updateKitState(self):
        config = getNYMarketplaceConfig()
        with self.viewModel.transaction() as (model):
            items = config.getCategoryItems(self.__settings.yearName)
            kitState = self.__getKitState(items[self.__settings.kitId], self.__currentYearName)
            model.setKitState(kitState)
            cardGroups = model.getCardGroups()
            for group in cardGroups:
                cards = group.getCards()
                groupItems = config.getCategoryItems(str(group.getYearName()))
                for card in cards:
                    index = card.getKitIndex()
                    if 0 <= index < len(groupItems):
                        item = groupItems[index]
                        kitState = self.__getKitState(item, group.getYearName())
                        card.setKitState(kitState.value)

                cards.invalidate()

            cardGroups.invalidate()

    def __onVehicleChanged(self):
        self.__subscribeVehicleChange()

    def __onVehicleChangeStarted(self):
        self.__unsubscribeVehicleChange()
        self.__updateVehicleState()

    def __onBalanceUpdated(self):
        self.__updatePrice()
        self.__updateKitState()

    def __clearCalbackId(self):
        if self.__cameraCallbackId is not None:
            BigWorld.cancelCallback(self.__cameraCallbackId)
            self.__cameraCallbackId = None
        return

    def __resetBlur(self):
        if self.__needResetBloor:
            self.__needResetBloor = False
            self.__blur.disable()

    def __getVehicleShortName(self, vehicleCD):
        return self.__itemsCache.items.getItemByCD(vehicleCD).shortUserName

    def __updateVehicleState(self):
        vehicle = g_currentPreviewVehicle.item
        actualVehicle = self.__itemsCache.items.getItemByCD(vehicle.intCD) if vehicle else None
        if actualVehicle:
            with self.viewModel.transaction() as (model):
                model.setIsVehicleCustomizationEnabled(actualVehicle.isCustomizationEnabled())
                if actualVehicle.isCustomizationEnabled():
                    model.setVehicleState(VehicleState.DEFAULT)
                elif not actualVehicle.isInInventory:
                    model.setVehicleState(VehicleState.NOT_IN_INVENTORY)
                elif actualVehicle.isInUnit:
                    model.setVehicleState(VehicleState.IN_UNIT)
                elif actualVehicle.isBroken:
                    model.setVehicleState(VehicleState.BROKEN)
                elif actualVehicle.isInBattle:
                    model.setVehicleState(VehicleState.IN_BATTLE)
                else:
                    model.setVehicleState(VehicleState.CUSTOMIZATION_UNAVAILABLE)
        return

    def __onWalletStatusChanged(self, _):
        with self.viewModel.transaction() as (model):
            self.__updateWalletStatus(model)

    def __updateWalletStatus(self, model):
        currencyStatus = self._wallet.dynamicComponentsStatuses.get(self.__settings.resource.value)
        model.setIsWalletAvailable(currencyStatus == WalletController.STATUS.AVAILABLE)