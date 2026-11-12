from new_year.gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_main_widget_tooltip_model import NyMainWidgetTooltipModel, WidgetBlock
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_indicator_model import NyPetIndicatorModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_indicator_type import IndicatorType
from new_year.gui.impl.lobby.new_year.pet.ny_pet_indicators_block import NyPetIndicatorsBlock
from new_year.gui.impl.gen.view_models.common.ny_event_state_model import EventState
from new_year_common.items.components.ny_constants import MAX_ATMOSPHERE_LVL
from new_year.gui.shared.ny_level_helper import NewYearAtmospherePresenter
from new_year.helpers.server_settings import getNewYearGeneralConfig
from new_year.ny_constants import NY_LAST_SEEN_LEVEL_INFO, PERCENT
from skeletons.account_helpers.settings_core import ISettingsCore
from new_year.skeletons.new_year import INewYearController, ITamagotchiDataProvider, INewYearTamagotchiController
from frameworks.wulf import View, ViewSettings
from new_year_account_settings import setNYSettings
from helpers import dependency, time_utils
from helpers.time_utils import ONE_WEEK
from new_year_common.items.components.ny_constants import RaidState
from gui.impl.gen import R

class NyMainWidgetTooltip(View):
    __slots__ = ('__block', )
    __nyController = dependency.descriptor(INewYearController)
    __settingsCore = dependency.descriptor(ISettingsCore)
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    _tamagotchiController = dependency.descriptor(INewYearTamagotchiController)

    def __init__(self, block=None):
        settings = ViewSettings(R.views.new_year.lobby.new_year.tooltips.NyMainWidgetTooltip())
        settings.model = NyMainWidgetTooltipModel()
        blockType = WidgetBlock(block)
        self.__block = blockType
        super(NyMainWidgetTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyMainWidgetTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        level = NewYearAtmospherePresenter.getLevel()
        leftLevel = level if level != MAX_ATMOSPHERE_LVL else level - 1
        currentPoints, nextPoints = NewYearAtmospherePresenter.getLevelProgress()
        endDate = getNewYearGeneralConfig().getNewYearEndDate()
        timeLeft = endDate - time_utils.getCurrentLocalServerTimestamp()
        raidState = self._dataProvider.getRaidState()
        with self.viewModel.transaction() as (tx):
            tx.setMaxBonus(self.__nyController.getMaxBonusValue() * PERCENT)
            tx.setBonus(self.__nyController.getActiveSettingBonusValue() * PERCENT + self._dataProvider.getDeb())
            tx.setCurrentLevel(level)
            tx.setCurrentPoints(currentPoints)
            tx.setNextLevelPoints(nextPoints)
            tx.setBlockState(self.__block)
            tx.setIsFirstEntry(not self.__nyController.isOnboardingFinished())
            tx.eventState.setValue(EventState.ACTIVE if self.__nyController.isEnabled() else EventState.PAUSED)
            tx.setIsPetPaused(not self._tamagotchiController.isPetVisible)
            tx.setIsWithLeaderboard(not self._dataProvider.isLeaderboardFinished)
            tx.setRewardsCount(self.__nyController.getVariadicDiscountCount())
            tx.setIsReadyRaid(raidState != RaidState.ACTIVE)
            self.__fillIndicators(tx)
            if level < MAX_ATMOSPHERE_LVL and timeLeft <= ONE_WEEK:
                tx.setIsNeedTimer(True)
                tx.setTimeLeft(timeLeft)
        setNYSettings(NY_LAST_SEEN_LEVEL_INFO, {'level': leftLevel, 'points': currentPoints})

    def __fillIndicators(self, tx):
        indicators = tx.getIndicators()
        indicators.clear()
        for indicatorName, points in self._dataProvider.playerInfo.indicators.iteritems():
            vm = NyPetIndicatorModel()
            NyPetIndicatorsBlock.applyIndicatorData(indicatorName, vm, points)
            vm.setType(IndicatorType(indicatorName))
            indicators.addViewModel(vm)

        indicators.invalidate()