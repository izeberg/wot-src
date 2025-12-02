from frameworks.wulf import ViewSettings, WindowLayer, ViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.pub.dialog_window import DialogFlags
from gui.impl.pub.lobby_window import LobbyWindow
from gui.shared.view_helpers.blur_manager import CachedBlur
from helpers import dependency
from skeletons.new_year import INewYearController

class HOResourcesIntroView(ViewImpl):
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self):
        settings = ViewSettings(R.views.mono.user_missions.ho_resources_intro_view())
        settings.model = ViewModel()
        super(HOResourcesIntroView, self).__init__(settings)

    def _getEvents(self):
        events = super(HOResourcesIntroView, self)._getEvents()
        return events + (
         (
          self.__nyController.onStateChanged, self.__onEventStateChanged),)

    def __onEventStateChanged(self):
        if not self.__nyController.isEnabled():
            self.destroyWindow()


class HOResourcesIntroWindow(LobbyWindow):

    def __init__(self):
        super(HOResourcesIntroWindow, self).__init__(DialogFlags.TOP_FULLSCREEN_WINDOW, content=HOResourcesIntroView(), layer=WindowLayer.FULLSCREEN_WINDOW)
        self.__blur = None
        return

    def _initialize(self):
        super(HOResourcesIntroWindow, self)._initialize()
        self.__blur = CachedBlur(enabled=True, ownLayer=self.layer - 1)

    def _finalize(self):
        if self.__blur is not None:
            self.__blur.fini()
        super(HOResourcesIntroWindow, self)._finalize()
        return