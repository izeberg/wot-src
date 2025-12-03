import typing
from constants import CURRENT_REALM
from frameworks.wulf import WindowFlags
from grinch.skeletons.battle_controller import IGrinchController
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.info_view_model import InfoViewModel
from grinch_progression.gui.impl.lobby.grinch_progression_helpers import showInfoVideo
from grinch_progression.gui.shared.event_dispatcher import showAboutGameBoard, showGameBoardView
from gui.impl.gen import R
from gui.impl.lobby.common.view_mixins import LobbyHeaderVisibility
from gui.impl.pub import WindowImpl
from gui.impl.pub.view_component import ViewComponent
from gui.shared import g_eventBus, events
from gui.shared.event_dispatcher import showHangar as showDefaultHangar
from helpers import getLanguageCode, dependency
if typing.TYPE_CHECKING:
    from grinch.gui.game_control.grinch_controller import GrinchController

class GameBoardInfoWindow(WindowImpl):

    def __init__(self, layer, **kwargs):
        super(GameBoardInfoWindow, self).__init__(content=InfoView(), wndFlags=WindowFlags.WINDOW, layer=layer)


class InfoView(ViewComponent, LobbyHeaderVisibility):
    LAYOUT_ID = R.views.grinch_progression.mono.lobby.info_view()
    _grinchCtrl = dependency.descriptor(IGrinchController)

    def __init__(self, *args, **kwargs):
        super(InfoView, self).__init__(self.LAYOUT_ID, InfoViewModel, *args, **kwargs)

    @property
    def viewModel(self):
        return super(InfoView, self).getViewModel()

    def _getEvents(self):
        return super(InfoView, self)._getEvents() + (
         (
          self.viewModel.onViewLoaded, self.__onViewLoaded),
         (
          self.viewModel.onVideoClick, self.__onPlayVideo),
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onShowAboutEvent, self.__onShowAboutEvent),
         (
          self._grinchCtrl.onConfigChanged, self.__onConfigChanged))

    def _onLoaded(self, *args, **kwargs):
        super(InfoView, self)._onLoaded(*args, **kwargs)
        self.suspendLobbyHeader(self.uniqueID)
        self.__update()

    def _finalize(self):
        super(InfoView, self)._finalize()
        self.resumeLobbyHeader(self.uniqueID)

    def __onClose(self):
        if self._grinchCtrl.isEventPrbActive():
            showGameBoardView()
        else:
            self._grinchCtrl.selectMode()

    def __update(self):
        with self.viewModel.transaction() as (model):
            model.setEventStartDate(self._grinchCtrl.getStartDate())
            model.setEventEndDate(self._grinchCtrl.getAllSeasonsEndDate())
            model.region.setRealm(CURRENT_REALM)
            model.region.setLanguage(getLanguageCode())

    @staticmethod
    def __onPlayVideo():
        showInfoVideo()

    @staticmethod
    def __onShowAboutEvent():
        showAboutGameBoard()

    def __onViewLoaded(self):
        g_eventBus.handleEvent(events.ViewReadyEvent(self.layoutID))

    def __onConfigChanged(self, _):
        if not self._grinchCtrl.isEnabled() and not self._grinchCtrl.isEventPrbActive():
            showDefaultHangar()