from frameworks.wulf import ViewModel

class JmLoreOverlayViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=1, commands=1):
        super(JmLoreOverlayViewModel, self).__init__(properties=properties, commands=commands)

    def getNodeId(self):
        return self._getString(0)

    def setNodeId(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(JmLoreOverlayViewModel, self)._initialize()
        self._addStringProperty('nodeId', '')
        self.onClose = self._addCommand('onClose')