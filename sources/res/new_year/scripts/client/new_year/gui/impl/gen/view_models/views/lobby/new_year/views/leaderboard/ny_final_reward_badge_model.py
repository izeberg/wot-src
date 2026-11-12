from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class NyFinalRewardBadgeModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(NyFinalRewardBadgeModel, self).__init__(properties=properties, commands=commands)

    def getIsRewarded(self):
        return self._getBool(8)

    def setIsRewarded(self, value):
        self._setBool(8, value)

    def _initialize(self):
        super(NyFinalRewardBadgeModel, self)._initialize()
        self._addBoolProperty('isRewarded', False)