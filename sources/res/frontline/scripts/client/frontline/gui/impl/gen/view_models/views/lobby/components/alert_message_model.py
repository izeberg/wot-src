from frameworks.wulf import ViewModel

class AlertMessageModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=2, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)

    def getMessage(self):
        return self._getString(0)

    def setMessage(self, value):
        self._setString(0, value)

    def getButtonLabel(self):
        return self._getString(1)

    def setButtonLabel(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty('message', '')
        self._addStringProperty('buttonLabel', '')
        self.onClick = self._addCommand('onClick')