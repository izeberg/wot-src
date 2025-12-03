import typing
from PlayerEvents import g_playerEvents
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_resource_model import NyResourceModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_resources_balance_model import CollectState, NyResourcesBalanceModel
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_resource_collector_tooltip_model import CollectorTooltipType
from gui.impl.lobby.new_year.observers import HolidayOpsObserver
from gui.impl.lobby.new_year.popovers.ny_resources_convert_popover import NyResourcesConvertPopover
from gui.impl.lobby.new_year.states import GladeResourcesState
from gui.impl.lobby.new_year.tooltips.ny_resource_collector_tooltip import NyResourceCollectorTooltip
from gui.impl.lobby.new_year.tooltips.ny_resource_tooltip import NyResourceTooltip
from gui.impl.new_year.navigation import NewYearNavigation
from gui.impl.pub.view_component import ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import NyResourcesEvent
from gui.shared.utils.scheduled_notifications import PeriodicNotifier
from helpers import dependency, time_utils
from items.components.ny_constants import NyCurrency
from new_year.ny_constants import NYObjects, NyWidgetTopMenu, RESOURCES_ORDER
from new_year.ny_helper import getNYGeneralConfig
from new_year.ny_resource_collecting_helper import getCollectingCooldownTime, isCollectingAvailable, isExtraCollectingAvailable
from new_year.ny_trigger_hints import TriggerHintsStates
from shared_utils import findFirst
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IWalletController
from skeletons.new_year import IFriendServiceController, INewYearTriggerHintsController, INewYearController
if typing.TYPE_CHECKING:
    from frameworks.wulf.view.view import View, ViewEvent

