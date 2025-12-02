from frameworks.wulf import ViewSettings, WindowLayer
from goodies.goodie_constants import GOODIE_TARGET_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.game_control.wallet import WalletController
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_purchase_model import PurchaseState
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.pet_purchase_overlay_model import PetPurchaseOverlayModel
from gui.impl.lobby.new_year.challenge.helper import fillMasteryProgression
from gui.impl.lobby.new_year.dialogs.dialog_helper import initBalance
from gui.impl.lobby.new_year.tooltips.ho_challenge_token_tooltip import NyChallengeTokenTooltip
from gui.impl.lobby.new_year.states import GladeFirState
from gui.impl.lobby.pet_system.states import PetStorageState
from gui.impl.pub import ViewImpl
from gui.impl.pub.dialog_window import DialogFlags
from gui.impl.pub.lobby_window import LobbyWindow
from gui.pet_system.pet_item_helper import PetItem
from gui.pet_system.processor import PetPurchaseProcessor
from gui.pet_system.requester import INVALID_PET_ID
from gui.shared.money import Currency, Money, ZERO_MONEY
from gui.shared.utils import decorators
from gui.shared.view_helpers.blur_manager import CachedBlur
from gui.shop import showBuyGoldForPet
from helpers import dependency, server_settings
from items.components.ny_constants import CelebrityQuestTokenParts, NY_PET_TOKEN
from pet_system_common.pet_constants import PETS_SYSTEM_CONFIG
from skeletons.gui.game_control import IWalletController
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.pet_system import IPetSystemController
from skeletons.gui.shared import IItemsCache
from skeletons.new_year import INewYearController

