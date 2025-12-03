from __future__ import absolute_import
from functools import partial
from frameworks.wulf import WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_resource_model import NyResourceModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_resources_balance_model import NyResourcesBalanceModel, CollectState
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_resource_collector_tooltip_model import CollectorTooltipType
from gui.impl.lobby.new_year.dialogs.dialogs import showResourcesConvertDialog
from gui.impl.lobby.new_year.popovers.ny_resources_convert_popover import NyResourcesConvertPopover
from gui.impl.lobby.new_year.states import GladeResourcesState
from gui.impl.lobby.new_year.tooltips.ny_resource_collector_tooltip import NyResourceCollectorTooltip
from gui.impl.lobby.new_year.tooltips.ny_resource_tooltip import NyResourceTooltip
from gui.impl.pub.view_component import ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared.utils import decorators
from gui.shared.utils.scheduled_notifications import SimpleNotifier
from helpers import dependency, time_utils
from new_year.ny_constants import RESOURCES_ORDER
from new_year.ny_helper import getNYGeneralConfig
from new_year.ny_processor import NewYearConvertResourcesProcessor
from new_year.ny_resource_collecting_helper import isCollectingAvailable, isExtraCollectingAvailable, getCollectingCooldownTime
from skeletons.gui.game_control import IWalletController
from skeletons.new_year import INewYearController

class AdventCalendarNyResourcesConvertPopover(NyResourcesConvertPopover):

    def __init__(self, closeClb=None, parentView=None):
        super(AdventCalendarNyResourcesConvertPopover, self).__init__()
        self.__closeClb = closeClb
        self.__parentView = parentView

    def _onGoToQuests(self):
        super(AdventCalendarNyResourcesConvertPopover, self)._onGoToQuests()
        if self.__closeClb is not None:
            self.__closeClb()
        return

    def _onGoToRewardKits(self):
        super(AdventCalendarNyResourcesConvertPopover, self)._onGoToRewardKits()
        if self.__closeClb is not None:
            self.__closeClb()
        return

    @decorators.adisp_process('newYear/resourcesConverter')
    def _convert(self, fromResourceType, fromValue, toResourceType, toValue, callback):
        result = yield NewYearConvertResourcesProcessor(fromResourceType, fromValue, toResourceType, toValue, self.__getConfirmator).request()
        callback(result=result)

    @property
    def __getConfirmator(self):
        return partial(showResourcesConvertDialog, parent=self.__parentView, layer=WindowLayer.TOP_WINDOW)


class NYResourceBalance(ViewComponent[NyResourcesBalanceModel]):
    __nyController = dependency.descriptor(INewYearController)
    __wallet = dependency.descriptor(IWalletController)

    def __init__(self, closeClb, isConvertPopoverAvailable=None):
        super(NYResourceBalance, self).__init__(model=NyResourcesBalanceModel)
        self.__closeClb = closeClb
        self.__isConvertPopoverAvailable = isConvertPopoverAvailable or (lambda : True)
        self.__notifier = SimpleNotifier(getCollectingCooldownTime, self.__updateCollecting)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(NYResourceBalance, self)._onLoading(*args, **kwargs)
        self.__updateResources()
        self.__notifier.startNotification()

    def _finalize(self):
        self.__notifier.stopNotification()
        self.__notifier.clear()
        super(NYResourceBalance, self)._finalize()

    def _getEvents(self):
        return (
         (
          self.viewModel.onCollectResources, self.__onCollectResources),
         (
          self.viewModel.onGoToResources, self.__onGoToResources),
         (
          self.__wallet.onWalletStatusChanged, self.__onWalletChanged),
         (
          self.__nyController.currencies.onBalanceUpdated, self.__onBalanceUpdated),
         (
          self.__nyController.resourceCollecting.onSwitchCollectingState, self.__onSwitchCollectingState))

    def __onCollectResources(self):
        self.__closeClb()
        GladeResourcesState.goTo(instantly=True)

    def __onGoToResources(self):
        self.__onCollectResources()

    def createToolTipContent(self, event, contentID):
        tooltips = R.views.mono.holiday_ops.tooltips
        if contentID == tooltips.ho_resource_tooltip():
            resourceType = event.getArgument('type')
            return NyResourceTooltip(resourceType)
        if contentID == tooltips.ho_resource_collector_tooltip():
            collectorTooltipType = CollectorTooltipType(event.getArgument('type'))
            return NyResourceCollectorTooltip(collectorTooltipType)
        return super(NYResourceBalance, self).createToolTipContent(event, contentID)

    def createPopOverContent(self, event):
        if event.contentID == R.views.mono.holiday_ops.popovers.ho_resources_convert_popover() and self.__isConvertPopoverAvailable():
            return AdventCalendarNyResourcesConvertPopover(self.__closeClb, self.getParentWindow())
        return super(NYResourceBalance, self).createPopOverContent(event)

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

    def __updateResources(self):
        with self.viewModel.transaction() as (model):
            self.__updateCollecting(model=model)
            model.setIsWalletAvailable(self.__wallet.isAvailable)
            resources = model.getResources()
            resources.clear()
            for resource in RESOURCES_ORDER:
                amount = self.__nyController.currencies.getResouceBalance(resource.value)
                resourceModel = NyResourceModel()
                resourceModel.setType(resource.value)
                resourceModel.setValue(amount)
                resources.addViewModel(resourceModel)

            resources.invalidate()

    def __onBalanceUpdated(self):
        self.__updateResources()

    def __onSwitchCollectingState(self, _):
        self.__updateResources()
        self.__notifier.startNotification()

    def __onWalletChanged(self, _):
        self.viewModel.setIsWalletAvailable(self.__wallet.isAvailable)