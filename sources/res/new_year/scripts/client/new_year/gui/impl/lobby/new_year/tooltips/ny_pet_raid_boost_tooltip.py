from frameworks.wulf import ViewSettings
from helpers import dependency, time_utils
from new_year.gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_pet_raid_boost_tooltip_model import NyPetRaidBoostTooltipModel
from gui.impl.pub import ViewImpl
from new_year.helpers.server_settings import getNewYearRaidConfig
from new_year.skeletons.new_year import INewYearController, INewYearTamagotchiController
from skeletons.gui.lobby_context import ILobbyContext
from gui.impl.gen import R

class NyPetRaidBoostTooltip(ViewImpl):
    __nyController = dependency.descriptor(INewYearController)
    __tamagotchiController = dependency.descriptor(INewYearTamagotchiController)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        settings = ViewSettings(R.views.new_year.lobby.new_year.tooltips.NyPetRaidBoostTooltip())
        settings.model = NyPetRaidBoostTooltipModel()
        super(NyPetRaidBoostTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyPetRaidBoostTooltip, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.__tamagotchiController.onRaidDataUpdated, self.__updateModel),
         (
          self.__lobbyContext.getServerSettings().onServerSettingsChange, self.__onServerSettingsChanged))

    def _initialize(self, *args, **kwargs):
        super(NyPetRaidBoostTooltip, self)._initialize(*args, **kwargs)
        self.__updateModel()

    def __onServerSettingsChanged(self, _):
        self.__updateModel()

    def __updateModel(self, *_):
        raidBoost = getNewYearRaidConfig().get('raidBoost', {})
        self.viewModel.setBoostAmount(self.__tamagotchiController.getRaidBoostAmount())
        self.viewModel.setMaxBoostLimit(raidBoost.get('limit', 0))
        self.viewModel.setBoostTime(raidBoost.get('boostTime', 0))
        self.viewModel.setBoostsToAdd(raidBoost.get('amount', 0))
        self.viewModel.setBoostAccrualTime(raidBoost.get('accrualTime', 0) + 3 * time_utils.ONE_HOUR)