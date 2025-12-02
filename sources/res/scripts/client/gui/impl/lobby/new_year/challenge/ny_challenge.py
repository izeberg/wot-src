import logging
from collections import namedtuple
import typing
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.lobby.new_year.challenge.ho_challenge_guest import HOChallengeGuest
from gui.impl.lobby.new_year.challenge.ho_challenge_guest_d_customization import HOChallengeGuestDCustomization
from gui.impl.lobby.new_year.challenge.ho_challenge_headquarters import HOChallengeHeadquarters
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.new_year_challenge_model import NewYearChallengeModel, ChallengeViewStates
from gui.impl.lobby.new_year.challenge.ho_challenge_tournament import HOChallengeTournament
from gui.impl.lobby.new_year.challenge.ho_challenge_tournament_completed import HOChallengeTournamentCompleted
from gui.impl.lobby.new_year.ho_selectable_logic_presenter import HOSelectableLogicPresenter
from gui.impl.lobby.new_year.ho_sidebar_component import ViewWithSidebarStateObserver
from gui.impl.lobby.new_year.scene_rotatable_view import SceneRotatableView
from gui.impl.lobby.new_year.states import ChallengeState
from gui.impl.new_year.new_year_helper import nyCreateToolTipContentDecorator
from helpers import dependency
from new_year.ny_constants import NyWidgetTopMenu, NyTabBarChallengeView as TabBarNames
from skeletons.new_year import ICelebritySceneController
if typing.TYPE_CHECKING:
    from typing import Dict, Optional, List
    from frameworks.wulf.view.submodel_presenter import SubModelPresenter
_logger = logging.getLogger(__name__)
_SubViewInfo = namedtuple('_SubViewInfo', ('viewCls', 'uiID'))
_VIEW_INFO_BY_ID = {TabBarNames.TOURNAMENT: _SubViewInfo(HOChallengeTournament, ChallengeViewStates.TOURNAMENT), 
   TabBarNames.TOURNAMENT_COMPLETED: _SubViewInfo(HOChallengeTournamentCompleted, ChallengeViewStates.COMPLETED), 
   TabBarNames.GUEST_A: _SubViewInfo(HOChallengeGuest, ChallengeViewStates.GUESTA), 
   TabBarNames.GUEST_CAT: _SubViewInfo(HOChallengeGuest, ChallengeViewStates.GUESTC), 
   TabBarNames.HEADQUARTERS: _SubViewInfo(HOChallengeHeadquarters, ChallengeViewStates.HEADQUARTERS), 
   TabBarNames.GUEST_D: _SubViewInfo(HOChallengeGuestDCustomization, ChallengeViewStates.GUESTD)}

class NewYearChallenge(SceneRotatableView, HOSelectableLogicPresenter):
    __celebrityController = dependency.descriptor(ICelebritySceneController)

    def __init__(self, viewModel, parentView, *args, **kwargs):
        super(NewYearChallenge, self).__init__(viewModel, parentView, *args, **kwargs)
        self.__subViews = {}
        self.__currentSubViewID = None
        self.__switchingSubViewID = None
        self.__stateObserver = None
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def createPopOverContent(self, event):
        view = self.__getCurrentSubView()
        if view:
            return view.createPopOverContent(event)
        return super(NewYearChallenge, self).createPopOverContent(event)

    @nyCreateToolTipContentDecorator
    def createToolTipContent(self, event, contentID):
        view = self.__getCurrentSubView()
        if view:
            return view.createToolTipContent(event, contentID)
        return super(NewYearChallenge, self).createToolTipContent(event, contentID)

    def createToolTip(self, event):
        view = self.__getCurrentSubView()
        if view:
            return view.createToolTip(event)
        return super(NewYearChallenge, self).createToolTip(event)

    def initialize(self, *args, **kwargs):
        self.__stateObserver = ViewWithSidebarStateObserver(ChallengeState)
        super(NewYearChallenge, self).initialize(*args, **kwargs)
        lsm = getLobbyStateMachine()
        lsm.connect(self.__stateObserver)
        viewInfo = _VIEW_INFO_BY_ID.get(TabBarNames.TOURNAMENT)
        self.viewModel.setViewState(viewInfo.uiID)

    def finalize(self):
        super(NewYearChallenge, self).finalize()
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__stateObserver)
        self.__stateObserver.clear()
        self.__stateObserver = None
        view = self.__getCurrentSubView()
        if view:
            view.finalize()
        self.__currentSubViewID = None
        return

    def clear(self):
        for view in self.__subViews.itervalues():
            view.clear()

        self.__subViews.clear()
        self.__subViews = None
        super(NewYearChallenge, self).clear()
        return

    def _getCallbacks(self):
        return tuple()

    def _getEvents(self):
        events = super(NewYearChallenge, self)._getEvents()
        return events + (
         (
          self.__stateObserver.onSidebarSelected, self.__onSideBarSelected),
         (
          self.__celebrityController.onQuestsUpdated, self.__onQuestsUpdated),
         (
          self.viewModel.onUpdateContentModel, self.__onUpdateContent))

    def __onSideBarSelected(self, tabName, menuName):
        if menuName != NyWidgetTopMenu.CHALLENGE:
            return
        self.__switchingSubViewID = tabName
        self.viewModel.setIsTabSwitching(True)

    def __onUpdateContent(self):
        if self.__switchingSubViewID is not None:
            self.__switchSubView(self.__switchingSubViewID)
        self.__switchingSubViewID = None
        self.viewModel.setIsTabSwitching(False)
        return

    def __switchSubView(self, tabName, *args, **kwargs):
        if tabName == TabBarNames.TOURNAMENT and self.__celebrityController.isChallengeCompleted:
            tabName = TabBarNames.TOURNAMENT_COMPLETED
        if self.__currentSubViewID == tabName:
            return
        else:
            newView = self.__getSubView(tabName)
            if newView is None:
                return
            view = self.__getCurrentSubView()
            if view:
                view.finalize()
            self.__initializeSubView(newView, tabName, *args, **kwargs)
            self.__currentSubViewID = tabName
            viewInfo = _VIEW_INFO_BY_ID.get(tabName)
            self.viewModel.setViewState(viewInfo.uiID)
            self.isMoveSpaceEnable(tabName != TabBarNames.GUEST_D)
            return

    def __getCurrentSubView(self):
        if self.__currentSubViewID in self.__subViews:
            return self.__subViews.get(self.__currentSubViewID)
        else:
            return

    def __getSubView(self, tabName):
        if tabName in self.__subViews:
            return self.__subViews.get(tabName)
        return self.__createSubView(tabName)

    def __createSubView(self, tabName):
        viewInfo = _VIEW_INFO_BY_ID.get(tabName)
        if viewInfo:
            view = viewInfo.viewCls(self.viewModel, self.parentView)
            self.__subViews[tabName] = view
            return view
        else:
            return

    @staticmethod
    def __initializeSubView(subView, tabName, *args, **kwargs):
        kwargs.setdefault('ctx', {}).update({'tabName': tabName})
        subView.initialize(*args, **kwargs)

    def __onQuestsUpdated(self):
        if self.__currentSubViewID == TabBarNames.TOURNAMENT and self.__celebrityController.isChallengeCompleted:
            self.__switchSubView(TabBarNames.TOURNAMENT_COMPLETED)