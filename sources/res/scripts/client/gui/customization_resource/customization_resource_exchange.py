from collections import namedtuple
from functools import partial
import AccountCommands, BigWorld
from gui.shared.gui_items.processors import Processor
ExchangeResponse = namedtuple('ExchangeResponse', ('success', 'items', 'reward', 'error'))

class CustomizationResourceExchangeProcessor(Processor):
    __slots__ = ('__payload', )

    def __init__(self, payload):
        super(CustomizationResourceExchangeProcessor, self).__init__()
        self.__payload = tuple((itemCD, count) for itemCD, _, count in payload)

    def _request(self, callback):
        BigWorld.player().shop.exchangeCustomizationResourceItems(self.__payload, partial(self.__onResponse, callback))

    def _successHandler(self, code, ctx=None):
        if not isinstance(ctx, dict):
            return self._errorHandler(AccountCommands.RES_FAILURE, 'INVALID_SERVER_RESPONSE')
        try:
            items = tuple(tuple(int(value) for value in item) for item in ctx['items'])
            reward = ctx['reward']
        except (KeyError, TypeError, ValueError):
            return self._errorHandler(AccountCommands.RES_FAILURE, 'INVALID_SERVER_RESPONSE')

        if not items or not reward or any(len(item) != 3 or item[2] <= 0 for item in items):
            return self._errorHandler(AccountCommands.RES_FAILURE, 'INVALID_SERVER_RESPONSE')
        response = ExchangeResponse(True, items, reward, '')
        return super(CustomizationResourceExchangeProcessor, self)._successHandler(code, ctx=response)

    def _errorHandler(self, code, errStr='', ctx=None):
        response = ExchangeResponse(False, (), {}, errStr)
        return super(CustomizationResourceExchangeProcessor, self)._errorHandler(code, errStr=errStr, ctx=response)

    def __onResponse(self, callback, resultID, errorStr='', data=None):
        self._response(resultID, callback, errStr=errorStr, ctx=data)