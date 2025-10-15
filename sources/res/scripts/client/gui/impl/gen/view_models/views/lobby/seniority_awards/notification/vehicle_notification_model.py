from gui.impl.gen.view_models.views.lobby.notifications.notification_model import NotificationModel

class VehicleNotificationModel(NotificationModel):
    __slots__ = ('onSelectVehicles', )

    def __init__(self, properties=1, commands=1):
        super(VehicleNotificationModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(VehicleNotificationModel, self)._initialize()
        self.onSelectVehicles = self._addCommand('onSelectVehicles')