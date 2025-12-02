import typing
from gui.impl.gen.view_models.views.lobby.new_year.components.ho_main_widget_model import HoMainWidgetModel
from gui.impl.gen.view_models.views.lobby.new_year.views.hangar_name_view_model import TypeView
from gui.impl.lobby.new_year.states import GladeFirState
from gui.impl.lobby.new_year.ho_main_widget_helpers import WidgetLevelProgressHelper
from gui.impl.new_year.sounds import NewYearSoundsManager, NewYearSoundVars
from gui.impl.pub.view_component import ViewComponent
from gui.shared.event_dispatcher import showNYHangarNameSelectionWindow
from helpers import dependency
from new_year.ny_helper import getNYGeneralConfig
from new_year.ny_level_helper import NewYearAtmospherePresenter
from skeletons.gui.shared import IItemsCache
from skeletons.new_year import INewYearController

class HOMainWidget(ViewComponent[HoMainWidgetModel]):
    __nyController = dependency.descriptor(INewYearController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(HOMainWidget, self).__init__(model=HoMainWidgetModel)
        self.__widgetHelper = None
        return

    @property
    def viewModel(self):
        return super(HOMainWidget, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if self.__widgetHelper:
            content = self.__widgetHelper.createToolTipContent(event, contentID)
            if content:
                return content
        return super(HOMainWidget, self).createToolTipContent(event, contentID)

    def _getEvents(self):
        return (
         (
          self.__nyController.onDataUpdated, self.__onDataUpdated),
         (
          self.viewModel.onGoToGladeView, self.__onGoToGladeView),
         (
          self.viewModel.onEditName, self.__onEditName),
         (
          self.__nyController.onStateChanged, self.__onHoStateUpdated),
         (
          self.__nyController.onStateInitialized, self.__onHoStateUpdated))

    def _finalize(self):
        self.__widgetHelper.clear()
        self.__widgetHelper = None
        super(HOMainWidget, self)._finalize()
        return

    def _onLoading(self, *args, **kwargs):
        self.__widgetHelper = WidgetLevelProgressHelper(self.viewModel.widgetLevelProgress)
        NewYearSoundsManager.setRTPC(NewYearSoundVars.RTPC_LEVEL_ATMOSPHERE, NewYearAtmospherePresenter.getReachedLevel())
        super(HOMainWidget, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            self.__updateRerollToken(model)
            self.__onHoStateUpdated(model)
        self.__widgetHelper.initialize()

    def __updateRerollToken(self, model=None):
        if model is None:
            model = self.viewModel
        generalConfig = getNYGeneralConfig()
        rerollToken = generalConfig.getHangarNameRerollToken()
        hasToken = self.__itemsCache.items.tokens.getTokenCount(rerollToken) > 0
        model.setHasEditButton(hasToken)
        return

    def __onGoToGladeView(self, *_):
        GladeFirState.goTo(instantly=False)

    def __onDataUpdated(self, keys, _):
        self.__updateRerollToken()

    def __onHoStateUpdated(self, model=None):
        if model is None:
            model = self.viewModel
        model.setIsEnabled(self.__nyController.isEnabled())
        return

    @staticmethod
    def __onEditName():
        showNYHangarNameSelectionWindow(TypeView.CHANGE)