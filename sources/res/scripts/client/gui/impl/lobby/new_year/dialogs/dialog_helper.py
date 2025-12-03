from frameworks.wulf.view.array import fillViewModelsArray
from gui.impl.gen.view_models.views.lobby.new_year.components.balance_model import BalanceModel
from helpers import dependency
from skeletons.gui.shared import IItemsCache

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def initBalance(balanceArray, currencies, itemsCache=None):
    money = itemsCache.items.stats.money
    currencyModelsList = []
    for currency in currencies:
        cur = BalanceModel()
        cur.setCurrency(currency)
        cur.setAmount(money.get(currency, 0))
        currencyModelsList.append(cur)

    fillViewModelsArray(currencyModelsList, balanceArray)