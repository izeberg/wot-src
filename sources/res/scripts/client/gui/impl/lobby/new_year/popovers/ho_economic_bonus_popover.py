from frameworks.wulf import ViewSettings
from gui.impl.gen.resources import R
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_economic_bonus_model import NyEconomicBonusModel
from gui.impl.gen.view_models.views.lobby.new_year.popovers.ho_economic_bonus_popover_model import HoEconomicBonusPopoverModel
from gui.impl.lobby.new_year.tooltips.ho_economic_bonus_simple_tooltip import HOEconomicBonusSimpleTooltip
from gui.impl.lobby.new_year.tooltips.ny_widget_bonus_tooltip import NyWidgetBonusTooltip
from gui.impl.pub import PopOverViewImpl
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from skeletons.gui.system_messages import ISystemMessages
from skeletons.new_year import INewYearController
from new_year.ny_constants import SyncDataKeys
from new_year.ny_bonuses import EconomicBonusHelper, getXpBonusNameByID, getXpBonusIDbyName, toPrettyCumulativeBonusValue

class HOEconomicBonusPopover(PopOverViewImpl):
    __nyController = dependency.descriptor(INewYearController)
    __systemMessages = dependency.descriptor(ISystemMessages)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        settings = ViewSettings(R.views.mono.holiday_ops.popovers.ho_economic_bonus_popover())
        settings.model = HoEconomicBonusPopoverModel()
        super(HOEconomicBonusPopover, self).__init__(settings)

    @property
    def viewModel(self):
        return super(HOEconomicBonusPopover, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.mono.holiday_ops.tooltips.ho_widget_bonus_tooltip():
            return NyWidgetBonusTooltip()
        if contentID == R.views.mono.holiday_ops.tooltips.ho_economic_bonus_simple_tooltip():
            header = event.getArgument('header', '')
            body = event.getArgument('body', '')
            return HOEconomicBonusSimpleTooltip(header, body)
        return super(HOEconomicBonusPopover, self).createToolTipContent(event, contentID)

    def _onLoading(self, *args, **kwargs):
        super(HOEconomicBonusPopover, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            self.__updateEconomicBonus(model)
            self.__updateSelectedBonus(model)

    def _getEvents(self):
        return (
         (
          self.__nyController.onDataUpdated, self.__onDataUpdated),
         (
          self.__nyController.onStateChanged, self.__onEventStateChanged),
         (
          self.viewModel.onSelectBonus, self.__onSelectBonus))

    def __onDataUpdated(self, keys, _):
        if SyncDataKeys.XP_BONUS_CHOICE in keys:
            with self.viewModel.transaction() as (model):
                self.__updateSelectedBonus(model)

    @staticmethod
    def __updateEconomicBonus(model):
        bonuses = EconomicBonusHelper.getBonusesDataInventory()
        economicBonuses = model.getEconomicBonuses()
        economicBonuses.clear()
        for bonusID, value in bonuses.iteritems():
            bonus = NyEconomicBonusModel()
            bonus.setBonusName(bonusID)
            bonus.setBonusValue(toPrettyCumulativeBonusValue(value))
            economicBonuses.addViewModel(bonus)

        economicBonuses.invalidate()

    def __onSelectBonus(self, args):
        bonusName = str(args['bonusName'])
        selectedBonusID = getXpBonusIDbyName(bonusName)
        if selectedBonusID is not None:
            self.__nyController.chooseXPBonus(selectedBonusID)
        return

    def __updateSelectedBonus(self, model):
        selectedBonusID = self.__itemsCache.items.festivity.getChosenXPBonus()
        model.setSelectedBonusName(getXpBonusNameByID(selectedBonusID))

    def __onEventStateChanged(self):
        if not self.__nyController.isEnabled():
            self.destroyWindow()