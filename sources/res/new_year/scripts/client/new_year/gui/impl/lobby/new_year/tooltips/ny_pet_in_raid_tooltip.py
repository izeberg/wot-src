from frameworks.wulf import ViewSettings
from helpers import dependency
from new_year.gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_pet_in_raid_tooltip_model import NyPetInRaidTooltipModel
from gui.impl.pub import ViewImpl
from new_year.helpers.server_settings import getNewYearRaidConfig
from new_year.skeletons.new_year import INewYearController, INewYearTamagotchiController, ITamagotchiDataProvider
from skeletons.gui.lobby_context import ILobbyContext
from gui.impl.gen import R

class NyPetInRaidTooltip(ViewImpl):
    __nyController = dependency.descriptor(INewYearController)
    __tamagotchiController = dependency.descriptor(INewYearTamagotchiController)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __dataProvider = dependency.descriptor(ITamagotchiDataProvider)

    def __init__(self):
        settings = ViewSettings(R.views.new_year.lobby.new_year.tooltips.NyPetInRaidTooltip())
        settings.model = NyPetInRaidTooltipModel()
        super(NyPetInRaidTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyPetInRaidTooltip, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.__tamagotchiController.onRaidDataUpdated, self.__updateModel),
         (
          self.__lobbyContext.getServerSettings().onServerSettingsChange, self.__onServerSettingsChanged))

    def _initialize(self, *args, **kwargs):
        super(NyPetInRaidTooltip, self)._initialize(*args, **kwargs)
        self.__updateModel()

    def __onServerSettingsChanged(self, _):
        self.__updateModel()

    def __updateModel(self, *_):
        raidBoost = getNewYearRaidConfig().get('raidBoost', {})
        remainingTime = self.__dataProvider.getRaidRemainingTime()
        self.viewModel.setRaidRemainingTime(remainingTime)
        self.viewModel.setBoostAmount(self.__tamagotchiController.getRaidBoostAmount())
        self.viewModel.setMaxBoostLimit(raidBoost.get('limit', 0))
        self.viewModel.setBoostTime(raidBoost.get('boostTime', 0))