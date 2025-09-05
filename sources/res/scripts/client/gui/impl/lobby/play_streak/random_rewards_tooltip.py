from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.daily.tooltips.random_rewards_tooltip_model import RandomRewardsTooltipModel
from gui.impl.pub import ViewImpl

class RandomRewardsTooltip(ViewImpl):

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.daily.tooltips.RandomRewardsTooltip())
        settings.model = RandomRewardsTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(RandomRewardsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RandomRewardsTooltip, self).getViewModel()