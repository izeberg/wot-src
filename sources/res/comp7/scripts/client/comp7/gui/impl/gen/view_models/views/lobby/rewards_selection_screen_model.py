from gui.impl.gen.view_models.views.lobby.common.selectable_reward_base_model import SelectableRewardBaseModel

class RewardsSelectionScreenModel(SelectableRewardBaseModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RewardsSelectionScreenModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(RewardsSelectionScreenModel, self)._initialize()