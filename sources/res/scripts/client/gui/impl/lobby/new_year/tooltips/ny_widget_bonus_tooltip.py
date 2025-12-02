from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_economic_bonus_model import NyEconomicBonusModel
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_widget_bonus_tooltip_model import NyWidgetBonusTooltipModel, TooltipState
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from CurrentVehicle import g_currentVehicle
from new_year.ny_bonuses import getBonusStatus, getXpBonusNameByID, EconomicBonusHelper, toPrettyCumulativeBonusValue
from new_year.ny_level_helper import NewYearAtmospherePresenter
from ny_common.settings import BattleBonusesConsts

class NyWidgetBonusTooltip(ViewImpl):
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        settings = ViewSettings(R.views.mono.holiday_ops.tooltips.ho_widget_bonus_tooltip())
        settings.model = NyWidgetBonusTooltipModel()
        self.__currentVehicle = g_currentVehicle.item
        self.__chosenXPBonus = self._itemsCache.items.festivity.getChosenXPBonus()
        self.__errorStatus = getBonusStatus(vehicle=self.__currentVehicle, maxReachedLevel=NewYearAtmospherePresenter.getLevel())
        super(NyWidgetBonusTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyWidgetBonusTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        selectedBonusName = getXpBonusNameByID(self.__chosenXPBonus)
        economicBonuses = self.viewModel.getEconomicBonuses()
        economicBonuses.clear()
        with self.viewModel.transaction() as (model):
            self.__tooltipState(model)
            model.setLevel(self.__currentVehicle.level)
            model.setSelectedBonusName(selectedBonusName)
            bonuses = EconomicBonusHelper.getBonusesDataInventory()
            for bonusID, value in bonuses.iteritems():
                bonus = NyEconomicBonusModel()
                bonus.setBonusName(bonusID)
                bonus.setBonusValue(toPrettyCumulativeBonusValue(value))
                economicBonuses.addViewModel(bonus)
                if bonusID == selectedBonusName:
                    model.setSelectedBonusValue(toPrettyCumulativeBonusValue(value))

            economicBonuses.invalidate()

    def _finalize(self):
        self.__chosenXPBonus = None
        self.__errorStatus = None
        super(NyWidgetBonusTooltip, self)._finalize()
        return

    def __tooltipState(self, model):
        if self.__errorStatus == BattleBonusesConsts.LEVEL_ERROR:
            model.setTooltipState(TooltipState.LEVELERROR)
        if self.__errorStatus == BattleBonusesConsts.VEHICLE_ERROR:
            model.setTooltipState(TooltipState.VEHICLEERROR)