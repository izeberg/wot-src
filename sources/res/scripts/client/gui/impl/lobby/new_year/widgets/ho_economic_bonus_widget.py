from CurrentVehicle import g_currentVehicle
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.widgets.ho_economic_bonus_widget_model import HoEconomicBonusWidgetModel
from gui.impl.lobby.new_year.tooltips.ho_economic_bonus_simple_tooltip import HOEconomicBonusSimpleTooltip
from gui.impl.lobby.new_year.tooltips.ny_widget_bonus_tooltip import NyWidgetBonusTooltip
from gui.impl.lobby.new_year.popovers.ho_economic_bonus_popover import HOEconomicBonusPopover
from gui.impl.lobby.new_year.states import AssignmentsState
from gui.impl.pub.view_component import ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from new_year.ny_bonuses import isBonusApplicable, EconomicBonusHelper, getXpBonusNameByID, toPrettyCumulativeBonusValue
from new_year.ny_constants import SyncDataKeys
from new_year.ny_level_helper import NewYearAtmospherePresenter
from helpers import dependency
from skeletons.new_year import INewYearController, ICelebrityController
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.shared import IItemsCache

class HOEconomicBonusWidget(ViewComponent[HoEconomicBonusWidgetModel]):
    __nyController = dependency.descriptor(INewYearController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __celebrityController = dependency.descriptor(ICelebrityController)
    __guiLoader = dependency.descriptor(IGuiLoader)

    def __init__(self):
        super(HOEconomicBonusWidget, self).__init__(model=HoEconomicBonusWidgetModel)

    @property
    def viewModel(self):
        return super(HOEconomicBonusWidget, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.mono.holiday_ops.tooltips.ho_widget_bonus_tooltip():
            return NyWidgetBonusTooltip()
        if contentID == R.views.mono.holiday_ops.tooltips.ho_economic_bonus_simple_tooltip():
            header = event.getArgument('header', '')
            body = event.getArgument('body', '')
            return HOEconomicBonusSimpleTooltip(header, body)
        return super(HOEconomicBonusWidget, self).createToolTipContent(event, contentID)

    def createPopOverContent(self, event):
        if event.contentID == R.views.mono.holiday_ops.popovers.ho_economic_bonus_popover():
            return HOEconomicBonusPopover()
        return super(HOEconomicBonusWidget, self).createPopOverContent(event)

    def _getEvents(self):
        return (
         (
          self.__nyController.onDataUpdated, self.__onDataUpdated),
         (
          self.__nyController.onStateChanged, self.__updateBonusError),
         (
          self.__celebrityController.onCelebCompletedTokensUpdated, self.__onCelebCompletedTokensUpdated),
         (
          self.viewModel.onGoToAssignments, self.__onGoToAssignments),
         (
          g_currentVehicle.onChanged, self.__onCurrentVehicleChanged))

    def _onLoading(self, *args, **kwargs):
        super(HOEconomicBonusWidget, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            self.__updateSelectedBonus(model)
            self.__updateBonusError(model=model)

    def __onGoToAssignments(self):
        if self.__nyController.isEnabled():
            AssignmentsState.goTo()

    def __onDataUpdated(self, keys, _):
        if SyncDataKeys.XP_BONUS_CHOICE in keys:
            with self.viewModel.transaction() as (model):
                self.__updateSelectedBonus(model)

    def __onCurrentVehicleChanged(self):
        self.__updateBonusError()

    @replaceNoneKwargsModel
    def __updateBonusError(self, model=None):
        bonusError = isBonusApplicable(g_currentVehicle.item, NewYearAtmospherePresenter.getLevel())
        model.setBonusError(bonusError)

    def __updateSelectedBonus(self, model):
        selectedBonusID = self.__itemsCache.items.festivity.getChosenXPBonus()
        selectedBonusName = getXpBonusNameByID(selectedBonusID)
        model.setSelectedBonusName(selectedBonusName)
        self.__onCelebCompletedTokensUpdated()

    def __onCelebCompletedTokensUpdated(self):
        with self.viewModel.transaction() as (model):
            self.__updateEconomicBonusValues(model)

    def __updateEconomicBonusValues(self, model):
        selectedBonusID = self.__itemsCache.items.festivity.getChosenXPBonus()
        selectedBonusName = getXpBonusNameByID(selectedBonusID)
        bonuses = EconomicBonusHelper.getBonusesDataInventory()
        for bonusID, value in bonuses.iteritems():
            if bonusID == selectedBonusName:
                model.setSelectedBonusValue(toPrettyCumulativeBonusValue(value))