from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class AvailableTokensModel(NotificationBaseModel):
    __slots__ = ('onClick', 'onClose')

    def __init__(self, properties=3, commands=2):
        super(AvailableTokensModel, self).__init__(properties=properties, commands=commands)

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(AvailableTokensModel, self)._initialize()
        self._addNumberProperty('timeLeft', 0)
        self._addNumberProperty('count', 0)
        self.onClick = self._addCommand('onClick')
        self.onClose = self._addCommand('onClose')