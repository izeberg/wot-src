from __future__ import absolute_import
import logging
from collections import namedtuple
import typing
from Event import Event, EventManager
from advent_calendar.skeletons.game_controller import IAdventCalendarController
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import List, Optional
_logger = logging.getLogger(__name__)
CurrencyInfo = namedtuple('CurrencyInfo', ('code', 'value', 'tooltipId'))
_CURRENCY_TOOLTIPS = {CURRENCIES_CONSTANTS.CREDITS: TOOLTIPS_CONSTANTS.CREDITS_INFO_SIMPLE, 
   CURRENCIES_CONSTANTS.CRYSTAL: TOOLTIPS_CONSTANTS.CRYSTAL_INFO_SIMPLE, 
   CURRENCIES_CONSTANTS.GOLD: TOOLTIPS_CONSTANTS.GOLD_INFO_SIMPLE}

class CurrencyProvider(object):
    _adventController = dependency.descriptor(IAdventCalendarController)

    def __init__(self):
        self._em = EventManager()
        self.onBalanceUpdated = Event(self._em)

    @property
    def icon(self):
        return ''

    @property
    def name(self):
        primary = self.getPrimary()
        if primary is not None:
            return primary.code
        else:
            return ''

    def init(self):
        pass

    def fini(self):
        self._em.clear()

    def getCodes(self):
        return list(self._adventController.config.currencies)

    def getCurrencies(self):
        return [ self.getCurrency(code) for code in self.getCodes() ]

    def getCurrency(self, code):
        return CurrencyInfo(code=code, value=self.getBalance(code), tooltipId=_CURRENCY_TOOLTIPS.get(code, ''))

    def getPrimary(self):
        codes = self.getCodes()
        if not codes:
            return None
        else:
            return self.getCurrency(codes[0])

    def getMax(self):
        codes = self.getCodes()
        if not codes:
            return None
        else:
            return self.getCurrency(max(codes, key=self.getBalance))

    def getMaxBalance(self):
        balances = [ self.getBalance(code) for code in self.getCodes() ]
        if balances:
            return max(balances)
        return 0

    def isEnough(self, price):
        return bool(self.getCodes()) and self.getMaxBalance() >= price

    def getBalance(self, code):
        raise NotImplementedError


class StandardCurrencyProvider(CurrencyProvider):
    __DYNAMIC_CURRENCIES_KEY = 'cache.dynamicCurrencies'
    _itemsCache = dependency.descriptor(IItemsCache)

    def init(self):
        super(StandardCurrencyProvider, self).init()
        callbacks = {('stats.{}').format(code):self.__onBalanceChanged for code in self.getCodes()}
        callbacks[self.__DYNAMIC_CURRENCIES_KEY] = self.__onBalanceChanged
        g_clientUpdateManager.addCallbacks(callbacks)

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(StandardCurrencyProvider, self).fini()

    def getBalance(self, code):
        return int(self._itemsCache.items.stats.getDynamicMoney().get(code, 0))

    def __onBalanceChanged(self, *_):
        self.onBalanceUpdated()