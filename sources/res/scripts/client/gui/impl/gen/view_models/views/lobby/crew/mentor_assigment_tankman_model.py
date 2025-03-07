from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class MentorAssigmentTankmanModel(TankmanModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(MentorAssigmentTankmanModel, self).__init__(properties=properties, commands=commands)

    def getTotalXP(self):
        return self._getNumber(23)

    def setTotalXP(self, value):
        self._setNumber(23, value)

    def getLostXP(self):
        return self._getNumber(24)

    def setLostXP(self, value):
        self._setNumber(24, value)

    def _initialize(self):
        super(MentorAssigmentTankmanModel, self)._initialize()
        self._addNumberProperty('totalXP', 0)
        self._addNumberProperty('lostXP', 0)