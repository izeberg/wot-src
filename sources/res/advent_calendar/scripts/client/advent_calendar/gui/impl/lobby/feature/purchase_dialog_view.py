from __future__ import absolute_import
import logging
from collections import namedtuple
from advent_calendar.gui.impl.gen.view_models.views.lobby.purchase_dialog_model import PurchaseDialogModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import getMaxResource
from advent_calendar.gui.impl.lobby.feature.ny_components.ny_resources_balance_view import NYResourceBalance
from advent_calendar.gui.impl.lobby.feature.tooltips.advent_calendar_simple_tooltip_view import AdventCalendarSimpleTooltip
from gui.game_control.wallet import WalletController
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.ny_constants import Resource
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView
from gui.impl.lobby.new_year.tooltips.ny_resource_tooltip import NyResourceTooltip
from gui.impl.new_year.new_year_helper import backportTooltipDecorator
from gui.impl.pub.dialog_window import DialogButtons
from gui.impl.pub.view_component import ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared.event_dispatcher import showLootBoxEntry
from helpers import dependency
from items.components.ny_constants import NyCurrency
from shared_utils import first
from skeletons.gui.game_control import IWalletController
from skeletons.new_year import INewYearController
_logger = logging.getLogger(__name__)
PurchaseData = namedtuple('PurchaseData', ('dayId', 'resourceStr'))

class PurchaseDialogView(ViewComponent[PurchaseDialogModel], FullScreenDialogBaseView):
    __nyController = dependency.descriptor(INewYearController)
    _wallet = dependency.descriptor(IWalletController)

    def __init__(self, dayId, price):
        self.__dayId = dayId
        self.__price = price
        self.__currentResource = NyCurrency.CRYSTAL
        super(PurchaseDialogView, self).__init__(layoutID=R.views.advent_calendar.mono.lobby.purchase_dialog_view(), model=PurchaseDialogModel)

    @property
    def viewModel(self):
        return super(PurchaseDialogView, self).getViewModel()

    @backportTooltipDecorator()
    def createToolTip(self, event):
        return super(PurchaseDialogView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        tooltips = R.views.mono.holiday_ops.tooltips
        if contentID == tooltips.ho_resource_tooltip():
            resourceType = event.getArgument('type')
            return NyResourceTooltip(resourceType)
        if contentID == R.views.advent_calendar.mono.lobby.tooltips.advent_calendar_simple_tooltip():
            payload = event.getArgument('payload', '')
            if not payload:
                _logger.error("Parameter 'payload' is omitted")
                return
            return AdventCalendarSimpleTooltip(payload)
        return super(PurchaseDialogView, self).createToolTipContent(event, contentID)

    def _getChildComponents(self):
        return {R.aliases.holiday_ops.default.BalancePanel(): lambda : NYResourceBalance(self.__onClose)}

    def _getEvents(self):
        return (
         (
          self.viewModel.onAccept, self.__onAccept),
         (
          self.viewModel.onCancel, self.__onClose),
         (
          self.viewModel.onSwitchToBoxes, self.__onOpenBoxes),
         (
          self._wallet.onWalletStatusChanged, self.__onWalletStatusChanged),
         (
          self.__nyController.currencies.onBalanceUpdated, self.__onBalanceUpdated),
         (
          self.viewModel.resources.onSwitchResource, self.__onSwitchResource))

    def _onLoading(self, *args, **kwargs):
        super(PurchaseDialogView, self)._onLoading(args, kwargs)
        self.__currentResource = getMaxResource().resourceName
        with self.viewModel.transaction() as (tx):
            tx.setDayId(self.__dayId)
            currencyStatus = self._wallet.dynamicComponentsStatuses.get(self.viewModel.resources.getCurrentResource())
            tx.setIsWalletAvailable(currencyStatus == WalletController.STATUS.AVAILABLE)
            resources = tx.resources.getResources()
            resources.clear()
            for currency in NyCurrency.ALL:
                resources.addString(currency)

            resources.invalidate()
            self.__updatePrice(model=tx)

    @replaceNoneKwargsModel
    def __updatePrice(self, model=None):
        currency = self.__currentResource.value
        balance = self.__nyController.currencies.getResouceBalance(currency)
        model.resources.setCurrentResource(currency)
        model.resources.setPrice(self.__price)
        model.resources.setNotEnoughResource(self.__price > balance)

    def _getAdditionalData(self):
        return PurchaseData(dayId=self.__dayId, resourceStr=self.viewModel.resources.getCurrentResource().encode('utf-8'))

    def __onClose(self):
        self._setResult(DialogButtons.CANCEL)

    def __onAccept(self):
        self._setResult(DialogButtons.PURCHASE)

    def __onOpenBoxes(self):
        self._setResult(DialogButtons.CANCEL)
        self.destroyWindow()
        showLootBoxEntry()

    def __onSwitchResource(self, args):
        resourceValue = args.get('resource', '')
        if not resourceValue:
            _logger.error('Argument - "resource" is omitted for command - "onSwitchResource"')
            return
        resource = first((item for item in Resource if item.value == resourceValue), Resource.CRYSTAL)
        _logger.info('Switching to resource with name=%s, required resource=%s', resource, resourceValue)
        self.__currentResource = resource
        self.__updatePrice()

    def __onBalanceUpdated(self):
        self.__updatePrice()

    def __onWalletStatusChanged(self, *_):
        with self.viewModel.transaction() as (model):
            currencyStatus = self._wallet.dynamicComponentsStatuses.get(self.viewModel.resources.getCurrentResource())
            model.setIsWalletAvailable(currencyStatus == WalletController.STATUS.AVAILABLE)