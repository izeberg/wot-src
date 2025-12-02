import typing, Event
from account_helpers import AccountSettings
from account_helpers.AccountSettings import NY_CELEBRITY_DAY_QUESTS_VISITED_MASK, NY_GIFT_MACHINE_BUY_TOKEN_VISITED, NY_DOG_PAGE_VISITED, NY_NARKET_PLACE_PAGE_VISITED, NY_CAT_PAGE_VISITED, NY_CELEBRITY_ADV_QUESTS_VISITED_MASK
from frameworks.state_machine import BaseStateObserver
from frameworks.wulf.view.array import fillStringsArray
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_trigger_hint_tabs_model import MenuTriggerHints
from gui.impl.gen.view_models.views.lobby.new_year.views.ny_main_menu_model import NyMainMenuModel
from gui.impl.lobby.new_year.states import HolidayOpsState, getMainMenuName
from gui.impl.lobby.new_year.tooltips.ny_menu_gift_tooltip import NyMenuGiftTooltip
from gui.impl.lobby.new_year.ho_main_widget_helpers import WidgetLevelProgressHelper, WidgetFriendStatusHelper
from gui.impl.new_year.navigation import NewYearNavigation
from gui.impl.new_year.sounds import NewYearSoundConfigKeys, NewYearSoundEvents, NewYearSoundStates, NewYearSoundsManager, NewYearSoundVars
from gui.impl.new_year.views.tabs_controller import NewYearMainTabsController
from gui.impl.pub.view_component import ViewComponent
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import HOLevelUpAnimation
from helpers import dependency
from items.components.ny_constants import CelebrityQuestTokenParts
from new_year.ny_constants import NyWidgetTopMenu
from new_year.ny_level_helper import NewYearAtmospherePresenter
from new_year.ny_trigger_hints import TriggerHintsStates
from skeletons.gui.impl import IGuiLoader
from skeletons.new_year import ICelebritySceneController, IFriendServiceController, IGiftMachineController, INewYearTriggerHintsController, INewYearController
if typing.TYPE_CHECKING:
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
_SOUNDS_MAP = {NewYearSoundConfigKeys.ENTRANCE_EVENT: {NyWidgetTopMenu.GLADE: NewYearSoundEvents.GLADE, 
                                           NyWidgetTopMenu.REWARDS: NewYearSoundEvents.REWARDS_LEVELS, 
                                           NyWidgetTopMenu.GIFT_MACHINE: NewYearSoundEvents.TOYS, 
                                           NyWidgetTopMenu.CHALLENGE: NewYearSoundEvents.CELEBRITY, 
                                           NyWidgetTopMenu.FRIENDS: NewYearSoundEvents.FRIENDS}, 
   NewYearSoundConfigKeys.EXIT_EVENT: {NyWidgetTopMenu.GLADE: NewYearSoundEvents.GLADE_EXIT, 
                                       NyWidgetTopMenu.MARKETPLACE: NewYearSoundEvents.MARKETPLACE_EXIT, 
                                       NyWidgetTopMenu.REWARDS: NewYearSoundEvents.REWARDS_LEVELS_EXIT, 
                                       NyWidgetTopMenu.GIFT_MACHINE: NewYearSoundEvents.TOYS_EXIT, 
                                       NyWidgetTopMenu.CHALLENGE: NewYearSoundEvents.CELEBRITY_EXIT, 
                                       NyWidgetTopMenu.FRIENDS: NewYearSoundEvents.FRIENDS_EXIT}, 
   NewYearSoundConfigKeys.STATE_VALUE: {NyWidgetTopMenu.MARKETPLACE: NewYearSoundStates.MARKETPLACE, 
                                        NyWidgetTopMenu.GIFT_MACHINE: NewYearSoundStates.TOYS, 
                                        NyWidgetTopMenu.FRIENDS: NewYearSoundStates.FRIENDS, 
                                        NyWidgetTopMenu.CHALLENGE: NewYearSoundStates.CELEBRITY, 
                                        NyWidgetTopMenu.REWARDS: NewYearSoundStates.REWARDS_LEVELS}}
_TRIGGER_HINT_TYPES = {TriggerHintsStates.DECORATION_ZONES: MenuTriggerHints.DECORATIONZONES, 
   TriggerHintsStates.GUESTA: MenuTriggerHints.GUESTA, 
   TriggerHintsStates.TOURNAMENT: MenuTriggerHints.TOURNAMENT}

class _MainViewStateObserver(BaseStateObserver):

    def __init__(self):
        super(_MainViewStateObserver, self).__init__()
        self.onMenuSwitched = Event.Event()

    def clear(self):
        super(_MainViewStateObserver, self).clear()
        self.onMenuSwitched.clear()

    def isObservingState(self, state):
        lsm = state.getMachine()
        return state.getParent() == lsm.getStateByCls(HolidayOpsState)

    def onEnterState(self, state, event):
        menuName = getMainMenuName(state.getStateID())
        self.onMenuSwitched(menuName)


