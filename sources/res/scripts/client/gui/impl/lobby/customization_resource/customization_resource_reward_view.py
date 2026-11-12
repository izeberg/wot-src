import BigWorld
from copy import deepcopy
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.customization_resource.common import getCustomizationResourceRewardsBonusPacker
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_reward_view_model import CustomizationResourceRewardViewModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.lobby.customization_resource.shared import closeWindowHandler
from gui.impl.lobby.customization_resource.tooltips.customization_resource_currency_tooltip_view import CustomizationResourceCurrencyTooltipView
from gui.impl.pub import ViewImpl, WindowImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.server_events.bonuses import getNonQuestBonuses, mergeBonuses, splitBonuses
from helpers import dependency
from skeletons.gui.game_control import ICustomizationResourceController
_DELAY_TO_SHOW_REWARD = 0.3

class CustomizationResourceRewardView(ViewImpl):
    __customizationResourceController = dependency.descriptor(ICustomizationResourceController)
    __slots__ = ('__tooltipData', '__rewards')

    def __init__(self, layoutID, rewards=None):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = CustomizationResourceRewardViewModel()
        self.__rewards = deepcopy(rewards) if rewards else {}
        self.__tooltipData = {}
        super(CustomizationResourceRewardView, self).__init__(settings)

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(CustomizationResourceRewardView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipData.get(tooltipId)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.customization_resource.tooltips.CustomizationResourceCurrencyTooltipView():
            return CustomizationResourceCurrencyTooltipView()
        return super(CustomizationResourceRewardView, self).createToolTipContent(event, contentID)

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.__customizationResourceController.onEventSettingsUpdated, self.__onEventSettingsUpdated))

    def _onLoading(self, *args, **kwargs):
        super(CustomizationResourceRewardView, self)._onLoading(*args, **kwargs)
        self.__fillRewardsModel()

    def _onReady(self):
        BigWorld.callback(_DELAY_TO_SHOW_REWARD, self.gui.windowsManager.getViewByLayoutID(R.views.lobby.customization_resource.CustomizationResourceVideoRewardView()).destroyWindow)

    def __onEventSettingsUpdated(self):
        closeWindowHandler(self)

    def __onClose(self):
        self.destroyWindow()

    @property
    def viewModel(self):
        return super(CustomizationResourceRewardView, self).getViewModel()

    @replaceNoneKwargsModel
    def __fillRewardsModel(self, model=None):
        rewardsList = model.getRewards()
        mainRewardsList = model.getMainRewards()
        rewardsList.clear()
        mainRewardsList.clear()
        rewards = []
        for bonusType, bonusValue in self.__rewards.iteritems():
            rewards.extend(getNonQuestBonuses(bonusType, bonusValue))

        rewards = splitBonuses(mergeBonuses(rewards))
        maxMainRewards = CustomizationResourceRewardViewModel.MAX_MAIN_REWARDS
        mainRewards = rewards[:maxMainRewards]
        rewards = rewards[maxMainRewards:]
        if len(mainRewards) == maxMainRewards:
            mainRewards[0], mainRewards[1] = mainRewards[1], mainRewards[0]
        packer = getCustomizationResourceRewardsBonusPacker()
        packBonusModelAndTooltipData(mainRewards, mainRewardsList, self.__tooltipData, packer)
        packBonusModelAndTooltipData(rewards, rewardsList, self.__tooltipData, packer, len(mainRewardsList))
        rewardsList.invalidate()
        mainRewardsList.invalidate()


class CustomizationResourceRewardViewWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, rewards, parent=None):
        super(CustomizationResourceRewardViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=CustomizationResourceRewardView(R.views.lobby.customization_resource.CustomizationResourceRewardView(), rewards), layer=WindowLayer.FULLSCREEN_WINDOW, parent=parent)