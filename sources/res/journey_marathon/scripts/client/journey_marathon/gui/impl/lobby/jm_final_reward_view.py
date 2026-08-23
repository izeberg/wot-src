import typing
from frameworks.wulf import ViewSettings, ViewStatus, WindowFlags
from gui.impl.gen import R
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses
from gui.shared.view_helpers.blur_manager import CachedBlur
from helpers import dependency
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_final_reward_view_model import JmFinalRewardViewModel
from journey_marathon.gui.shared.bonus_packers import getJMBonusPacker
from journey_marathon.skeletons.game_control import IJourneyMarathonController
from skeletons.gui.app_loader import IAppLoader

class JmFinalRewardView(ViewImpl):
    jmCtrl = dependency.descriptor(IJourneyMarathonController)
    LAYOUT_ID = R.views.journey_marathon.mono.lobby.main_rewards()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(self.LAYOUT_ID)
        settings.model = JmFinalRewardViewModel()
        settings.args = args
        settings.kwargs = kwargs
        self.__tooltipItems = {}
        super(JmFinalRewardView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(JmFinalRewardView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(JmFinalRewardView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipItems.get(tooltipId)

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__close),)

    def _onLoading(self, nodeID, *args, **kwargs):
        super(JmFinalRewardView, self)._onLoading(*args, **kwargs)
        node = self.jmCtrl.jmNodes.getJmNodes().get(nodeID)
        bonuses = []
        for bonusName, bonusValue in node.bonus.items():
            bonuses.extend(getNonQuestBonuses(bonusName, bonusValue))

        self.__setAwards(bonuses)

    def _finalize(self):
        super(JmFinalRewardView, self)._finalize()
        self.__tooltipItems = None
        return

    def __setAwards(self, bonuses):
        mainRewards = self.__setMainRewards(bonuses)
        rewards = [ reward for reward in bonuses if reward not in mainRewards ]
        packBonusModelAndTooltipData(rewards, self.viewModel.getAdditionalRewards(), self.__tooltipItems, packer=getJMBonusPacker())

    def __setMainRewards(self, bonuses):
        mainRewards = []
        for bonus in bonuses:
            if bonus.getName() == 'vehicles':
                mainRewards.append(bonus)

        packBonusModelAndTooltipData(mainRewards, self.viewModel.getMainRewards(), self.__tooltipItems, packer=getJMBonusPacker())
        return mainRewards

    def __close(self):
        if self.viewStatus not in (ViewStatus.DESTROYING, ViewStatus.DESTROYED):
            self.destroyWindow()


class JmFinalRewardWindow(LobbyNotificationWindow):
    __slots__ = ('_blur', )
    __appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, nodeID):
        super(JmFinalRewardWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=JmFinalRewardView(nodeID))
        self._blur = None
        return

    def load(self):
        if self._blur is None:
            self._blur = CachedBlur(enabled=True, ownLayer=self.layer - 1)
        super(JmFinalRewardWindow, self).load()
        return

    def _initialize(self):
        super(JmFinalRewardWindow, self)._initialize()
        containerManager = self.__appLoader.getApp().containerManager
        if containerManager:
            containerManager.onViewAddedToContainer += self.__onViewLoaded

    def __onViewLoaded(self, _, *args):
        self._blur.enable()

    def _finalize(self):
        if self._blur:
            self._blur.fini()
        containerManager = self.__appLoader.getApp().containerManager
        if containerManager:
            containerManager.onViewAddedToContainer -= self.__onViewLoaded
        super(JmFinalRewardWindow, self)._finalize()