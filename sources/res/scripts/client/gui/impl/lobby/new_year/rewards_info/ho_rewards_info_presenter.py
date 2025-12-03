import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.new_year.rewards_info.level_reward_presenter import LevelRewardPresenter
from new_year.ny_level_helper import getLevelIndexes
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from gui.impl.gen.view_models.views.lobby.new_year.views.rewards_info.ny_levels_rewards_model import NyLevelsRewardsModel
from helpers import dependency
from skeletons.new_year import INewYearController
if typing.TYPE_CHECKING:
    from typing import List

class HORewardsInfoPresenter(SubModelPresenter):
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self, viewModel, parentView):
        super(HORewardsInfoPresenter, self).__init__(viewModel, parentView)
        self.__levels = []

    @property
    def viewModel(self):
        return self.getViewModel()

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            toolTipData = None
            tooltipId = event.getArgument('tooltipId')
            idx = event.getArgument('idx')
            if idx is not None:
                toolTipData = self.__levels[int(idx)].createToolTipData(tooltipId)
            if not toolTipData:
                return
            window = backport.BackportTooltipWindow(toolTipData, self.parentView.getParentWindow(), event)
            window.load()
            return window
        else:
            return super(HORewardsInfoPresenter, self).createToolTip(event)

    def createToolTipContent(self, event, ctID):
        toolTipContent = None
        idx = event.getArgument('idx')
        if idx is not None:
            toolTipContent = self.__levels[int(idx)].createToolTipContent(event, ctID)
        return toolTipContent

    def initialize(self, *args, **kwargs):
        super(HORewardsInfoPresenter, self).initialize(*args, **kwargs)
        self.__createData()

    def finalize(self):
        while self.__levels:
            self.__levels.pop().clear()

        super(HORewardsInfoPresenter, self).finalize()

    def _getEvents(self):
        return (
         (
          self.__nyController.onDataUpdated, self.__onDataUpdated),)

    def __onDataUpdated(self, *_):
        self.__updateData()

    def __createData(self):
        for index, level in enumerate(getLevelIndexes()):
            self.__levels.append(LevelRewardPresenter(index, level))

        with self.viewModel.transaction() as (tx):
            renderers = tx.rewardRenderers.getItems()
            renderers.clear()
            for levelPresenter in self.__levels:
                renderer = levelPresenter.getRenderer()
                renderers.addViewModel(renderer)

            renderers.invalidate()

    def __updateData(self):
        with self.viewModel.transaction() as (tx):
            renderers = tx.rewardRenderers.getItems()
            for idx, renderer in enumerate(renderers):
                self.__levels[idx].updateRenderer(renderer)