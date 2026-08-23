from __future__ import absolute_import
from frameworks.wulf import WindowFlags, ViewSettings, ViewStatus
from gui.collection.collections_helpers import composeBonuses
from gui.impl.gen import R
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from helpers import dependency
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_rewards_view_model import JmRewardsViewModel
from journey_marathon.gui.shared.bonus_packers import getJMBonusPacker
from journey_marathon.skeletons.game_control import IJourneyMarathonController

class JmAnniversaryPresentView(ViewImpl):
    LAYOUT_ID = R.views.journey_marathon.mono.lobby.rewards_view()
    jmCtrl = dependency.descriptor(IJourneyMarathonController)

    def __init__(self, bonuses):
        super(JmAnniversaryPresentView, self).__init__(settings=ViewSettings(layoutID=self.LAYOUT_ID, model=JmRewardsViewModel(), args=(
         bonuses,)))
        self.__tooltips = {}

    @property
    def viewModel(self):
        return super(JmAnniversaryPresentView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(JmAnniversaryPresentView, self).createToolTip(event)

    def getTooltipData(self, event):
        return self.__tooltips.get(event.getArgument('tooltipId', None), None)

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__close),)

    def _onLoading(self, bonuses):
        super(JmAnniversaryPresentView, self)._onLoading()
        with self.viewModel.transaction() as (tx):
            composedBonuses = composeBonuses([bonuses])
            sortedBonuses = self.jmCtrl.jmBonuses.sortJmAnniversaryPresentBonuses(composedBonuses)
            bonusModels = tx.getRewards()
            bonusModels.clear()
            packBonusModelAndTooltipData(sortedBonuses, bonusModels, self.__tooltips, getJMBonusPacker())

    def _finalize(self):
        super(JmAnniversaryPresentView, self)._finalize()
        self.__tooltips = None
        return

    def __close(self):
        if self.viewStatus not in (ViewStatus.DESTROYING, ViewStatus.DESTROYED):
            self.destroyWindow()


class JmAnniversaryPresentWindow(LobbyNotificationWindow):

    def __init__(self, bonuses):
        super(JmAnniversaryPresentWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=JmAnniversaryPresentView(bonuses))