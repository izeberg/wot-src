import typing
from frameworks.wulf import ViewSettings
from helpers import dependency
from new_year.gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_pet_bonus_tooltip_model import NyPetBonusTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from new_year.ny_constants import PERCENT
from new_year.skeletons.new_year import INewYearController
if typing.TYPE_CHECKING:
    from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_model import NyPetModel

class NyPetBonusTooltip(ViewImpl):
    _nyController = dependency.descriptor(INewYearController)

    def __init__(self, petViewModel):
        settings = ViewSettings(R.views.new_year.lobby.new_year.tooltips.NyPetBonusTooltip())
        settings.model = NyPetBonusTooltipModel()
        self.__fillModel(settings.model, petViewModel)
        super(NyPetBonusTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyPetBonusTooltip, self).getViewModel()

    @classmethod
    def __fillModel(cls, model, petViewModel):
        with model.transaction() as (tx):
            cls.__fillIndicators(tx, petViewModel)
            tx.setMinBonus(cls._nyController.getActiveSettingBonusValue() * PERCENT)
            tx.setMaxBonus(petViewModel.getMaxBonus())
            tx.setCurrentBonus(petViewModel.getCurBonus())

    @classmethod
    def __fillIndicators(cls, model, petViewModel):
        array = model.getIndicators()
        array.clear()
        array.addViewModel(petViewModel.foodIndicator)
        array.addViewModel(petViewModel.funIndicator)
        array.addViewModel(petViewModel.activityIndicator)
        array.invalidate()