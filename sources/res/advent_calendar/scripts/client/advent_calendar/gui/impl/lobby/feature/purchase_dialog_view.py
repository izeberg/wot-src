from __future__ import absolute_import
import logging, typing
from collections import namedtuple
from advent_calendar.gui.impl.gen.view_models.views.lobby.purchase_dialog_model import PurchaseDialogModel
from advent_calendar.gui.impl.lobby.feature.currency_provider import CurrencyProvider, CurrencyInfo
from advent_calendar.gui.impl.lobby.feature.tooltips.advent_calendar_simple_tooltip_view import AdventCalendarSimpleTooltip
from advent_calendar.skeletons import IAdventCalendarController
from gui.impl.gen import R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView, TViewModel
from gui.impl.pub.dialog_window import DialogButtons
from gui.impl.pub.view_component import ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from helpers import dependency
from skeletons.gui.game_control import IWalletController
if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional
    from gui.impl.backport import TooltipData
_logger = logging.getLogger(__name__)
PurchaseData = namedtuple('PurchaseData', ('dayId', 'resourceStr'))

class BasePurchaseDialogView(FullScreenDialogBaseView, ViewComponent[TViewModel]):
    _wallet = dependency.descriptor(IWalletController)
    __adventController = dependency.descriptor(IAdventCalendarController)

    def __init__(self, dayId, price, currencyProvider, layoutID, model):
        super(BasePurchaseDialogView, self).__init__(layoutID=layoutID, model=model)
        self._dayId = dayId
        self._price = price
        self._currencyProvider = currencyProvider
        self._currency = None
        self._tooltips = {}
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(BasePurchaseDialogView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self._tooltips.get(tooltipId)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.advent_calendar.mono.lobby.tooltips.advent_calendar_simple_tooltip():
            payload = event.getArgument('payload', '')
            if not payload:
                _logger.error("Parameter 'payload' is omitted")
                return None
            return AdventCalendarSimpleTooltip(payload)
        else:
            return super(BasePurchaseDialogView, self).createToolTipContent(event, contentID)

    def _finalize(self):
        super(BasePurchaseDialogView, self)._finalize()
        self._currencyProvider = None
        self._tooltips.clear()
        return

    def _onLoading(self, *args, **kwargs):
        super(BasePurchaseDialogView, self)._onLoading(args, kwargs)
        self._setCurrency()
        self._fillModel()

    def _getEvents(self):
        return (
         (
          self._wallet.onWalletStatusChanged, self.__onWalletStatusChanged),
         (
          self._currencyProvider.onBalanceUpdated, self.__onBalanceUpdated),
         (
          self.__adventController.onConfigChanged, self.__onSettingsChanged))

    def _getAdditionalData(self):
        return PurchaseData(dayId=self._dayId, resourceStr=self._currency.code if self._currency else '')

    @replaceNoneKwargsModel
    def _updatePrice(self, model=None):
        raise NotImplementedError

    def _fillModel(self):
        raise NotImplementedError

    def _setCurrency(self):
        self._currency = self._currencyProvider.getMax()

    def _onClose(self):
        self._setResult(DialogButtons.CANCEL)

    def _onAccept(self):
        self._setResult(DialogButtons.PURCHASE)

    def __onWalletStatusChanged(self, *_):
        self.viewModel.setIsWalletAvailable(self._wallet.isAvailable)

    def __onBalanceUpdated(self):
        self._updatePrice()

    def __onSettingsChanged(self):
        if not self.__adventController.isAvailable():
            self.destroyWindow()
            return
        doorIdx = self._dayId - 1
        doorsConfig = self.__adventController.config.doors
        if 0 <= doorIdx < len(doorsConfig):
            self._price = doorsConfig[doorIdx].get('cost', 0)
        self._setCurrency()
        self._updatePrice()


class PurchaseDialogView(BasePurchaseDialogView[PurchaseDialogModel]):

    def __init__(self, dayId, price, currencyProvider=None):
        super(PurchaseDialogView, self).__init__(dayId, price, currencyProvider, layoutID=R.views.advent_calendar.mono.lobby.purchase_dialog_view(), model=PurchaseDialogModel)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _getEvents(self):
        return super(PurchaseDialogView, self)._getEvents() + (
         (
          self.viewModel.onAccept, self._onAccept),
         (
          self.viewModel.onCancel, self._onClose))

    def _fillModel(self):
        with self.viewModel.transaction() as (tx):
            tx.setDayId(self._dayId)
            tx.setIsWalletAvailable(self._wallet.isAvailable)
            self._updatePrice(model=tx)

    @replaceNoneKwargsModel
    def _updatePrice(self, model=None):
        if self._currency:
            balance = self._currencyProvider.getBalance(self._currency.code)
            model.setCurrentResource(self._currency.code)
            model.setCurrencyTooltipId(self._currency.tooltipId)
            model.setBalanceCurrencyValue(balance)
            model.setPrice(self._price)
            model.setNotEnoughResource(self._price > balance)