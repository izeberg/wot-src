from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_entry_point_view_model import CustomizationResourceEntryPointViewModel, StatusEnum
from gui.impl.pub import ViewImpl
from gui.shared.event_dispatcher import showCustomizationResourceShopPage
from gui.impl.lobby.customization_resource.shared import getCustomizationResourceLimitUpdated, setCustomizationResourceLimitFlags
from helpers import dependency
from skeletons.gui.game_control import ICustomizationResourceController

@dependency.replace_none_kwargs(customizationResource=ICustomizationResourceController)
def isCustomizationResourceEntryPointAvailable(customizationResource=None):
    return customizationResource.isStarted() and not customizationResource.isFinished()


class CustomizationResourceEntryPointView(ViewImpl):
    __customizationResourceController = dependency.descriptor(ICustomizationResourceController)
    __slots__ = ('__isSingle', )

    def __init__(self):
        settings = ViewSettings(R.views.lobby.customization_resource.CustomizationResourceEntryPointView())
        settings.model = CustomizationResourceEntryPointViewModel()
        super(CustomizationResourceEntryPointView, self).__init__(settings)
        self.__isSingle = True

    @property
    def viewModel(self):
        return super(CustomizationResourceEntryPointView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CustomizationResourceEntryPointView, self)._onLoading(*args, **kwargs)
        self.__updateViewModel()

    def setIsSingle(self, value):
        self.__isSingle = value
        self.__updateViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.toCustomizationResourceEvent, self.__onClick),
         (
          self.__customizationResourceController.onEventSettingsUpdated, self.__updateViewModel))

    def __onClick(self):
        setCustomizationResourceLimitFlags()
        showCustomizationResourceShopPage()

    def __getStatus(self):
        if self.__customizationResourceController.isEnding():
            return StatusEnum.ENDING
        if not self.__customizationResourceController.isEnabled():
            return StatusEnum.DISABLED
        return StatusEnum.ACTIVE

    def __updateViewModel(self):
        with self.viewModel.transaction() as (tx):
            tx.setIsAloneBanner(self.__isSingle)
            tx.setIsLimitsUpdated(getCustomizationResourceLimitUpdated())
            tx.setTimer(self.__customizationResourceController.getLocalEndDate())
            tx.setStatus(self.__getStatus())