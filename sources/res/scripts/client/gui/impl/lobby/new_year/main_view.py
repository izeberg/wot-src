import weakref
from functools import partial
import typing, BigWorld
from future.utils import iteritems
from frameworks.wulf import ViewSettings, WindowFlags
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.ny_glade_view_model import AnimationLevelUpStates
from gui.impl.gen.view_models.views.lobby.new_year.views.main_view_model import MainViewModel, MainViews
from gui.impl.lobby.new_year.observers import HolidayOpsObserver
from gui.impl.lobby.new_year.states import GladeTownState
from gui.impl.lobby.new_year.ny_menu_component import NYMainMenu
from gui.impl.lobby.new_year.ho_sidebar_component import HOSidebar
from gui.impl.lobby.hangar.presenters.lootbox_entry_point_presenter import LootboxEntryPointPresenter
from gui.impl.new_year.navigation import NewYearNavigation
from gui.impl.new_year.sounds import NY_MAIN_VIEW_SOUND_SPACE, NewYearSoundsManager, NewYearSoundEvents
from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus
from gui.shared.event_dispatcher import showHangar
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from helpers import dependency, uniprof
from new_year.ny_constants import NyWidgetTopMenu
from shared_utils import nextTick
from gui.shared.events import NyGladeVisibilityEvent, LobbySimpleEvent
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.new_year import INewYearController, IFriendServiceController
from gui.lobby_state_machine.routable_view import IRoutableView
from gui.impl.pub.view_component import ViewComponent
from gui.impl.pub import WindowImpl
if typing.TYPE_CHECKING:
    from typing import Dict
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
_SubModelInfo = typing.NamedTuple('_SubModelInfo', [
 (
  'ID', MainViews),
 (
  'presenter', SubModelPresenter),
 (
  'canBeLoaded', typing.Optional[typing.Callable[([], bool)]])])
_STAGE_ENABLED_TAB = (
 NyWidgetTopMenu.GLADE,
 NyWidgetTopMenu.CHALLENGE,
 NyWidgetTopMenu.FRIEND_GLADE,
 NyWidgetTopMenu.FRIEND_CHALLENGE,
 NyWidgetTopMenu.MARKETPLACE,
 NyWidgetTopMenu.GIFT_MACHINE)

class MainViewWindow(WindowImpl):

    def __init__(self, layer, *args, **kwargs):
        super(MainViewWindow, self).__init__(content=MainView(*args, **kwargs), wndFlags=WindowFlags.WINDOW, layer=layer)


