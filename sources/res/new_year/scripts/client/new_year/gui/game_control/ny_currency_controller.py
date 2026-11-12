from functools import partial
from Event import Event
from debug_utils import LOG_ERROR
from gui.shared.money import Currency
from helpers import dependency
from helpers.events_handler import EventsHandler
from new_year.gui.impl.gen.view_models.common.ny_currency_type_model import NyCurrencyType
from new_year.gui.impl.new_year.navigation import NewYearNavigation
from new_year.gui.shared.ny_machine_helper import getMachineKeysCount, getMachineLootboxToken, isMachineEnabled
from new_year.messenger.sys_messages import showMachineNotification
from new_year.ny_constants import ViewAliases
from new_year.skeletons.new_year import INewYearController
from new_year.skeletons.new_year import INewYearCurrencyController
from new_year_common.items.components.ny_constants import TOKEN_MANDARIN, TOKEN_LOOTBOX_FRAGMENT
from skeletons.gui.shared import IItemsCache

class NewYearCurrencyController(INewYearCurrencyController, EventsHandler):
    __slots__ = ('__currencyCountProviders', '__currencies')
    __itemsCache = dependency.descriptor(IItemsCache)
    __newYearController = dependency.descriptor(INewYearController)
    __DEFAULT_CURRENCIES = (
     NyCurrencyType.MANDARIN,
     NyCurrencyType.NYGIFTMACHINETOKEN,
     NyCurrencyType.NYLOOTBOXFRAGMENT,
     NyCurrencyType.CREDITS)

    def __init__(self, *args, **kwargs):
        super(NewYearCurrencyController, self).__init__(*args, **kwargs)
        self.onCurrencyUpdated = Event()
        self.onVisibleCurrenciesChanged = Event()
        self.__currencies = self.__DEFAULT_CURRENCIES
        self.__currencyCountProviders = {NyCurrencyType.MANDARIN: partial(self.__tokenProvider, TOKEN_MANDARIN), 
           NyCurrencyType.NYGIFTMACHINETOKEN: getMachineKeysCount, 
           NyCurrencyType.NYLOOTBOXFRAGMENT: partial(self.__tokenProvider, TOKEN_LOOTBOX_FRAGMENT), 
           NyCurrencyType.GOLD: partial(self.__currencyProvider, Currency.GOLD), 
           NyCurrencyType.CREDITS: partial(self.__currencyProvider, Currency.CREDITS)}

    @property
    def getCurrencies(self):
        return self.__currencies

    @property
    def getGiftMachineTokenCount(self):
        return self.getCurrencyCount(NyCurrencyType.NYGIFTMACHINETOKEN)

    @property
    def getMandarinTokenCount(self):
        return self.getCurrencyCount(NyCurrencyType.MANDARIN)

    @property
    def getGoldCount(self):
        return self.getCurrencyCount(NyCurrencyType.GOLD)

    def getCurrencyClickHandler(self, currency):
        instantly = NewYearNavigation.getCurrentViewName() in (
         ViewAliases.PET_VIEW, ViewAliases.INFO_VIEW, ViewAliases.LEADERS_VIEW)
        machineEnabled = isMachineEnabled()
        if currency == NyCurrencyType.MANDARIN:
            if self.__newYearController.isMaxAtmosphereLevel() and machineEnabled:
                return self.switchToMachine(instantly)
            return self.switchToCity(instantly)
        else:
            if currency == NyCurrencyType.NYGIFTMACHINETOKEN and machineEnabled:
                return self.switchToMachine(instantly)
            return

    @staticmethod
    def switchToMachine(instantly):
        return partial(NewYearNavigation.switchToView, ViewAliases.SURPRISE_MACHINE_VIEW, instantly=instantly)

    @staticmethod
    def switchToCity(instantly):
        return partial(NewYearNavigation.switchToView, ViewAliases.CITY_VIEW, instantly=instantly)

    def getCurrencyCount(self, currency):
        provider = self.__currencyCountProviders.get(currency)
        if provider is None:
            LOG_ERROR(('Unknown currency {}').format(currency))
            return 0
        else:
            return provider()

    def setVisibleCurrencies(self, currencies=None):
        if currencies is None:
            newVal = self.__DEFAULT_CURRENCIES
        elif isinstance(currencies, (list, tuple)):
            newVal = tuple(currencies)
        else:
            newVal = (
             currencies,)
        if newVal != self.__currencies:
            self.__currencies = newVal
            self.onVisibleCurrenciesChanged()
        return

    def init(self):
        self._subscribe()

    def fini(self):
        self._unsubscribe()
        self.onCurrencyUpdated.clear()
        self.onVisibleCurrenciesChanged.clear()

    def onDisconnected(self):
        self.setVisibleCurrencies()

    def _getCallbacks(self):
        return (
         (
          ('stats.{}').format(Currency.GOLD), self.__onGoldUpdated),
         (
          ('stats.{}').format(Currency.CREDITS), self.__onCreditsUpdated),
         (
          'tokens', self.__onTokensUpdated))

    def __tokenProvider(self, token):
        return self.__itemsCache.items.tokens.getTokenCount(tokenID=token)

    def __currencyProvider(self, currency):
        return getattr(self.__itemsCache.items.stats, currency)

    def __onGoldUpdated(self, diff):
        self.onCurrencyUpdated(NyCurrencyType.GOLD, diff)

    def __onCreditsUpdated(self, diff):
        self.onCurrencyUpdated(NyCurrencyType.CREDITS, diff)

    def __onTokensUpdated(self, diff):
        machineToken = getMachineLootboxToken()
        if machineToken in diff:
            machineTokenData = diff[machineToken]
            machineTokenCount = machineTokenData[1] if machineTokenData is not None else 0
            self.onCurrencyUpdated(NyCurrencyType.NYGIFTMACHINETOKEN, machineTokenCount)
            if machineTokenCount > 0:
                showMachineNotification()
        if TOKEN_MANDARIN in diff:
            mandarinTokenData = diff[TOKEN_MANDARIN]
            mandarinTokenCount = mandarinTokenData[1] if mandarinTokenData is not None else 0
            self.onCurrencyUpdated(NyCurrencyType.MANDARIN, mandarinTokenCount)
        if TOKEN_LOOTBOX_FRAGMENT in diff:
            fragmentTokenData = diff[TOKEN_LOOTBOX_FRAGMENT]
            fragmentTokenCount = fragmentTokenData[1] if fragmentTokenData is not None else 0
            self.onCurrencyUpdated(NyCurrencyType.NYLOOTBOXFRAGMENT, fragmentTokenCount)
        return