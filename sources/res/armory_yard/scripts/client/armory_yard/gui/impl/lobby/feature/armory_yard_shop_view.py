import logging
from account_helpers.AccountSettings import ArmoryYard, AccountSettings
from armory_yard.gui.impl.lobby.feature.armory_yard_shop_base import ArmoryYardShopBaseView
from armory_yard.gui.impl.lobby.feature.tooltips.armory_yard_currency_tooltip_view import ArmoryYardCurrencyTooltipView
from armory_yard.gui.impl.lobby.feature.tooltips.armory_yard_simple_tooltip_view import ArmoryYardSimpleTooltipView
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_shop_view_model import ArmoryYardShopViewModel, BackButtonState
from armory_yard.gui.window_events import showArmoryYardShopBuyWindow
from armory_yard.gui.shared.shop_bonus_packers import packShopItem
from armory_yard_helpers import evaluatePrerequisiteToken
from frameworks.wulf import WindowFlags, WindowLayer, ViewSettings, ViewFlags
from gui.impl.gen import R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub.lobby_window import LobbyWindow
from gui.impl.wrappers.user_compound_price_model import PriceModelBuilder
from gui.shared.money import Money
from helpers import dependency
from skeletons.gui.game_control import IArmoryYardShopController, IArmoryYardController
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class ArmoryYardShopView(ArmoryYardShopBaseView):
    __slots__ = ('__isArmoryVisiting', '__onCloseCallback')
    __ayShopCtrl = dependency.descriptor(IArmoryYardShopController)
    __ayCtrl = dependency.descriptor(IArmoryYardController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, layoutID, onLoadedCallback=None, onCloseCallback=None):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_TOP_SUB_VIEW
        settings.model = ArmoryYardShopViewModel()
        super(ArmoryYardShopView, self).__init__(settings, onLoadedCallback)
        self.__isArmoryVisiting = self.__ayCtrl.isArmoryVisiting
        self.__onCloseCallback = onCloseCallback

    @property
    def viewModel(self):
        return super(ArmoryYardShopView, self).getViewModel()

    def __onBuyProduct(self, args):
        productId = int(args.get('productId', -1))
        if productId and productId in self.__ayShopCtrl.products:
            showArmoryYardShopBuyWindow(productId, parent=self.getParentWindow(), onClosedCallback=self.destroyWindow)

    def __onCurrencyUpdate(self):
        with self.viewModel.transaction() as (vm):
            vm.setCurrency(self.__ayShopCtrl.ayCoins)

    def __update(self):
        if not self.__ayShopCtrl.isEnabled:
            self.destroyWindow()
            return
        else:
            self.__onCurrencyUpdate()
            isIntroViewed = not AccountSettings.getArmoryYard(ArmoryYard.ARMORY_SHOP_INTRO_VIEWED)
            if isIntroViewed:
                AccountSettings.setArmoryYard(ArmoryYard.ARMORY_SHOP_INTRO_VIEWED, True)
            with self.viewModel.transaction() as (vm):
                vm.setIsIntroVisible(isIntroViewed)
                vm.setBackButtonState(BackButtonState.ARMORY if self.__ayCtrl.isArmoryVisiting else BackButtonState.INGAMESHOP)
                PriceModelBuilder.fillPriceModel(vm.tokenPrice, Money.makeMoney(self.__ayShopCtrl.conversionPrices))
                items = vm.getItems()
                items.clear()
                amountValues = []
                for productId, product in self.__ayShopCtrl.products.iteritems():
                    prerequisiteToken = product.get('prerequisiteToken')
                    if prerequisiteToken:
                        tokenID = prerequisiteToken.get('id')
                        tokensAmount = self.__itemsCache.items.tokens.getTokenCount(tokenID)
                        isBlocked, diff = evaluatePrerequisiteToken(prerequisiteToken, tokensAmount)
                        amountValues.append(diff)
                        if isBlocked:
                            continue
                    item = packShopItem(productId, product)
                    if item is None:
                        _logger.error('ArmoryYardShop product %s failed pack', productId)
                    elif item.getAvailable():
                        items.addViewModel(item)

                items.invalidate()
                vm.setSpecialOffersLimit(min(amountValues) if amountValues else 0)
            return

    def onBack(self):
        if self.__onCloseCallback:
            self.__onCloseCallback()
        self.destroyWindow()

    def _getEvents(self):
        return (
         (
          self.viewModel.onBack, self.onBack),
         (
          self.viewModel.onClose, self.onBack),
         (
          self.viewModel.onBuyProduct, self.__onBuyProduct),
         (
          self.viewModel.onCloseIntro, lambda : self.viewModel.setIsIntroVisible(False)),
         (
          self.viewModel.onShowIntro, lambda : self.viewModel.setIsIntroVisible(True)),
         (
          self.__ayShopCtrl.onProductsUpdate, self.__update),
         (
          self.__ayShopCtrl.onAYCoinsUpdate, self.__onCurrencyUpdate),
         (
          self.__ayShopCtrl.onSettingsUpdate, self.__update),
         (
          self.__ayCtrl.onUpdated, self.__checkExit))

    def __checkExit(self):
        if not self.__ayCtrl.isActive() and self.__isArmoryVisiting:
            self.destroyWindow()

    def _onLoading(self, *args, **kwargs):
        super(ArmoryYardShopView, self)._onLoading(*args, **kwargs)
        self.__update()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(ArmoryYardShopView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.armory_yard.lobby.feature.tooltips.ArmoryYardSimpleTooltipView():
            return ArmoryYardSimpleTooltipView(event.getArgument('state'), event.getArgument('id'))
        if contentID == R.views.armory_yard.lobby.feature.tooltips.ArmoryYardCurrencyTooltipView():
            return ArmoryYardCurrencyTooltipView(event.getArgument('currency'))
        return super(ArmoryYardShopView, self).createToolTipContent(event, contentID)


class ArmoryYardShopWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self, parent=None, onLoadedCallback=None, onCloseCallback=None):
        super(ArmoryYardShopWindow, self).__init__(wndFlags=WindowFlags.WINDOW, layer=WindowLayer.TOP_SUB_VIEW, content=ArmoryYardShopView(R.views.armory_yard.lobby.feature.ArmoryYardShopView(), onLoadedCallback=onLoadedCallback, onCloseCallback=onCloseCallback), parent=parent)