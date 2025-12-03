import typing
from config_schemas.umg_config import umgConfigSchema
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.user_missions.info_page_model import InfoPageModel
from gui.impl.pub import ViewImpl
from gui.server_events.events_helpers import getRerollTimeout
from helpers import dependency
from skeletons.new_year import INewYearController

class InfoPageView(ViewImpl):
    __hoController = dependency.descriptor(INewYearController)

    def __init__(self, settings, *args, **kwargs):
        super(InfoPageView, self).__init__(settings, args, kwargs)

    @property
    def viewModel(self):
        return super(InfoPageView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self._onViewClose),)

    def _onLoading(self, *args, **kwargs):
        super(InfoPageView, self)._onLoading(*args, **kwargs)
        self.viewModel.setRerollInterval(getRerollTimeout())
        self.viewModel.setIsWeeklySectionAvailable(umgConfigSchema.getModel().enableAllWeekly)
        self.viewModel.setIsHolidayOpsActive(self.__hoController.isEnabled())

    def _onViewClose(self):
        self.destroyWindow()