class MainView(ViewComponent, IRoutableView):
    _COMMON_SOUND_SPACE = NY_MAIN_VIEW_SOUND_SPACE
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __nyController = dependency.descriptor(INewYearController)
    __friendsService = dependency.descriptor(IFriendServiceController)
    __appLoader = dependency.descriptor(IAppLoader)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.holiday_ops.main())
        settings.args = args
        settings.kwargs = kwargs
        settings.model = MainViewModel()
        self.__contentPresentersMap = {}
        self.__appLoader.getApp().setBackgroundAlpha(0.0)
        self.__regionName = None
        self.__lsmObserver = HolidayOpsObserver()
        self.__menuName = None
        super(MainView, self).__init__(R.views.mono.holiday_ops.main(), MainViewModel)
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def getRouterModel(self):
        return self.getViewModel().router

    @property
    def currentPresenter(self):
        return self.__contentPresentersMap[self.__menuName].presenter

    def _initChildren(self):
        holidayOps = R.aliases.holiday_ops.default
        self._registerChild(holidayOps.Sidebar(), HOSidebar())
        self._registerChild(holidayOps.MainMenu(), NYMainMenu())
        self._registerChild(R.aliases.hangar.shared.LootboxEntryPoint(), LootboxEntryPointPresenter())

    def createToolTipContent(self, event, contentID):
        return self.currentPresenter.createToolTipContent(event, contentID) or super(MainView, self).createToolTipContent(event, contentID)

    def createToolTip(self, event):
        for _, child in iteritems(self._childrenByUid):
            content = child.createToolTip(event)
            if content is not None:
                return content

        return self.currentPresenter.createToolTip(event) or super(MainView, self).createToolTip(event)

    def createPopOverContent(self, event):
        return self.currentPresenter.createPopOverContent(event) or super(MainView, self).createPopOverContent(event)

    def _initialize(self, *args, **kwargs):
        g_eventBus.handleEvent(events.LobbyHeaderEvent(events.LobbyHeaderEvent.TOGGLE_VISIBILITY, ctx={'visible': False}), EVENT_BUS_SCOPE.LOBBY)
        self.viewModel.gladeModel.setAnimationLevelUpState(AnimationLevelUpStates.IDLE)
        NewYearSoundsManager.playEvent(NewYearSoundEvents.ENTER_CUSTOM)
        NewYearNavigation.closeMainViewInProcess(False)

    def _getEvents(self):
        return super(MainView, self)._getEvents() + (
         (
          self.viewModel.onClose, self.__onCloseClick),
         (
          self.viewModel.onStartClose, self.__onStartClose),
         (
          self.viewModel.onGlobalFadeIn, self.__onGlobalFadeIn),
         (
          self.viewModel.onGlobalFadeOut, self.__onGlobalFadeOut),
         (
          self.__nyController.onStateChanged, self.__onStateChanged),
         (
          self.__friendsService.onFriendServiceStateChanged, self.__onChangeFriendService),
         (
          self.__lsmObserver.onNavigationChanged, self.__switchSubView),
         (
          self.__lsmObserver.onExitView, self.__exitSubView))

    def _getListeners(self):
        return super(MainView, self)._getListeners() + (
         (
          NyGladeVisibilityEvent.START_FADE_IN, self.__handleStartFadeIn, EVENT_BUS_SCOPE.DEFAULT),
         (
          NyGladeVisibilityEvent.START_FADE_OUT, self.__handleStartFadeOut, EVENT_BUS_SCOPE.DEFAULT),
         (
          LobbySimpleEvent.WAITING_SHOWN, self.__showWaiting, EVENT_BUS_SCOPE.LOBBY),
         (
          LobbySimpleEvent.WAITING_HIDDEN, self.__hideWaiting, EVENT_BUS_SCOPE.LOBBY))

    def _onLoading(self, *args, **kwargs):
        super(MainView, self)._onLoading(args, kwargs)
        self.__registerSubModels()
        lsm = getLobbyStateMachine()
        lsm.connect(self.__lsmObserver)

    def _onLoaded(self, *args, **kwargs):
        nextTick(partial(self.__onStateChanged))()

    def _finalize(self):
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__lsmObserver)
        if dependency.instance(IHangarSpace).spaceInited:
            BigWorld.worldDrawEnabled(True)
        if self.currentPresenter.isLoaded:
            self.currentPresenter.finalize()
        if self.__regionName:
            uniprof.exitFromRegion(self.__regionName)
            self.__regionName = None
        for subModelInfo in self.__contentPresentersMap.itervalues():
            subModelInfo.presenter.clear()

        self.__contentPresentersMap.clear()
        self.__contentPresentersMap = None
        NewYearNavigation.clear()
        g_eventBus.handleEvent(events.LobbyHeaderEvent(events.LobbyHeaderEvent.TOGGLE_VISIBILITY, ctx={'visible': True}), EVENT_BUS_SCOPE.LOBBY)
        super(MainView, self)._finalize()
        return

    def __updateWaitingStatus(self, isWaitingShown):
        if self.viewModel is None:
            return
        else:
            self.viewModel.setIsWaitingShown(isWaitingShown)
            return

    def __showWaiting(self, _):
        self.__updateWaitingStatus(True)

    def __hideWaiting(self, _):
        self.__updateWaitingStatus(False)

    def __registerSubModels(self):
        self.__contentPresentersMap = _PresentersMap(self)

    def __switchSubView(self, menuName):
        if self.__menuName == menuName:
            return
        if self.__regionName:
            uniprof.exitFromRegion(self.__regionName)
        self.__regionName = menuName
        uniprof.enterToRegion(self.__regionName)
        if dependency.instance(IHangarSpace).spaceInited:
            BigWorld.worldDrawEnabled(menuName in _STAGE_ENABLED_TAB)
        subModelInfo = self.__contentPresentersMap[menuName]
        with self.viewModel.transaction() as (tx):
            if subModelInfo:
                subModelInfo.presenter.initialize()
                tx.setViewType(subModelInfo.ID)
        self.__menuName = menuName

    def __exitSubView(self, exitMenuName):
        subModelInfo = self.__contentPresentersMap[exitMenuName]
        if subModelInfo and subModelInfo.presenter.isLoaded:
            subModelInfo.presenter.finalize()

    def __onStateChanged(self):
        if not self.__nyController.isEnabled():
            self.__onClose()

    def __onChangeFriendService(self):
        if self.__friendsService.isServiceEnabled is False and self.__friendsService.isInFriendHangar:
            self.__friendsService.leaveFriendHangar()
            GladeTownState.goTo(instantly=True)

    @staticmethod
    def __onClose():
        showHangar()

    def __onCloseClick(self, args):
        self.__onClose()

    @staticmethod
    def __onStartClose():
        NewYearNavigation.closeMainViewInProcess(True)

    def __handleStartFadeIn(self, *_):
        with self.viewModel.transaction() as (model):
            model.setIsGlobalFaded(True)

    def __handleStartFadeOut(self, _):
        with self.viewModel.transaction() as (model):
            model.setIsGlobalFaded(False)

    @staticmethod
    def __onGlobalFadeIn():
        g_eventBus.handleEvent(NyGladeVisibilityEvent(eventType=NyGladeVisibilityEvent.END_FADE_IN), scope=EVENT_BUS_SCOPE.DEFAULT)

    @staticmethod
    def __onGlobalFadeOut():
        g_eventBus.handleEvent(NyGladeVisibilityEvent(eventType=NyGladeVisibilityEvent.END_FADE_OUT), scope=EVENT_BUS_SCOPE.DEFAULT)


