from frameworks.wulf import ViewModel

class EnvSwitcherBtnTipModel(ViewModel):
    __slots__ = ('onClosed', )

    def __init__(self, properties=1, commands=1):
        super(EnvSwitcherBtnTipModel, self).__init__(properties=properties, commands=commands)

    def getShowTip(self):
        return self._getBool(0)

    def setShowTip(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(EnvSwitcherBtnTipModel, self)._initialize()
        self._addBoolProperty('showTip', False)
        self.onClosed = self._addCommand('onClosed')