class PetPurchaseOverlay(ViewImpl):
    __itemsCache = dependency.descriptor(IItemsCache)
    __wallet = dependency.descriptor(IWalletController)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __goodiesCache = dependency.descriptor(IGoodiesCache)
    __nyController = dependency.descriptor(INewYearController)
    __petController = dependency.descriptor(IPetSystemController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.holiday_ops.pet_purchase_overlay())
        settings.args = args
        settings.kwargs = kwargs
        settings.model = PetPurchaseOverlayModel()
        super(PetPurchaseOverlay, self).__init__(settings)
        self.__isRequestToBuyProcessing = False

    def _onLoading(self, *args, **kwargs):
        super(PetPurchaseOverlay, self)._onLoading(*args, **kwargs)
        g_clientUpdateManager.addMoneyCallback(self.__onMoneyChangeHandler)
        self.__update()

    def _finalize(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(PetPurchaseOverlay, self)._finalize()

    @property
    def viewModel(self):
        return super(PetPurchaseOverlay, self).getViewModel()

    def canBeClosed(self):
        return not self.__isRequestToBuyProcessing

    def __update(self):
        self.viewModel.setIsPetSystemEnabled(self.__petController.isEnabled)
        self.viewModel.setIsPetAvailable(self.__nyController.isDogTokenReceived())
        self.__updatePrice()
        fillMasteryProgression(self.viewModel.masteryProgression)

    def __updatePrice(self):
        price = self.__getPetPrice()
        currency = price.getCurrency()
        fullPriceValue = price.get(currency, 0)
        totalPrice = self.__itemsCache.items.shop.getPetCostWithDiscount(price)
        totalPriceValue = totalPrice.get(currency, 0)
        money = self.__itemsCache.items.stats.money
        isEnough = money.get(currency, 0) >= totalPriceValue
        discount = 0.0 if fullPriceValue == 0 else (fullPriceValue - totalPriceValue) / float(fullPriceValue) * 100
        currencyStatus = self.__wallet.componentsStatuses.get(currency)
        if self.__wallet.isNotAvailable:
            status = PurchaseState.UNAVAILABLE
        elif currencyStatus != WalletController.STATUS.AVAILABLE:
            status = PurchaseState.UNAVAILABLE
        else:
            status = PurchaseState.AVAILABLE
        with self.viewModel.transaction() as (model):
            model.setPurchaseState(status)
            model.setCurrency(currency)
            model.setPrice(int(fullPriceValue))
            model.setPriceWithDiscount(int(totalPriceValue))
            model.setDiscountPercent(int(discount))
            model.setIsEnough(isEnough)
            initBalance(model.getBalance(), [Currency.GOLD])

    def __getPetPrice(self):
        price = PetItem.getPetsConfig().getPetPrice(self.__getPromoPetID())
        if price:
            return Money(**price)
        return ZERO_MONEY

    def __getPromoPetID(self):
        petsPromo = self.__petController.getPetsPromoConfig()
        if petsPromo.isEnabled():
            return next(iter(petsPromo.getPets()))
        return INVALID_PET_ID

    def _getEvents(self):
        events = super(PetPurchaseOverlay, self)._getEvents()
        return events + (
         (
          self.viewModel.onBuy, self.__onBuy),
         (
          self.viewModel.onBuyGold, self.__onBuyGold),
         (
          self.viewModel.onGoToVillage, self.__onGoToVillage),
         (
          self.viewModel.onGoToPetDen, self.__onGoToPetDen),
         (
          self.__wallet.onWalletStatusChanged, self.__onWalletStatusChanged),
         (
          self.__lobbyContext.getServerSettings().onServerSettingsChange, self.__onServerSettingsChanged))

    def _getCallbacks(self):
        return (
         (
          'tokens', self.__onTokensChanged),
         (
          'goodies', self._onGoodiesUpdate))

    def createToolTipContent(self, event, contentID):
        if event.contentID == R.views.mono.holiday_ops.tooltips.ho_challenge_token_tooltip():
            tokenType = str(event.getArgument('tokenType'))
            return NyChallengeTokenTooltip(tokenType)
        return super(PetPurchaseOverlay, self).createToolTipContent(event, contentID)

    def __onMoneyChangeHandler(self, *_):
        self.__updatePrice()

    @decorators.adisp_process('newYear/buyPet')
    def __onBuy(self):
        self.__isRequestToBuyProcessing = True
        petID = self.__getPromoPetID()
        yield PetPurchaseProcessor(petID).request()
        self.__isRequestToBuyProcessing = False

    def __onBuyGold(self):
        price = self.__getPetPrice()
        currency = price.getCurrency()
        value = price.get(currency, 0)
        if value and currency and currency == Currency.GOLD:
            showBuyGoldForPet(price)

    def __onGoToVillage(self):
        GladeFirState.goTo(instantly=True)
        self.destroyWindow()

    def __onGoToPetDen(self):
        PetStorageState.goTo()
        self.destroyWindow()

    def __onWalletStatusChanged(self, *_):
        self.__updatePrice()

    @server_settings.serverSettingsChangeListener(PETS_SYSTEM_CONFIG)
    def __onServerSettingsChanged(self, _):
        self.__update()

    def __onTokensChanged(self, tokens):
        if CelebrityQuestTokenParts.FULL_SEAL_TOKEN in tokens:
            self.__update()
        elif NY_PET_TOKEN in tokens:
            self.destroyWindow()

    def _onGoodiesUpdate(self, goodies):
        for goodyId in goodies.keys():
            goody = self.__goodiesCache.getGoodieByID(goodyId)
            if goody.target.targetType == GOODIE_TARGET_TYPE.ON_BUY_PET:
                self.__updatePrice()
                break


class PetPurchaseOverlayWindow(LobbyWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super(PetPurchaseOverlayWindow, self).__init__(DialogFlags.TOP_FULLSCREEN_WINDOW, content=PetPurchaseOverlay(*args, **kwargs), layer=WindowLayer.FULLSCREEN_WINDOW, parent=parent)
        self._blur = None
        return

    def _initialize(self):
        super(PetPurchaseOverlayWindow, self)._initialize()
        self._blur = CachedBlur(enabled=True, ownLayer=self.layer - 1)

    def _finalize(self):
        if self._blur:
            self._blur.fini()
            self._blur = None
        super(PetPurchaseOverlayWindow, self)._finalize()
        return