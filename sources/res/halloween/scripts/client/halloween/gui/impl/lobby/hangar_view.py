import logging
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from PlayerEvents import g_playerEvents
from gui.shared.event_dispatcher import showVehicleHubOverview
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter
from gui.impl.pub import WindowImpl
from gui.impl.pub.view_component import ViewComponent
from halloween.gui.impl.lobby.widgets.gsw_view import GswPresenter
from frameworks.wulf import WindowLayer, WindowStatus, WindowFlags
from notification import NotificationMVC
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.game_loading.resources.consts import Milestones
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.app_loader import sf_lobby
from gui.impl.gen import R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip
from gui.impl.lobby.hangar.presenters.utils import getSharedMenuItems
from gui.impl.lobby.tank_setup.ammunition_setup.base_hangar import BaseHangarAmmunitionSetupView
from gui.prb_control import prbEntityProperty, prb_getters
from gui.shared.events import AmmunitionPanelViewEvent
from gui.shared import EVENT_BUS_SCOPE, g_eventBus, events
from halloween.gui.impl.gen.view_models.views.lobby.hangar_view_model import HangarViewModel
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTypes
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_vehicle_view_model import VehicleStates
from halloween.gui.impl.lobby.hw_helpers import getVehicleState
from halloween.gui.impl.lobby.hw_ammunition_panel_view import HWAmmunitionPanelView
from halloween.gui.impl.lobby.widgets.carousel_view import CarouselView
from halloween.gui.impl.lobby.widgets.difficulty_view import DifficultyView
from halloween.gui.impl.lobby.widgets.meta_view import MetaWidgetView
from halloween.gui.halloween_account_settings import AccountSettingsKeys, getSettings, setSettings
from halloween.gui.shared.event_dispatcher import showHalloweenShopVehicle, showHWHangarAmmunitionSetupView, showIntroVideo, showInfoPage, showComparisonWindow
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController
from halloween.gui.sounds.sound_constants import HANGAR_SOUND_SETTINGS
from helpers import dependency, int2roman
from helpers.CallbackDelayer import CallbackDelayer
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.impl import IGuiLoader, INotificationWindowController
from skeletons.gui.shared.utils import IHangarSpace
from halloween.gui.impl.lobby.base_view import SwitcherPresenter
_BACKGROUND_ALPHA = 0.0
_logger = logging.getLogger(__name__)