class HOBalanceWidget(ViewComponent[NyResourcesBalanceModel]):
    __friendsService = dependency.descriptor(IFriendServiceController)
    __settingsCore = dependency.descriptor(ISettingsCore)
    __wallet = dependency.descriptor(IWalletController)
    __triggerHintsController = dependency.descriptor(INewYearTriggerHintsController)
    _nyController = dependency.descriptor(INewYearController)
    _friendsService = dependency.descriptor(IFriendServiceController)

    def __init__(self):
        super(HOBalanceWidget, self).__init__(model=NyResourcesBalanceModel)
        self.__lockForCustomAnimation = False
        self.__notifier = None
        self.__currentView = None
        self.__lsmObserver = HolidayOpsObserver()
        return

    @property
    def viewModel(self):
        return super(HOBalanceWidget, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        tooltips = R.views.mono.holiday_ops.tooltips
        if contentID == tooltips.ho_resource_tooltip():
            resourceType = event.getArgument('type')
            return NyResourceTooltip(resourceType)
        if contentID == tooltips.ho_resource_collector_tooltip():
            collectorTooltipType = CollectorTooltipType(event.getArgument('type'))
            return NyResourceCollectorTooltip(collectorTooltipType)
        return super(HOBalanceWidget, self).createToolTipContent(event, contentID)

    def createPopOverContent(self, event):
        if event.contentID == R.views.mono.holiday_ops.popovers.ho_resources_convert_popover():
            return NyResourcesConvertPopover()
        return super(HOBalanceWidget, self).createPopOverContent(event)

    def _initialize(self, *args, **kwargs):
        super(HOBalanceWidget, self)._initialize(*args, **kwargs)
        self.__notifier = PeriodicNotifier(lambda : time_utils.ONE_SECOND, self.__updateCollecting, periods=(
         time_utils.ONE_SECOND,))

    def _onLoading(self, *args, **kwargs):
        super(HOBalanceWidget, self)._onLoading(args, kwargs)
        lsm = getLobbyStateMachine()
        lsm.connect(self.__lsmObserver)
        self.__updatePanel()

    def _finalize(self):
        self.__notifier.stopNotification()
        self.__notifier.clear()
        super(HOBalanceWidget, self)._finalize()
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__lsmObserver)
        self.__lsmObserver.clear()
        self.__lsmObserver = None
        return

    def _getEvents(self):
        return (
         (
          self._nyController.currencies.onBalanceUpdated, self.__onBalanceUpdated),
         (
          self.viewModel.onCollectResources, self.__onCollectResources),
         (
          self.viewModel.onGoToResources, self.__onGoToResources),
         (
          self.__lsmObserver.onNavigationChanged, self.__switchSubView),
         (
          self._nyController.onDataUpdated, self.__onDataUpdated),
         (
          self.__triggerHintsController.onStateChanged, self.__onTriggerHintsStateChanged),
         (
          self._nyController.resourceCollecting.onCollectingUpdateLock, self.__onCollectingUpdateLock),
         (
          self._nyController.resourceCollecting.onCollectingUpdateResource, self.__onCollectingUpdateResource),
         (
          g_playerEvents.onDisconnected, self.__stopNotification),
         (
          self.__wallet.onWalletStatusChanged, self.__onWalletChanged))

    def __switchSubView(self, menuName):
        self.__currentView = menuName
        self.__updatePanel()
        self.viewModel.setIsFriendHangar(menuName in NyWidgetTopMenu.ALL_FRIEND_HANGAR)

    def _getListeners(self):
        return (
         (
          NyResourcesEvent.RESOURCE_COLLECTED, self.__onResourceCollected, EVENT_BUS_SCOPE.LOBBY),)

    def __onCollectResources(self):
        if self.__isResourcesTabOpened:
            return
        if self.__friendsService.isInFriendHangar:
            self.__friendsService.leaveFriendHangar()
        GladeResourcesState.goTo(instantly=True)

    def __onGoToResources(self):
        self.__onCollectResources()

    def __onDataUpdated(self, *_):
        self.__updatePanel()

    def __onTriggerHintsStateChanged(self):
        self.__updatePanel()

    def __updatePanel(self):
        if not self.__currentView:
            return
        with self.viewModel.transaction() as (model):
            model.setIsResourcesTabOpen(self.__isResourcesTabOpened)
            self.__updateCollecting(model=model)
        self.__updateResources()

    def __getCollectState(self):
        if isCollectingAvailable():
            if not self.__wallet.isAvailable:
                return CollectState.UNAVAILABLE
            if isExtraCollectingAvailable():
                return CollectState.AVAILABLEEXTRA
            return CollectState.AVAILABLE
        eventEndTimeTill = getNYGeneralConfig().getEventEndTime() - time_utils.getServerUTCTime()
        if getCollectingCooldownTime() > eventEndTimeTill:
            return CollectState.FINISHED
        return CollectState.COLLECTED

    @replaceNoneKwargsModel
    def __updateCollecting(self, model=None):
        state = self.__getCollectState()
        cooldown = getCollectingCooldownTime()
        model.setCollectState(state)
        model.setCollectCooldown(cooldown)
        if cooldown > 0:
            self.__notifier.startNotification()
        else:
            self.__notifier.stopNotification()

    def __stopNotification(self):
        self.__notifier.stopNotification()

    def __onWalletChanged(self, _):
        self.__updatePanel()
        with self.viewModel.transaction() as (model):
            model.setIsWalletAvailable(self.__wallet.isAvailable)

    def __updateResources(self):
        if self.__lockForCustomAnimation:
            return
        with self.viewModel.transaction() as (model):
            model.setIsHintVisible(self.__triggerHintsController.triggerHintsState == TriggerHintsStates.RESOURCES and self.__currentView != NyWidgetTopMenu.GLADE)
            model.setIsWalletAvailable(self.__wallet.isAvailable)
            resources = model.getResources()
            resources.clear()
            for resource in RESOURCES_ORDER:
                amount = self._nyController.currencies.getResouceBalance(resource.value)
                resourceModel = NyResourceModel()
                resourceModel.setType(resource.value)
                resourceModel.setValue(amount)
                resources.addViewModel(resourceModel)

            resources.invalidate()

    def __updateResource(self, resourceID):
        if not self.__lockForCustomAnimation or resourceID not in NyCurrency.ALL:
            return
        with self.viewModel.transaction() as (model):
            resources = model.getResources()
            for resourceModel in resources:
                if resourceModel.getType() == resourceID:
                    amount = self._nyController.currencies.getResouceBalance(resourceID)
                    resourceModel.setValue(amount)

            resources.invalidate()

    def __onCollectingUpdateResource(self, resourceID):
        self.__updateResource(resourceID)

    def __onCollectingUpdateLock(self, enable):
        self.__lockForCustomAnimation = enable
        if enable is False:
            self.__updateResources()

    def __onResourceCollected(self, event):
        resource = event.ctx.get('resource')
        if resource is None:
            return
        else:
            with self.viewModel.transaction() as (model):
                resources = model.getResources()
                resourceModel = findFirst(lambda r: r.getType() == resource.value, resources)
                if resourceModel is not None:
                    amount = self._nyController.currencies.getResouceBalance(resource.value)
                    resourceModel.setValue(amount)
                    resources.invalidate()
            return

    @property
    def __isResourcesTabOpened(self):
        return self.__currentView == NyWidgetTopMenu.GLADE and NewYearNavigation.getCurrentObject() == NYObjects.RESOURCES

    def __onBalanceUpdated(self):
        self.__updateResources()