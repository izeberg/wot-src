from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class SessionProgressRewardBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(SessionProgressRewardBonusModel, self).__init__(properties=properties, commands=commands)

    def getVehicleName(self):
        return self._getString(7)

    def setVehicleName(self, value):
        self._setString(7, value)

    def getVehicleType(self):
        return self._getString(8)

    def setVehicleType(self, value):
        self._setString(8, value)

    def getVehicleLevel(self):
        return self._getNumber(9)

    def setVehicleLevel(self, value):
        self._setNumber(9, value)

    def getIsElite(self):
        return self._getBool(10)

    def setIsElite(self, value):
        self._setBool(10, value)

    def getCompensatedBonus(self):
        return self._getString(11)

    def setCompensatedBonus(self, value):
        self._setString(11, value)

    def _initialize(self):
        super(SessionProgressRewardBonusModel, self)._initialize()
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('vehicleType', '')
        self._addNumberProperty('vehicleLevel', 0)
        self._addBoolProperty('isElite', False)
        self._addStringProperty('compensatedBonus', '')