class _PresentersMap(object):

    def __init__(self, mainView):
        self.__presentersCache = {}
        self.__mainView = weakref.proxy(mainView)
        self.__loadersMap = self.__makeLoadersMap()

    def itervalues(self):
        return self.__presentersCache.itervalues()

    def clear(self):
        self.__loadersMap = {}
        self.__presentersCache = {}
        self.__mainView = None
        return

    def __getitem__(self, item):
        if item not in self.__presentersCache:
            self.__tryToLoadPresenter(item)
        return self.__presentersCache.get(item, None)

    def __tryToLoadPresenter(self, key):
        if key in self.__loadersMap:
            self.__presentersCache[key] = self.__loadersMap[key]()

    def __makeLoadersMap(self):
        return {NyWidgetTopMenu.GLADE: partial(self.__makeSubModel, MainViews.GLADE, self.__loadGlade), 
           NyWidgetTopMenu.GIFT_MACHINE: partial(self.__makeSubModel, MainViews.GIFT_MACHINE, self.__loadGiftMachine), 
           NyWidgetTopMenu.REWARDS: partial(self.__makeSubModel, MainViews.REWARDS, self.__loadRewards), 
           NyWidgetTopMenu.MARKETPLACE: partial(self.__makeSubModel, MainViews.MARKETPLACE, self.__loadMarketplace), 
           NyWidgetTopMenu.CHALLENGE: partial(self.__makeSubModel, MainViews.CHALLENGE, self.__loadChallenge), 
           NyWidgetTopMenu.FRIENDS: partial(self.__makeSubModel, MainViews.FRIENDS, self.__loadFriends), 
           NyWidgetTopMenu.FRIEND_GLADE: partial(self.__makeSubModel, MainViews.FRIEND_GLADE, self.__loadFriendGlade), 
           NyWidgetTopMenu.FRIEND_CHALLENGE: partial(self.__makeSubModel, MainViews.FRIEND_CHALLENGE, self.__loadFriendChallenge)}

    def __loadGlade(self):
        from gui.impl.lobby.new_year.glade.ho_glade_view import HOGladeView
        return HOGladeView(self.__mainView.viewModel.gladeModel, self.__mainView)

    def __loadGiftMachine(self):
        from gui.impl.lobby.new_year.gift_machine.ho_gift_machine_view import HOGiftMachineView
        return HOGiftMachineView(self.__mainView.viewModel.giftMachineModel, self.__mainView)

    def __loadRewards(self):
        from gui.impl.lobby.new_year.rewards_info.ho_rewards_info_presenter import HORewardsInfoPresenter
        return HORewardsInfoPresenter(self.__mainView.viewModel.rewardsModel, self.__mainView)

    def __loadMarketplace(self):
        from gui.impl.lobby.new_year.marketplace.marketplace_view import MarketplaceView
        return MarketplaceView(self.__mainView.viewModel.marketplaceModel, self.__mainView)

    def __loadChallenge(self):
        from gui.impl.lobby.new_year.challenge.ny_challenge import NewYearChallenge
        return NewYearChallenge(self.__mainView.viewModel.challengeModel, self.__mainView)

    def __loadFriends(self):
        from gui.impl.lobby.new_year.friends.ho_friends_view import HOFriendsView
        return HOFriendsView(self.__mainView.viewModel.friendsModel, self.__mainView)

    def __loadFriendGlade(self):
        from gui.impl.lobby.new_year.friend_glade.ho_friend_glade_view import HOFriendGladeView
        return HOFriendGladeView(self.__mainView.viewModel.friendGladeModel, self.__mainView)

    def __loadFriendChallenge(self):
        from gui.impl.lobby.new_year.friend_challenge.ho_friend_challenge_view import HOFriendChallengeView
        return HOFriendChallengeView(self.__mainView.viewModel.friendChallengeModel, self.__mainView)

    @staticmethod
    def __makeSubModel(viewAlias, loader, customPredicate=None):
        return _SubModelInfo(viewAlias, loader(), customPredicate)