from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class VehicleSelectionModel(NotificationBaseModel):
    __slots__ = ('onClick', 'onClose')

    def __init__(self, properties=2, commands=2):
        super(VehicleSelectionModel, self).__init__(properties=properties, commands=commands)

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(VehicleSelectionModel, self)._initialize()
        self._addNumberProperty('count', 0)
        self.onClick = self._addCommand('onClick')
        self.onClose = self._addCommand('onClose')