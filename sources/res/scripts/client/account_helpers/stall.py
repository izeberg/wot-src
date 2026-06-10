from typing import TYPE_CHECKING
import AccountCommands
if TYPE_CHECKING:
    from typing import Callable

class Stall(object):

    def __init__(self):
        self.__account = None
        return

    def setAccount(self, account):
        self.__account = account

    def purchaseProduct(self, productCode, count=1, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(requestID, resultID, errorStr, ext)
        else:
            proxy = None
        self.__account._doCmdIntStr(AccountCommands.CMD_PURCHASE_STALL_PRODUCT, count, productCode, proxy)
        return