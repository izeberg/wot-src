from frameworks.wulf import ViewModel

class NotificationBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NotificationBaseModel, self).__init__(properties=properties, commands=commands)

    def getIsPopUp(self):
        return self._getBool(0)

    def setIsPopUp(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(NotificationBaseModel, self)._initialize()
        self._addBoolProperty('isPopUp', False)