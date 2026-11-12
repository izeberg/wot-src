import json
from wotdecorators import noexcept
from uilogging.base.logger import MetricsLogger, FlowLogger
from new_year.skeletons.new_year import INewYearMetricsLogger, INewYearCurrencyController
from new_year.uilogging.constants import Actions, Items, FEATURE, Views
from new_year.gui.impl.gen.view_models.common.ny_currency_type_model import NyCurrencyType
from new_year.gui.shared.ny_level_helper import NewYearAtmospherePresenter
from helpers import dependency

class NewYearMetricsLogger(MetricsLogger, INewYearMetricsLogger):
    __nyCurrencyController = dependency.descriptor(INewYearCurrencyController)

    def __init__(self):
        super(NewYearMetricsLogger, self).__init__(FEATURE)

    @noexcept
    def logSwitcherOpened(self):
        self.log(action=Actions.OPEN, item=Items.ENV_SWITCHER)

    @noexcept
    def logQuestsScreenClosed(self, animation):
        self.log(action=Actions.CLOSE, item=Items.QUESTS, info=json.dumps({'animation': animation}))

    @noexcept
    def logQuestsVoiceoverSwitch(self, isEnabled):
        self.log(action=Actions.CLICK, item=Items.VOICEOVER_SWITCH, parentScreen=Views.QUESTS, info=json.dumps({'enabled': isEnabled}))

    @noexcept
    def logMachineScreenOpened(self, animation):
        mandarins = self.__nyCurrencyController.getCurrencyCount(NyCurrencyType.MANDARIN)
        tokens = self.__nyCurrencyController.getCurrencyCount(NyCurrencyType.NYGIFTMACHINETOKEN)
        atmosphereLevel = NewYearAtmospherePresenter.getLevel()
        self.log(action=Actions.OPEN, item=Items.MACHINE, info=json.dumps({'animation': animation, 
           'mandarins': mandarins, 
           'machine_tokens': tokens, 
           'atmosphere_lvl': atmosphereLevel}))

    @noexcept
    def logMachineScreenClosed(self, animation):
        self.log(action=Actions.CLOSE, item=Items.MACHINE, info=json.dumps({'animation': animation}))

    @noexcept
    def logMachineCoinExchange(self, count):
        self.log(action=Actions.CLICK, item=Items.MACHINE_BUY_BTN, parentScreen=Views.SURPRISE_MACHINE, info=json.dumps({'count': count}))

    @noexcept
    def logMachineTokenUsed(self, count):
        self.log(action=Actions.CLICK, item=Items.MACHINE_APPLY_BTN, parentScreen=Views.SURPRISE_MACHINE, info=json.dumps({'count': count}))

    @noexcept
    def logLeaderboardScreenOpened(self):
        self.log(action=Actions.OPEN, item=Items.LEADERBOARD)

    @noexcept
    def logWeeklyRewardsScreenOpened(self):
        self.log(action=Actions.OPEN, item=Items.WEEKLY_REWARDS)

    @noexcept
    def logPetScreenOpened(self):
        self.log(action=Actions.OPEN, item=Items.PET)

    @noexcept
    def logPetRepeatOnboardingClick(self, count):
        self.log(action=Actions.CLICK, item=Items.PET_REPEAT_ONBOARDING_BTN, parentScreen=Views.PET, info=json.dumps({'count': count}))

    @noexcept
    def logRaidRepeatOnboardingClick(self, count):
        self.log(action=Actions.CLICK, item=Items.RAID_REPEAT_ONBOARDING_BTN, parentScreen=Views.PET_RAID, info=json.dumps({'count': count}))

    @noexcept
    def logEasterEggVideoOpened(self, videoId):
        self.log(action=Actions.OPEN, item=Items.EASTER_EGG_VIDEO, info=json.dumps({'video_id': videoId}))


class NewYearFlowLogger(FlowLogger):

    def __init__(self):
        super(NewYearFlowLogger, self).__init__(FEATURE)