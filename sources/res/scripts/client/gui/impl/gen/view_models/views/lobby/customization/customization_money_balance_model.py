from gui.impl.gen.view_models.views.dialogs.sub_views.money_balance_view_model import MoneyBalanceViewModel

class CustomizationMoneyBalanceModel(MoneyBalanceViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(CustomizationMoneyBalanceModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CustomizationMoneyBalanceModel, self)._initialize()