class HangarView(ViewComponent[HangarViewModel]):
    _POP_UP_PADDING_X = 5
    _POP_UP_PADDING_Y = 112
    _appLoader = dependency.descriptor(IAppLoader)
    _guiLoader = dependency.descriptor(IGuiLoader)
    _hwController = dependency.descriptor(IHalloweenController)
    _hwArtefactsCtrl = dependency.descriptor(IHalloweenArtefactsController)
    _hangarSpace = dependency.descriptor(IHangarSpace)
    _notificationMgr = dependency.descriptor(INotificationWindowController)
    _COMMON_SOUND_SPACE = HANGAR_SOUND_SETTINGS

    def __init__(self, *args, **kwargs):
        super(HangarView, self).__init__(R.views.halloween.mono.lobby.hangar(), HangarViewModel, *args, **kwargs)
        self.__isUnitJoiningInProgress = False
        self.__timer = None
        self.__ammoPanel = None
        self.__metaWidget = None
        self.__selectedMissionIndex = 1
        self.__needSlideToNext = False
        return

    @property
    def viewModel(self):
        return super(HangarView, self).getViewModel()

    def createContextMenu(self, event):
        if self.__ammoPanel is not None:
            return self.__ammoPanel.createContextMenu(event)
        else:
            return super(HangarView, self).createContextMenu(event)

    def createToolTip(self, event):
        dialogsContainer = self.__app.containerManager.getContainer(WindowLayer.TOP_WINDOW)
        if dialogsContainer.getView(criteria={POP_UP_CRITERIA.VIEW_ALIAS: VIEW_ALIAS.LOBBY_MENU}):
            return None
        else:
            return super(HangarView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.common.tooltips.ExtendedTextTooltip():
            text = event.getArgument('text', '')
            stringifyKwargs = event.getArgument('stringifyKwargs', '')
            return ExtendedTextTooltip(text, stringifyKwargs)
        return super(HangarView, self).createToolTipContent(event, contentID)

    def selectSlideByArtefact(self, artefactID):
        self.viewModel.setSelectedSlide(self._hwArtefactsCtrl.getIndex(artefactID))

    def selectNextSlide(self):
        self.__needSlideToNext = True

    def updateSlide(self):
        self.__prepareSelectedArtefact()
        self.__fillCore()

    @prbEntityProperty
    def prbEntity(self):
        return

    def _onLoading(self, *args, **kwargs):
        super(HangarView, self)._onLoading()
        self.__timer = CallbackDelayer()
        self.__prepareSelectedArtefact()
        self.__fillCore()
        self.__fillGiftVehicle()
        self.__metaWidget.updateData(int(self.__selectedMissionIndex))
        self.__updateVehicleLocked()

    def _onLoaded(self, *args, **kwargs):
        super(HangarView, self)._onLoaded(*args, **kwargs)
        if g_currentPreviewVehicle is not None:
            g_currentPreviewVehicle.selectNoVehicle()
        if self._hangarSpace.spaceInited:
            self.__updateNotificationsLayout()
        else:
            g_playerEvents.onLoadingMilestoneReached += self.__onLoadingMilestoneReached
        return

    def _onShown(self):
        super(HangarView, self)._onShown()
        if getSettings(AccountSettingsKeys.IS_EVENT_NEW):
            showIntroVideo()
            setSettings(AccountSettingsKeys.IS_EVENT_NEW, False)

    def _finalize(self):
        notificationsModel = NotificationMVC.g_instance.getModel()
        if notificationsModel is not None:
            notificationsModel.onPopUpPaddingChanged(False)
        self.__ammoPanel = None
        self.__metaWidget = None
        super(HangarView, self)._finalize()
        return

    def _getEvents(self):
        return [
         (
          g_playerEvents.onPrebattleInvitationAccepted, self.__onPrebattleInvitationAccepted),
         (
          self._guiLoader.windowsManager.onWindowStatusChanged, self.__windowStatusChanged),
         (
          self.viewModel.onEscPressed, self.__onEscape),
         (
          self.viewModel.onExitClick, self.__onExitClick),
         (
          self.viewModel.onAboutClick, self.__onAboutClick),
         (
          self.viewModel.onTasksClick, self.__onTasksClick),
         (
          self.viewModel.onPacksClick, self.__onPacksClick),
         (
          self.viewModel.onViewLoaded, self.__onViewLoaded),
         (
          self.viewModel.onSlide, self.__onSlide),
         (
          self.viewModel.onPreview, self.__onPreview),
         (
          self.viewModel.onComparisonClick, self.__onComporisonClick),
         (
          self._hwArtefactsCtrl.onArtefactStatusUpdated, self.__onArtefactStatusUpdated),
         (
          self._hwArtefactsCtrl.onArtefactSettingsUpdated, self.__onArtefactSettingsUpdated),
         (
          self._hwController.onSettingsUpdate, self.__fillCore),
         (
          g_currentVehicle.onChanged, self.__onCurrentVehicleChanged),
         (
          g_currentPreviewVehicle.onChanged, self.__onCurrentVehicleChanged)]

    def _subscribe(self):
        super(HangarView, self)._subscribe()
        unitMgr = prb_getters.getClientUnitMgr()
        if unitMgr:
            unitMgr.onUnitJoined += self.__onUnitJoined
        g_eventBus.addListener(AmmunitionPanelViewEvent.SECTION_SELECTED, self.__onTankSetupChange, scope=EVENT_BUS_SCOPE.LOBBY)
        g_clientUpdateManager.addCallbacks({'cache.vehsLock': self.__onVehicleLockUpdated})

    def _unsubscribe(self):
        g_eventBus.removeListener(AmmunitionPanelViewEvent.SECTION_SELECTED, self.__onTankSetupChange, scope=EVENT_BUS_SCOPE.LOBBY)
        g_clientUpdateManager.removeObjectCallbacks(self)
        unitMgr = prb_getters.getClientUnitMgr()
        if unitMgr:
            unitMgr.onUnitJoined -= self.__onUnitJoined
        if self.__timer is not None:
            self.__timer.clearCallbacks()
            self.__timer = None
        g_playerEvents.onLoadingMilestoneReached -= self.__onLoadingMilestoneReached
        super(HangarView, self)._unsubscribe()
        return

    def _getChildComponents(self):
        self.__metaWidget = MetaWidgetView(parent=self)
        self.__ammoPanel = HWAmmunitionPanelView()
        self.setChildView(R.aliases.halloween.shared.AmmunitionPanel(), self.__ammoPanel)
        halloween = R.aliases.halloween.shared
        return {halloween.Switcher(): SwitcherPresenter, 
           halloween.Difficulty(): DifficultyView, 
           halloween.Carousel(): CarouselView, 
           R.aliases.hangar.shared.MainMenu(): lambda : MainMenuPresenter(getSharedMenuItems()), 
           halloween.Gsw(): GswPresenter, 
           halloween.Meta(): lambda : self.__metaWidget}

    def __selectNextSlide(self):
        if self.__metaWidget is not None:
            self.__metaWidget.updateData(int(self.__selectedMissionIndex))
        self._hwArtefactsCtrl.selectedArtefactID = None
        self.__prepareSelectedArtefact()
        self.viewModel.setSelectedSlide(self.__selectedMissionIndex)
        self.__needSlideToNext = False
        self.viewModel.setIsCompleted(self._hwArtefactsCtrl.getCurrentArtefactProgress() >= self._hwArtefactsCtrl.getMaxArtefactsProgress())
        return

    def __prepareSelectedArtefact(self):
        artefacts = self._hwArtefactsCtrl.artefactsSorted()
        if self._hwArtefactsCtrl.selectedArtefactID is None:
            artefactID = None
            if self._hwArtefactsCtrl.getCurrentArtefactProgress() >= self._hwArtefactsCtrl.getMaxArtefactsProgress():
                artefact = self._hwArtefactsCtrl.getFinalArtefact()
                artefactID = artefact.artefactID if artefact is not None else None
            else:
                for artefact in artefacts:
                    if not self._hwArtefactsCtrl.isArtefactOpened(artefact.artefactID):
                        artefactID = artefact.artefactID
                        break

            if artefactID is None and artefacts:
                artefactID = artefacts[0].artefactID
            self.__selectedMissionIndex = self._hwArtefactsCtrl.getIndex(artefactID) if artefactID is not None else 1
            self._hwArtefactsCtrl.selectedArtefactID = artefactID
        else:
            self.__selectedMissionIndex = self._hwArtefactsCtrl.getIndex(self._hwArtefactsCtrl.selectedArtefactID)
        return

    def __onVehicleLockUpdated(self, *args):
        if g_currentVehicle.item:
            self.viewModel.setIsVehicleInBattle(g_currentVehicle.item.isInBattle)

    def __onPrebattleInvitationAccepted(self, _, __):
        self.__isUnitJoiningInProgress = True
        self.__timer.delayCallback(15, self.__onResetUnitJoiningProgress)

    def __onResetUnitJoiningProgress(self):
        self.__isUnitJoiningInProgress = False

    def __onUnitJoined(self, _, __):
        self.__isUnitJoiningInProgress = False
        if self.__timer is not None:
            self.__timer.stopCallback(self.__onResetUnitJoiningProgress)
        return

    def __onArtefactStatusUpdated(self, _):
        if self._hwArtefactsCtrl.isArtefactOpened(self._hwArtefactsCtrl.selectedArtefactID):
            return
        self.__metaWidget.updateData(int(self.__selectedMissionIndex))

    def __onArtefactSettingsUpdated(self):
        self.__fillCore()
        self.__updateVehicleLocked()

    def __onSlide(self, args):
        if args is None:
            return
        else:
            slideIndex = int(args.get('slide', 1))
            self.viewModel.setSelectedSlide(slideIndex)
            self.__selectedMissionIndex = slideIndex
            self._hwArtefactsCtrl.selectedArtefactID = self._hwArtefactsCtrl.getArtefactIDByIndex(slideIndex)
            self.__metaWidget.updateData(slideIndex)
            return

    @sf_lobby
    def __app(self):
        return

    def __fillGiftVehicle(self):
        vehicle = self._hwArtefactsCtrl.getMainGiftVehicle()
        if vehicle is not None:
            with self.viewModel.transaction() as (tx):
                vehGift = tx.mainGiftVehicle
                vehGift.setName(vehicle.userName)
                vehGift.setLevel(int2roman(vehicle.level))
                vehGift.setIsPremium(vehicle.isPremium)
                vehGift.setVehicleType(VehicleTypes(vehicle.type) if vehicle.type != '' else VehicleTypes.NONE)
        return

    def __fillCore(self):
        with self.viewModel.transaction() as (tx):
            tx.setSelectedSlide(self.__selectedMissionIndex)
            tx.setSlidesCount(self._hwArtefactsCtrl.getArtefactsCount())
            tx.setIsCompleted(self._hwArtefactsCtrl.getCurrentArtefactProgress() >= self._hwArtefactsCtrl.getMaxArtefactsProgress())
            tx.setIsInfoPageEnabled(self._hwController.isInfoPageEnabled())

    def __updateVehicleLocked(self):
        vehicle = g_currentVehicle.item
        if vehicle is not None:
            vehicleLocked = getVehicleState(vehicle) == VehicleStates.LOCKED
            self.viewModel.setIsVehicleLocked(vehicleLocked)
            if vehicleLocked:
                missionID = self._hwArtefactsCtrl.getArtefactIDForAccessToVehicle(vehicle.intCD)
                if missionID is not None:
                    self.viewModel.setLockedMissionIndex(self._hwArtefactsCtrl.getIndex(missionID))
            self.viewModel.setIsVehicleInBattle(vehicle.isInBattle)
        return

    def __updateNotificationsLayout(self):
        notificationsModel = NotificationMVC.g_instance.getModel()
        if notificationsModel is not None:
            notificationsModel.onPopUpPaddingChanged(True, self._POP_UP_PADDING_X, self._POP_UP_PADDING_Y)
        return

    def __onLoadingMilestoneReached(self, milestoneName):
        if milestoneName == Milestones.HANGAR_READY:
            g_playerEvents.onLoadingMilestoneReached -= self.__onLoadingMilestoneReached
            self.__updateNotificationsLayout()

    def __onExitClick(self):
        if self.prbEntity and not self.prbEntity.hasLockedState():
            self._hwController.selectRandomMode()

    def __onAboutClick(self):
        showInfoPage()

    def __onComporisonClick(self):
        showComparisonWindow()

    def __onPreview(self, args):
        if args.get('isKingReward', False):
            vehicle = self._hwArtefactsCtrl.getMainGiftVehicle()
            if vehicle is not None:
                showVehicleHubOverview(vehicle.intCD)
        elif g_currentVehicle.item:
            showVehicleHubOverview(g_currentVehicle.item.intCD, outfit=g_currentVehicle.item.getOutfit(g_currentVehicle.item.getAnyOutfitSeason()))
        return

    def __onTasksClick(self):
        vehicle = g_currentVehicle.item
        if not vehicle:
            return
        else:
            missionID = self._hwArtefactsCtrl.getArtefactIDForAccessToVehicle(vehicle.intCD)
            if missionID is None:
                return
            self.__selectedMissionIndex = self._hwArtefactsCtrl.getIndex(missionID)
            self.viewModel.setSelectedSlide(self.__selectedMissionIndex)
            return

    def __onPacksClick(self):
        showHalloweenShopVehicle()

    def __onEscape(self):
        dialogsContainer = self.__app.containerManager.getContainer(WindowLayer.TOP_WINDOW)
        if not dialogsContainer.getView(criteria={POP_UP_CRITERIA.VIEW_ALIAS: VIEW_ALIAS.LOBBY_MENU}):
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_MENU)), scope=EVENT_BUS_SCOPE.LOBBY)

    def __onCurrentVehicleChanged(self):
        if g_currentVehicle.item is None:
            return
        else:
            self.__updateVehicleLocked()
            return

    def __onTankSetupChange(self, event):
        ctx = event.ctx
        if self._hangarSpace.spaceLoading():
            _logger.warning('Optional Device click was not handled (kwargs=%s). HangarSpace is currently  loading.', ctx)
        elif not self.__isUnitJoiningInProgress:
            with self.viewModel.transaction() as (tx):
                tx.setIsLoadedSetup(True)
            showHWHangarAmmunitionSetupView(**ctx)

    def __windowStatusChanged(self, uniqueID, newStatus):
        if newStatus == WindowStatus.LOADING:
            window = self._guiLoader.windowsManager.getWindow(uniqueID)
            if window is None or window.content is None:
                return
            if isinstance(window.content, BaseHangarAmmunitionSetupView):
                with self.viewModel.transaction() as (tx):
                    tx.setIsLoadedSetup(True)
            return
        if newStatus == WindowStatus.DESTROYING:
            window = self._guiLoader.windowsManager.getWindow(uniqueID)
            if window is None or window.content is None:
                return
            if isinstance(window.content, BaseHangarAmmunitionSetupView):
                with self.viewModel.transaction() as (tx):
                    tx.setIsLoadedSetup(False)
                return
        if newStatus == WindowStatus.DESTROYED:
            if self.__needSlideToNext and self._notificationMgr.activeQueueLength == 0:
                self.__selectNextSlide()
        return

    def __onViewLoaded(self):
        g_eventBus.handleEvent(events.ViewReadyEvent(self.layoutID))


class HangarWindow(WindowImpl):

    def __init__(self, layer, **kwargs):
        super(HangarWindow, self).__init__(content=HangarView(), wndFlags=WindowFlags.WINDOW, layer=layer)