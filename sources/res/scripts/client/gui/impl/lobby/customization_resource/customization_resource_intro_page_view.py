from account_helpers import AccountSettings
from account_helpers.AccountSettings import SHOWN_CUSTOMIZATION_RESOURCE_INTRO
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_intro_page_view_model import CustomizationResourceIntroPageViewModel
from gui.impl.lobby.customization_resource.shared import closeWindowHandler
from gui.impl.pub import ViewImpl, WindowImpl
from helpers import dependency
from skeletons.gui.game_control import ICustomizationResourceController

class CustomizationResourceIntroPageView(ViewImpl):
    __customizationResourceController = dependency.descriptor(ICustomizationResourceController)
    __slots__ = ()

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = CustomizationResourceIntroPageViewModel()
        super(CustomizationResourceIntroPageView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CustomizationResourceIntroPageView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CustomizationResourceIntroPageView, self)._onLoading(*args, **kwargs)
        AccountSettings.setSettings(SHOWN_CUSTOMIZATION_RESOURCE_INTRO, True)
        self.__updateViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.__customizationResourceController.onEventSettingsUpdated, self.__onEventSettingsUpdated))

    def __updateViewModel(self):
        with self.viewModel.transaction() as (tx):
            tx.setStartTimestamp(self.__customizationResourceController.getLocalStartDate())
            tx.setEndTimestamp(self.__customizationResourceController.getLocalEndDate())

    def __onClose(self):
        self.destroyWindow()

    def __onEventSettingsUpdated(self):
        closeWindowHandler(self)


class CustomizationResourceIntroPageViewWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, parent=None):
        super(CustomizationResourceIntroPageViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=CustomizationResourceIntroPageView(R.views.lobby.customization_resource.CustomizationResourceIntroPageView()), parent=parent)