from frameworks.wulf import ViewModel

class ShopCardViewModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=0, commands=1):
        super(ShopCardViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ShopCardViewModel, self)._initialize()
        self.onClick = self._addCommand('onClick')