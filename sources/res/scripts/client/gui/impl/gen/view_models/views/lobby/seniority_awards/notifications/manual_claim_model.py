from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class ManualClaimModel(NotificationBaseModel):
    __slots__ = ('onClick', 'onClose')

    def __init__(self, properties=1, commands=2):
        super(ManualClaimModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ManualClaimModel, self)._initialize()
        self.onClick = self._addCommand('onClick')
        self.onClose = self._addCommand('onClose')