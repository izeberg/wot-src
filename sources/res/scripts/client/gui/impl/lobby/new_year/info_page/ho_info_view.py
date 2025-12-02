from constants import CURRENT_REALM
from gui.impl.gen.view_models.views.lobby.new_year.views.new_year_info_view_model import NewYearInfoViewModel
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen.resources import R
from gui.impl.lobby.new_year.ny_views_helpers import showInfoVideo
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.shared.event_dispatcher import showHolidayOpsLootBoxBuyWindow, showAboutEvent
from helpers import dependency, getLanguageCode
from new_year.ny_level_helper import getNYGeneralConfig
from skeletons.new_year import INewYearController

class HOInfoView(ViewImpl):
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.holiday_ops.info_view())
        settings.model = NewYearInfoViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(HOInfoView, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self):
        super(HOInfoView, self)._onLoading()
        generalConfig = getNYGeneralConfig()
        with self.viewModel.transaction() as (model):
            model.setEventStartDate(generalConfig.getEventStartTime())
            model.setEventEndDate(generalConfig.getEventEndTime())
            model.region.setRealm(CURRENT_REALM)
            model.region.setLanguage(getLanguageCode())

    def _getEvents(self):
        events = super(HOInfoView, self)._getEvents()
        return events + (
         (
          self.viewModel.videoCover.onClick, self.__onPlayVideo),
         (
          self.viewModel.onShowAboutEvent, self.__onShowAboutEvent),
         (
          self.viewModel.onShowRewardKitBuyWindow, self.__onShowRewardKitBuyWindow),
         (
          self.__nyController.onStateChanged, self.__onEventStateChanged))

    @staticmethod
    def __onShowAboutEvent():
        showAboutEvent()

    @staticmethod
    def __onPlayVideo():
        showInfoVideo()

    @staticmethod
    def __onShowRewardKitBuyWindow():
        showHolidayOpsLootBoxBuyWindow()

    def __onEventStateChanged(self):
        if not self.__nyController.isEnabled():
            self.destroyWindow()


class HOInfoViewWindow(LobbyWindow):

    def __init__(self, *args, **kwargs):
        super(HOInfoViewWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=HOInfoView(*args, **kwargs), layer=WindowLayer.WINDOW)