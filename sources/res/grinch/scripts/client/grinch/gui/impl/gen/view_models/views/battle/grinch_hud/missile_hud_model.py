from frameworks.wulf import ViewModel
from grinch.gui.impl.gen.view_models.views.battle.grinch_missile_target_marker_model import GrinchMissileTargetMarkerModel

class MissileHudModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(MissileHudModel, self).__init__(properties=properties, commands=commands)

    @property
    def currentTargetMarker(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentTargetMarkerType():
        return GrinchMissileTargetMarkerModel

    @property
    def lostTargetMarkerEven(self):
        return self._getViewModel(1)

    @staticmethod
    def getLostTargetMarkerEvenType():
        return GrinchMissileTargetMarkerModel

    @property
    def lostTargetMarkerOdd(self):
        return self._getViewModel(2)

    @staticmethod
    def getLostTargetMarkerOddType():
        return GrinchMissileTargetMarkerModel

    def getPercentageX(self):
        return self._getNumber(3)

    def setPercentageX(self, value):
        self._setNumber(3, value)

    def getPercentageY(self):
        return self._getNumber(4)

    def setPercentageY(self, value):
        self._setNumber(4, value)

    def getIsTargeting(self):
        return self._getBool(5)

    def setIsTargeting(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(MissileHudModel, self)._initialize()
        self._addViewModelProperty('currentTargetMarker', GrinchMissileTargetMarkerModel())
        self._addViewModelProperty('lostTargetMarkerEven', GrinchMissileTargetMarkerModel())
        self._addViewModelProperty('lostTargetMarkerOdd', GrinchMissileTargetMarkerModel())
        self._addNumberProperty('percentageX', 0)
        self._addNumberProperty('percentageY', 0)
        self._addBoolProperty('isTargeting', False)