from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.common.mission_base_model import MissionBaseModel

class PremiumDailyMissionModel(MissionBaseModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(PremiumDailyMissionModel, self).__init__(properties=properties, commands=commands)

    def getIsLocked(self):
        return self._getBool(11)

    def setIsLocked(self, value):
        self._setBool(11, value)

    def _initialize(self):
        super(PremiumDailyMissionModel, self)._initialize()
        self._addBoolProperty('isLocked', False)