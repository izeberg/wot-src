from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType
from frameworks.wulf import ViewModel

class ProxyCurrencyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ProxyCurrencyTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getCoinType(self):
        return CoinType(self._getString(0))

    def setCoinType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(ProxyCurrencyTooltipViewModel, self)._initialize()
        self._addStringProperty('coinType')