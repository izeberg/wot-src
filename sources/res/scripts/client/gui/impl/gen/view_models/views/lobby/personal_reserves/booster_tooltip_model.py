from gui.impl.gen.view_models.common.personal_reserves.booster_model import BoosterModel

class BoosterTooltipModel(BoosterModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(BoosterTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(BoosterTooltipModel, self)._initialize()