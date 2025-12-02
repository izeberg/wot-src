from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ho_challenge_token_tooltip_model import HoChallengeTokenTooltipModel, TokenType
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.new_year import ICelebritySceneController

class NyChallengeTokenTooltip(ViewImpl):
    __celebritySceneController = dependency.descriptor(ICelebritySceneController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.holiday_ops.tooltips.ho_challenge_token_tooltip(), model=HoChallengeTokenTooltipModel())
        settings.args = args
        settings.kwargs = kwargs
        super(NyChallengeTokenTooltip, self).__init__(settings, *args, **kwargs)

    @property
    def viewModel(self):
        return super(NyChallengeTokenTooltip, self).getViewModel()

    def _onLoading(self, tokenType):
        with self.viewModel.transaction() as (model):
            model.setMissionsAmount(self.__celebritySceneController.questsCount)
            model.setTokenType(TokenType(tokenType))