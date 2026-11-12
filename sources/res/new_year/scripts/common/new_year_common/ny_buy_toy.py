from new_year_common.settings import NyBuyToyConsts

class BuyToyConfig(object):
    __slots__ = ('_config', )

    def __init__(self, config):
        self._config = config

    def getToyCountForOnePurchase(self):
        return self._config.get(NyBuyToyConsts.TOY_COUNT_FOR_ONE_PURCHASE)