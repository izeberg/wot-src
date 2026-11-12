import typing, SoundGroups
from frameworks.wulf import ViewSettings, WindowLayer, ViewStatus
from gui.shared.money import Currency
from gui.impl.backport import TooltipData
from gui.impl.gen.resources import R
from gui.impl.lobby.awards import SupportedTokenTypes
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip
from helpers import dependency, isPlayerAccount
from messenger.proto.events import g_messengerEvents
from new_year.gui.impl.new_year.sounds import NewYearCelebVoiceOvers, OVERLAY_HANGAR_SOUND_SPACE
from new_year_common.items.components.ny_constants import CurrentNYConstants
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.quests.ny_quests_reward_model import NyQuestsRewardModel
from new_year.gui.impl.new_year.new_year_bonus_packer import packBonusModelAndTooltipData, getNewYearBonusPacker
from new_year.gui.shared.ny_machine_helper import getMachineLootboxToken
from new_year.gui.shared.ny_token_helper import getSmallLootBoxToken
from gui.impl.backport import BackportTooltipWindow
from new_year.skeletons.new_year import INewYearController
SMALL_LOOTBOX_TOKEN = getSmallLootBoxToken()
MACHINE_LOOTBOX_TOKEN = getMachineLootboxToken()
DEFAULT = 'default'
PET_CURRENCIES = 'currencies'
REWARDS_ORDER = (
 SMALL_LOOTBOX_TOKEN,
 MACHINE_LOOTBOX_TOKEN,
 PET_CURRENCIES,
 Currency.CREDITS,
 CurrentNYConstants.MANDARINS,
 DEFAULT)

def _bonusSortOrder(bonus):
    bonusName = bonus.getName()
    if bonusName == SupportedTokenTypes.LOOTBOX_TOKEN:
        bonusName = bonus.getTokens().keys()[0]
    if bonusName in REWARDS_ORDER:
        return REWARDS_ORDER.index(bonusName)
    return REWARDS_ORDER.index(DEFAULT)


class NyQuestsRewardView(ViewImpl):
    _COMMON_SOUND_SPACE = OVERLAY_HANGAR_SOUND_SPACE
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self, data, backCallback=None, voiceoverEvent=None, *args, **kwargs):
        settings = ViewSettings(R.views.new_year.lobby.new_year.NyQuestsRewardView())
        settings.model = NyQuestsRewardModel()
        settings.args = args
        settings.kwargs = kwargs
        super(NyQuestsRewardView, self).__init__(settings)
        self.__tooltips = {}
        self.__rewards = data
        self.__backCallback = backCallback
        self.__voiceoverEvent = voiceoverEvent

    @property
    def viewModel(self):
        return super(NyQuestsRewardView, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if R.views.dyn('gui_lootboxes').isValid() and contentID == R.views.dyn('gui_lootboxes').lobby.gui_lootboxes.tooltips.LootboxTooltip():
            tooltipData = self.__tooltips[event.getArgument('tooltipId')]
            return tooltipData.tooltip(*tooltipData.specialArgs)
        if contentID == R.views.lobby.tooltips.AdditionalRewardsTooltip() and self.viewStatus == ViewStatus.LOADED:
            showCount = int(event.getArgument('showedCount'))
            return AdditionalRewardsTooltip(self.__rewards[showCount:], getNewYearBonusPacker())
        return super(NyQuestsRewardView, self).createToolTipContent(event, contentID)

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument('tooltipId')
            window = None
            if tooltipId is not None:
                window = BackportTooltipWindow(self.__tooltips[tooltipId], self.getParentWindow())
                window.load()
            return window
        return super(NyQuestsRewardView, self).createToolTip(event)

    def _initialize(self, *args, **kwargs):
        super(NyQuestsRewardView, self)._initialize(*args, **kwargs)
        g_messengerEvents.onLockPopUpMessages(lockHigh=True)
        self.__rewards.sort(key=_bonusSortOrder)
        self.__updateRewards()
        self.__setRewardVoiceover(True)

    def _finalize(self):
        self.__setRewardVoiceover(False)
        g_messengerEvents.onUnlockPopUpMessages()
        super(NyQuestsRewardView, self)._finalize()
        self.__rewards = None
        self.__voiceoverEvent = None
        if callable(self.__backCallback) and isPlayerAccount():
            self.__backCallback()
        self.__backCallback = None
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onCloseAction),
         (
          self.__nyController.onStateChanged, self.__onEventStateChanged))

    def __updateRewards(self):
        with self.getViewModel().transaction() as (model):
            rewardsList = model.rewards.getItems()
            self.__tooltips.clear()
            rewardsList.clear()
            packBonusModelAndTooltipData(self.__rewards, rewardsList, getNewYearBonusPacker(), self.__tooltips)
            rewardsList.invalidate()

    def __onCloseAction(self):
        self.destroyWindow()

    def __onEventStateChanged(self):
        if not self.__nyController.isEnabled():
            self.destroyWindow()

    def __setRewardVoiceover(self, isEnabled):
        if not self.__voiceoverEvent:
            return
        event = self.__voiceoverEvent if isEnabled else NewYearCelebVoiceOvers.REWARD_STOP
        SoundGroups.g_instance.playSound2D(event)


class NyQuestRewardWindow(LobbyNotificationWindow):
    __slots__ = ('__blurBackground', '__worldDrawEnabled', '__worldOn', '__blur')

    def __init__(self, data, *args, **kwargs):
        super(NyQuestRewardWindow, self).__init__(content=NyQuestsRewardView(data, *args, **kwargs), layer=WindowLayer.OVERLAY)