class NYMainMenu(ViewComponent):
    __celebrityController = dependency.descriptor(ICelebritySceneController)
    __friendsService = dependency.descriptor(IFriendServiceController)
    __guiLoader = dependency.descriptor(IGuiLoader)
    __nyGiftMachineCtrl = dependency.descriptor(IGiftMachineController)
    __triggerHintsController = dependency.descriptor(INewYearTriggerHintsController)
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self, *args, **kwargs):
        super(NYMainMenu, self).__init__(model=NyMainMenuModel, *args, **kwargs)
        self.__tabsController = NewYearMainTabsController()
        self.__mainViewObserver = _MainViewStateObserver()
        self.__soundsManager = None
        self.__currentView = None
        self.__widgetHelper = None
        self.__widgetFriendHelper = None
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.mono.holiday_ops.tooltips.ho_menu_gift_tooltip():
            return NyMenuGiftTooltip()
        if self.__widgetHelper:
            content = self.__widgetHelper.createToolTipContent(event, contentID)
            if content:
                return content
        return super(NYMainMenu, self).createToolTipContent(event, contentID)

    def _onLoading(self, *args, **kwargs):
        super(NYMainMenu, self)._onLoading(*args, **kwargs)
        lsm = getLobbyStateMachine()
        lsm.connect(self.__mainViewObserver)

    def _onLoaded(self, *args, **kwargs):
        super(NYMainMenu, self)._onLoaded(*args, **kwargs)
        self.__widgetHelper.onLevelChanged += self.__onLevelChanged

    def _initialize(self, *args, **kwargs):
        super(NYMainMenu, self)._initialize(*args, **kwargs)
        self.__widgetHelper = WidgetLevelProgressHelper(self.viewModel.widgetLevelProgress)
        self.__widgetHelper.initialize()
        self.__widgetFriendHelper = WidgetFriendStatusHelper(self.viewModel.widgetFriendStatus)
        self.__widgetFriendHelper.initialize()
        soundConfig = {NewYearSoundConfigKeys.ENTRANCE_EVENT: self.__getEntranceSoundEvent, 
           NewYearSoundConfigKeys.EXIT_EVENT: self.__getExitSoundEvent, 
           NewYearSoundConfigKeys.STATE_VALUE: self.__getSoundStateValue}
        self.__soundsManager = NewYearSoundsManager(soundConfig)

    def _finalize(self):
        self.__widgetHelper.onLevelChanged -= self.__onLevelChanged
        self.__soundsManager.onExitView()
        self.__soundsManager.clear()
        self.__soundsManager = None
        self.__widgetHelper.clear()
        self.__widgetHelper = None
        self.__widgetFriendHelper.clear()
        self.__widgetFriendHelper = None
        self.__currentView = None
        super(NYMainMenu, self)._finalize()
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__mainViewObserver)
        self.__mainViewObserver.clear()
        self.__mainViewObserver = None
        return

    def _getEvents(self):
        return (
         (
          self.__mainViewObserver.onMenuSwitched, self.__onMenuItemSelected),
         (
          self.viewModel.onGoToFriendsList, self.__onGoToFriendsView),
         (
          self.__nyController.onDataUpdated, self.__onDataUpdated),
         (
          self.__nyController.sacksHelper.onUpdated, self.__onDataUpdated),
         (
          self.__nyController.currencies.onNyCoinsUpdate, self.__onNyCoinsUpdate),
         (
          self.__celebrityController.onQuestsUpdated, self.__onDataUpdated),
         (
          self.__friendsService.onFriendServiceStateChanged, self.__onDataUpdated),
         (
          AccountSettings.onSettingsChanging, self.__onAccountDataUpdated),
         (
          self.__triggerHintsController.onStateChanged, self.__onTriggerHintsStateChanged),
         (
          self.__nyController.onWidgetLevelUpAnimationEnd, self.__setAnimationEnd))

    def _getCallbacks(self):
        return (
         (
          'tokens', self.__onTokensChanged),)

    def _getListeners(self):
        return (
         (
          HOLevelUpAnimation.CHANGED_VIEW, self.__updateChangedView, EVENT_BUS_SCOPE.LOBBY),
         (
          HOLevelUpAnimation.START, self.__startLevelUp, EVENT_BUS_SCOPE.LOBBY))

    def __onMenuItemSelected(self, menuName):
        if not self.__needHangarSwitch(menuName):
            with self.viewModel.transaction() as (tx):
                tx.setStartIndexMenu(self.__tabsController.tabOrderKey(menuName))
            if self.__currentView and self.__currentView != menuName:
                self.__soundsManager.playEvent(NewYearSoundEvents.TAB_BAR_CLICK)
        self.__onSwitchView(menuName)
        NewYearNavigation.setCurrentMenuName(menuName)

    def __onGoToFriendsView(self):
        leaveService = self.__currentView in NyWidgetTopMenu.ALL_FRIEND_HANGAR
        if leaveService:
            self.__friendsService.preLeaveFriendHangar()

    def __onSwitchView(self, menuName):
        if menuName != self.__currentView:
            if self.__currentView:
                self.__soundsManager.onExitView()
                wasInFriendHangar = self.__currentView in NyWidgetTopMenu.ALL_FRIEND_HANGAR
                toFriendHangar = menuName in NyWidgetTopMenu.ALL_FRIEND_HANGAR
                if wasInFriendHangar and not toFriendHangar or not wasInFriendHangar and not toFriendHangar and self.__friendsService.isInFriendHangar:
                    self.__friendsService.leaveFriendHangar()
            self.__currentView = menuName
            self.__soundsManager.onEnterView()
        isHangarSwitch = self.__needHangarSwitch(menuName)
        if isHangarSwitch:
            isFriendHangar = not self.__tabsController.getIsFriendHangar()
            self.__tabsController.updateIsFriendHangar(isFriendHangar)
            self.__recreateMenu()
        elif self.__tabsController.getCurrentTabName() != menuName:
            self.__tabsController.selectTab(menuName)
        self.__updateMenu()

    def __needHangarSwitch(self, menuName):
        if self.__tabsController.getIsFriendHangar():
            return menuName in NyWidgetTopMenu.ALL_PLAYER_HANGAR
        return menuName in NyWidgetTopMenu.ALL_FRIEND_HANGAR

    def __onDataUpdated(self, *_):
        self.__updateMenu()

    def __onNyCoinsUpdate(self):
        self.__tryToDestroyTooltip((R.views.mono.holiday_ops.tooltips.ho_menu_gift_tooltip(),))
        self.__updateMenu()

    def __onAccountDataUpdated(self, key, _):
        if key in (
         NY_CELEBRITY_DAY_QUESTS_VISITED_MASK,
         NY_CELEBRITY_ADV_QUESTS_VISITED_MASK,
         NY_GIFT_MACHINE_BUY_TOKEN_VISITED,
         NY_DOG_PAGE_VISITED,
         NY_NARKET_PLACE_PAGE_VISITED,
         NY_CAT_PAGE_VISITED):
            self.__updateMenu()

    def __onTokensChanged(self, tokens):
        if any(token.startswith(CelebrityQuestTokenParts.PREFIX) for token in tokens):
            self.__updateMenu()

    def __onTriggerHintsStateChanged(self):
        self.__updateMenu()

    def __recreateMenu(self):
        with self.viewModel.transaction() as (model):
            tabIdx = self.__getTabIdx()
            model.setStartIndexMenu(tabIdx)
            self.__tabsController.setSelectedTabIdx(tabIdx)
            self.__tabsController.createTabModels(model.getItemsMenu())

    def __updateMenu(self):
        tabIdx = self.__getTabIdx()
        if not self.__currentView:
            return
        else:
            with self.viewModel.transaction() as (model):
                self.__tabsController.updateTabModels(model.getItemsMenu())
                model.setCurrentView(self.__currentView)
                model.setStartIndexMenu(tabIdx)
                activeTriggerHintTabs = self.__triggerHintsController.getActiveMenuTabs(self.__currentView)
                if activeTriggerHintTabs is not None:
                    triggerHintsState = self.__triggerHintsController.triggerHintsState
                    triggerHintTabs = model.triggerHintTabs
                    triggerHintTabs.setTriggerHintType(_TRIGGER_HINT_TYPES.get(triggerHintsState, MenuTriggerHints.NONE))
                    triggerHintTabsArray = model.triggerHintTabs.getActiveTabs()
                    fillStringsArray(activeTriggerHintTabs, triggerHintTabsArray)
            return

    def __updateChangedView(self, event):
        with self.viewModel.transaction() as (model):
            model.setHasChangedViewAnimation(event.ctx['hasChanged'])

    def __startLevelUp(self, _):
        with self.viewModel.transaction() as (model):
            model.setIsAnimationLevelUp(True)

    def __setAnimationEnd(self):
        with self.viewModel.transaction() as (model):
            model.setIsAnimationLevelUp(False)

    def __getEntranceSoundEvent(self):
        return _SOUNDS_MAP.get(NewYearSoundConfigKeys.ENTRANCE_EVENT, {}).get(self.__currentView)

    def __getExitSoundEvent(self):
        return _SOUNDS_MAP.get(NewYearSoundConfigKeys.EXIT_EVENT, {}).get(self.__currentView)

    def __getSoundStateValue(self):
        if self.__friendsService.isInFriendHangar:
            return None
        else:
            return _SOUNDS_MAP.get(NewYearSoundConfigKeys.STATE_VALUE, {}).get(self.__currentView)

    def __getTabIdx(self):
        currentView = self.__currentView
        if currentView not in self.__tabsController.tabs:
            return 0
        return self.__tabsController.tabOrderKey(currentView)

    def __tryToDestroyTooltip(self, tooltipIDs):
        for tooltipID in tooltipIDs:
            tooltipView = self.__guiLoader.windowsManager.getViewByLayoutID(tooltipID)
            if tooltipView:
                tooltipView.destroyWindow()

    def __onLevelChanged(self):
        NewYearSoundsManager.setRTPC(NewYearSoundVars.RTPC_LEVEL_ATMOSPHERE, NewYearAtmospherePresenter.getReachedLevel())