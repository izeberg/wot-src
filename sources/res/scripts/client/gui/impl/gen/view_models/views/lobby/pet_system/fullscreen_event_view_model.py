from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class FullscreenEventViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=2, commands=1):
        super(FullscreenEventViewModel, self).__init__(properties=properties, commands=commands)

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def getEventId(self):
        return self._getNumber(1)

    def setEventId(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(FullscreenEventViewModel, self)._initialize()
        self._addArrayProperty('rewards', Array())
        self._addNumberProperty('eventId', 0)
        self.onClose = self._addCommand('onClose')