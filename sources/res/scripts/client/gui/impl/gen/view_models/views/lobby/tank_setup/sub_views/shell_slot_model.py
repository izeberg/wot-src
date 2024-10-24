from frameworks.wulf import Array
from gui.impl.gen.view_models.common.price_model import PriceModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_specification_model import ShellSpecificationModel

class ShellSlotModel(BaseSlotModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(ShellSlotModel, self).__init__(properties=properties, commands=commands)

    @property
    def totalPrice(self):
        return self._getViewModel(20)

    @staticmethod
    def getTotalPriceType():
        return PriceModel

    def getCount(self):
        return self._getNumber(21)

    def setCount(self, value):
        self._setNumber(21, value)

    def getBuyCount(self):
        return self._getNumber(22)

    def setBuyCount(self, value):
        self._setNumber(22, value)

    def getType(self):
        return self._getString(23)

    def setType(self, value):
        self._setString(23, value)

    def getSpecifications(self):
        return self._getArray(24)

    def setSpecifications(self, value):
        self._setArray(24, value)

    @staticmethod
    def getSpecificationsType():
        return ShellSpecificationModel

    def _initialize(self):
        super(ShellSlotModel, self)._initialize()
        self._addViewModelProperty('totalPrice', PriceModel())
        self._addNumberProperty('count', 0)
        self._addNumberProperty('buyCount', 0)
        self._addStringProperty('type', '')
        self._addArrayProperty('specifications', Array())