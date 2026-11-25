from enum import Enum
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class State(Enum):
    DOORS_AVAILABLE = 'doorsAvailable'
    FIRST_ENTRY = 'firstEntry'
    POST_EVENT = 'postEvent'


class AvailableDoorsViewModel(NotificationBaseModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=7, commands=1):
        super(AvailableDoorsViewModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return State(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)

    def getBackgroundPlugin(self):
        return self._getString(2)

    def setBackgroundPlugin(self, value):
        self._setString(2, value)

    def getDescriptionPlugin(self):
        return self._getString(3)

    def setDescriptionPlugin(self, value):
        self._setString(3, value)

    def getEventEndDate(self):
        return self._getNumber(4)

    def setEventEndDate(self, value):
        self._setNumber(4, value)

    def getIsButtonDisabled(self):
        return self._getBool(5)

    def setIsButtonDisabled(self, value):
        self._setBool(5, value)

    def getRewardImagePath(self):
        return self._getString(6)

    def setRewardImagePath(self, value):
        self._setString(6, value)

    def _initialize(self):
        super(AvailableDoorsViewModel, self)._initialize()
        self._addStringProperty('state')
        self._addStringProperty('backgroundPlugin', '')
        self._addStringProperty('descriptionPlugin', '')
        self._addNumberProperty('eventEndDate', 0)
        self._addBoolProperty('isButtonDisabled', False)
        self._addStringProperty('rewardImagePath', '')
        self.onClick = self._addCommand('onClick')