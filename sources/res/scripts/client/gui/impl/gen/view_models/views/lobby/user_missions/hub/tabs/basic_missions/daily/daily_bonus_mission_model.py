from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.common.mission_base_model import MissionBaseModel

class DailyBonusMissionModel(MissionBaseModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(DailyBonusMissionModel, self).__init__(properties=properties, commands=commands)

    def getIsAvailable(self):
        return self._getBool(10)

    def setIsAvailable(self, value):
        self._setBool(10, value)

    def _initialize(self):
        super(DailyBonusMissionModel, self)._initialize()
        self._addBoolProperty('isAvailable', False)