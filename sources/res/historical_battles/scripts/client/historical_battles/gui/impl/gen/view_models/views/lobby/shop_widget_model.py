from frameworks.wulf import ViewModel

class ShopWidgetModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=1, commands=1):
        super(ShopWidgetModel, self).__init__(properties=properties, commands=commands)

    def getFrontType(self):
        return self._getString(0)

    def setFrontType(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(ShopWidgetModel, self)._initialize()
        self._addStringProperty('frontType', '')
        self.onClick = self._addCommand('onClick')