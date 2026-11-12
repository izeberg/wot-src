from enum import Enum
from frameworks.wulf import ViewModel

class PetTvAnimation(Enum):
    OFF = 'off'
    WALK = 'walk'
    FOOD = 'food'
    CARE = 'care'
    ACTIVITY = 'activity'


class NyPetTvScreenViewModel(ViewModel):
    __slots__ = ('onAnimationFinished', 'onResetToIdle')

    def __init__(self, properties=2, commands=2):
        super(NyPetTvScreenViewModel, self).__init__(properties=properties, commands=commands)

    def getIsRaidActive(self):
        return self._getBool(0)

    def setIsRaidActive(self, value):
        self._setBool(0, value)

    def getAnimation(self):
        return PetTvAnimation(self._getString(1))

    def setAnimation(self, value):
        self._setString(1, value.value)

    def _initialize(self):
        super(NyPetTvScreenViewModel, self)._initialize()
        self._addBoolProperty('isRaidActive', False)
        self._addStringProperty('animation', PetTvAnimation.OFF.value)
        self.onAnimationFinished = self._addCommand('onAnimationFinished')
        self.onResetToIdle = self._addCommand('onResetToIdle')