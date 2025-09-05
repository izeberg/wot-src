from frameworks.wulf import ViewSettings
from white_tiger.gui.impl.gen.view_models.views.lobby.tooltips.cinematic_tooltip_model import CinematicTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class CinematicTooltip(ViewImpl):
    __slots__ = ('__isOutroTooltip', '__isProgressionCompleted')

    def __init__(self, isOutroTooltip, isProgressionCompleted):
        settings = ViewSettings(R.views.white_tiger.lobby.tooltips.CinematicTooltip())
        settings.model = CinematicTooltipModel()
        self.__isOutroTooltip = isOutroTooltip
        self.__isProgressionCompleted = isProgressionCompleted
        super(CinematicTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CinematicTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CinematicTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            model.setIsOutroTooltip(self.__isOutroTooltip)
            model.setIsProgressionCompleted(self.__isProgressionCompleted)