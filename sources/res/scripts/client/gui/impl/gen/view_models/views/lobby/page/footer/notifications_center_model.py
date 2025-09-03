from frameworks.wulf import ViewModel

class NotificationsCenterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NotificationsCenterModel, self).__init__(properties=properties, commands=commands)

    def getNewNotificationsCount(self):
        return self._getNumber(0)

    def setNewNotificationsCount(self, value):
        self._setNumber(0, value)

    def getHasImportantNotification(self):
        return self._getBool(1)

    def setHasImportantNotification(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(NotificationsCenterModel, self)._initialize()
        self._addNumberProperty('newNotificationsCount', 0)
        self._addBoolProperty('hasImportantNotification', False)