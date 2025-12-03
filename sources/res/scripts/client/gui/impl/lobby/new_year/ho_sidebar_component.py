import typing, Event
from frameworks.state_machine import BaseStateObserver, visitor
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.new_year.views.ny_sidebar_model import NySidebarModel
from gui.impl.lobby.new_year.states import HolidayOpsState, getLastPathSegment, getMainMenuName
from gui.impl.new_year.sounds import NewYearSoundConfigKeys, NewYearSoundEvents, NewYearSoundStates, NewYearSoundsManager
from gui.impl.new_year.views.tabs_controller import GladeTabsController, ChallengeTabsController, MarketplaceTabsController, FriendGladeTabsController
from gui.impl.pub.view_component import ViewComponent
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.scheduled_notifications import SimpleNotifier
from helpers import dependency, uniprof
from items.components.ny_constants import CustomizationObjects
from new_year.ny_constants import SyncDataKeys, NyWidgetTopMenu, NYObjects, Collections, CHALLENGE_TAB_TO_CAMERA_OBJ
from new_year.ny_resource_collecting_helper import getCollectingCooldownTime
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IWalletController
from skeletons.new_year import ICelebritySceneController, ICelebrityController, IFriendServiceController, INewYearTriggerHintsController, INewYearController
if typing.TYPE_CHECKING:
    from gui.impl.new_year.views.tabs_controller import NyTabsController
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
    from gui.lobby_state_machine.states import LobbyState
_GLADE_SOUNDS_MAP = {NewYearSoundConfigKeys.ENTRANCE_EVENT: {CustomizationObjects.FIR: NewYearSoundEvents.TREE, 
                                           CustomizationObjects.FAIR: NewYearSoundEvents.FAIR, 
                                           CustomizationObjects.INSTALLATION: NewYearSoundEvents.SNOWTANK, 
                                           NYObjects.RESOURCES: NewYearSoundEvents.RESOURCES, 
                                           NYObjects.TOWN: NewYearSoundEvents.UNDER_SPACE}, 
   NewYearSoundConfigKeys.EXIT_EVENT: {CustomizationObjects.FIR: NewYearSoundEvents.TREE_EXIT, 
                                       CustomizationObjects.FAIR: NewYearSoundEvents.FAIR_EXIT, 
                                       CustomizationObjects.INSTALLATION: NewYearSoundEvents.SNOWTANK_EXIT, 
                                       NYObjects.RESOURCES: NewYearSoundEvents.RESOURCES_EXIT, 
                                       NYObjects.TOWN: NewYearSoundEvents.UNDER_SPACE_EXIT}, 
   NewYearSoundConfigKeys.STATE_VALUE: {CustomizationObjects.FIR: NewYearSoundStates.TREE, 
                                        CustomizationObjects.FAIR: NewYearSoundStates.FAIR, 
                                        CustomizationObjects.INSTALLATION: NewYearSoundStates.SNOWTANK, 
                                        NYObjects.CELEBRITY: NewYearSoundStates.CELEBRITY, 
                                        NYObjects.RESOURCES: NewYearSoundStates.RESOURCES, 
                                        NYObjects.TOWN: NewYearSoundStates.UNDER_SPACE}}
_MARKETPLACE_SOUNDS_MAP = {NewYearSoundConfigKeys.ENTRANCE_EVENT: {Collections.Previous: NewYearSoundEvents.ALBUM_SELECT_2021, 
                                           Collections.NewYear21: NewYearSoundEvents.ALBUM_SELECT_2022, 
                                           Collections.NewYear22: NewYearSoundEvents.ALBUM_SELECT_2023, 
                                           Collections.NewYear23: NewYearSoundEvents.ALBUM_SELECT_2018, 
                                           Collections.NewYear24: NewYearSoundEvents.ALBUM_SELECT_2019, 
                                           Collections.NewYear25: NewYearSoundEvents.ALBUM_SELECT_2020}, 
   NewYearSoundConfigKeys.EXIT_EVENT: {Collections.Previous: NewYearSoundEvents.ALBUM_SELECT_2021_EXIT, 
                                       Collections.NewYear21: NewYearSoundEvents.ALBUM_SELECT_2022_EXIT, 
                                       Collections.NewYear22: NewYearSoundEvents.ALBUM_SELECT_2023_EXIT, 
                                       Collections.NewYear23: NewYearSoundEvents.ALBUM_SELECT_2018_EXIT, 
                                       Collections.NewYear24: NewYearSoundEvents.ALBUM_SELECT_2019_EXIT, 
                                       Collections.NewYear25: NewYearSoundEvents.ALBUM_SELECT_2020_EXIT}}
_GUESTS_SOUNDS_MAP = {NewYearSoundConfigKeys.ENTRANCE_EVENT: {NYObjects.CHALLENGE: NewYearSoundEvents.CHALLENGE, 
                                           NYObjects.CELEBRITY_A: NewYearSoundEvents.CELEBRITY_A, 
                                           NYObjects.CELEBRITY_CAT: NewYearSoundEvents.CELEBRITY_CAT, 
                                           NYObjects.CELEBRITY_D: NewYearSoundEvents.CELEBRITY_D, 
                                           NYObjects.CELEBRITY: NewYearSoundEvents.CELEBRITY_HQ}, 
   NewYearSoundConfigKeys.EXIT_EVENT: {NYObjects.CHALLENGE: NewYearSoundEvents.CHALLENGE_EXIT, 
                                       NYObjects.CELEBRITY_A: NewYearSoundEvents.CELEBRITY_A_EXIT, 
                                       NYObjects.CELEBRITY_CAT: NewYearSoundEvents.CELEBRITY_CAT_EXIT, 
                                       NYObjects.CELEBRITY_D: NewYearSoundEvents.CELEBRITY_D_EXIT, 
                                       NYObjects.CELEBRITY: NewYearSoundEvents.CELEBRITY_HQ_EXIT}, 
   NewYearSoundConfigKeys.STATE_GROUP: NewYearSoundStates.STATE_CELEBRITY, 
   NewYearSoundConfigKeys.STATE_VALUE: {NYObjects.CHALLENGE: NewYearSoundStates.CHALLENGE, 
                                        NYObjects.CELEBRITY_A: NewYearSoundStates.CELEBRITY_A, 
                                        NYObjects.CELEBRITY_CAT: NewYearSoundStates.CELEBRITY_CAT, 
                                        NYObjects.CELEBRITY_D: NewYearSoundStates.CELEBRITY_D, 
                                        NYObjects.CELEBRITY: NewYearSoundStates.CELEBRITY_HQ}}

class ViewWithSidebarStateObserver(BaseStateObserver):

    def __init__(self, viewStateCls):
        super(ViewWithSidebarStateObserver, self).__init__()
        self.onSidebarSelected = Event.Event()
        self.onExitView = Event.Event()
        self.__viewStateCls = viewStateCls

    def clear(self):
        super(ViewWithSidebarStateObserver, self).clear()
        self.onSidebarSelected.clear()
        self.onExitView.clear()

    def isObservingState(self, state):
        lsm = state.getMachine()
        return state.getParent() == lsm.getStateByCls(self.__viewStateCls)

    def onEnterState(self, state, _):
        tabName = getLastPathSegment(state.getStateID())
        menuName = getMainMenuName(state.getStateID())
        self.onSidebarSelected(tabName, menuName)

    def onExitState(self, state, _):
        self.onExitView()


class _SidebarStatesObserver(BaseStateObserver):

    def __init__(self):
        super(_SidebarStatesObserver, self).__init__()
        self.onSwitchView = Event.Event()
        self.onChangeTab = Event.Event()
        self.onExitTab = Event.Event()

    def clear(self):
        super(_SidebarStatesObserver, self).clear()
        self.onSwitchView.clear()
        self.onChangeTab.clear()
        self.onExitTab.clear()

    def isObservingState(self, state):
        lsm = state.getMachine()
        return visitor.isDescendantOf(state, lsm.getStateByCls(HolidayOpsState))

    def onEnterState(self, state, event):
        lsm = state.getMachine()
        tabName = getLastPathSegment(state.getStateID())
        menuName = getMainMenuName(state.getStateID())
        if state.getParent() == lsm.getStateByCls(HolidayOpsState):
            self.onSwitchView(menuName)
        else:
            self.onChangeTab(tabName)

    def onExitState(self, state, event):
        lsm = state.getMachine()
        if state.getParent() != lsm.getStateByCls(HolidayOpsState):
            self.onExitTab()


class HOSidebar(ViewComponent[NySidebarModel]):
    __nyController = dependency.descriptor(INewYearController)
    __celebrityController = dependency.descriptor(ICelebrityController)
    __celebritySceneController = dependency.descriptor(ICelebritySceneController)
    __settingsCore = dependency.descriptor(ISettingsCore)
    __triggerHintsController = dependency.descriptor(INewYearTriggerHintsController)
    __friendsService = dependency.descriptor(IFriendServiceController)
    __wallet = dependency.instance(IWalletController)

    def __init__(self, *args, **kwargs):
        super(HOSidebar, self).__init__(model=NySidebarModel)
        self.__tabsController = None
        self.__controllers = {}
        self.__currentTab = None
        self.__currentViewName = None
        self.__soundsManager = None
        self.__regionName = None
        self.__notifier = None
        self.__stateObserver = _SidebarStatesObserver()
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def _initialize(self, ctx=None, *args, **kwargs):
        super(HOSidebar, self)._initialize(*args, **kwargs)
        lsm = getLobbyStateMachine()
        lsm.connect(self.__stateObserver)
        self.__nyController.onDataUpdated += self.__onDataUpdated
        self.__celebritySceneController.onQuestsUpdated += self.__onQuestUpdated
        self.__settingsCore.onSettingsChanged += self.__onSettingsChanged
        self.__triggerHintsController.onStateChanged += self.__onTriggerHintsStateChanged
        self.__notifier = SimpleNotifier(getCollectingCooldownTime, self.__onResourcesUpdated)
        self.__celebrityController.onCelebCompletedTokensUpdated += self.__onCelebCompletedTokensUpdated
        g_clientUpdateManager.addCallbacks({'inventory': self.__onInventoryUpdate})
        soundConfig = {NewYearSoundConfigKeys.ENTRANCE_EVENT: self.__getEntranceSoundEvent, 
           NewYearSoundConfigKeys.EXIT_EVENT: self.__getExitSoundEvent, 
           NewYearSoundConfigKeys.STATE_VALUE: self.__getSoundStateValue, 
           NewYearSoundConfigKeys.STATE_GROUP: self.__getSoundStateGroup}
        self.__soundsManager = NewYearSoundsManager(soundConfig)
        self.__controllers = {NyWidgetTopMenu.GLADE: GladeTabsController(), 
           NyWidgetTopMenu.FRIEND_GLADE: FriendGladeTabsController(), 
           NyWidgetTopMenu.MARKETPLACE: MarketplaceTabsController(), 
           NyWidgetTopMenu.CHALLENGE: ChallengeTabsController()}
        if ctx is not None:
            self.__onSwitchView(ctx)
        return

    def _finalize(self):
        super(HOSidebar, self)._finalize()
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__stateObserver)
        self.__stateObserver.clear()
        self.__stateObserver = None
        self.__nyController.onDataUpdated -= self.__onDataUpdated
        self.__celebritySceneController.onQuestsUpdated -= self.__onQuestUpdated
        self.__celebrityController.onCelebCompletedTokensUpdated -= self.__onCelebCompletedTokensUpdated
        self.__settingsCore.onSettingsChanged -= self.__onSettingsChanged
        self.__triggerHintsController.onStateChanged -= self.__onTriggerHintsStateChanged
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__tabsController = None
        self.__controllers.clear()
        self.__soundsManager.clear()
        self.__soundsManager = None
        self.__currentViewName = None
        if self.__regionName:
            uniprof.exitFromRegion(self.__regionName)
            self.__regionName = None
        self.__notifier.stopNotification()
        self.__notifier.clear()
        self.__nyController.setLastViewedTab(isReset=True)
        return

    def _getEvents(self):
        events = super(HOSidebar, self)._getEvents()
        return events + (
         (
          self.__stateObserver.onSwitchView, self.__onSwitchView),
         (
          self.__stateObserver.onChangeTab, self.__onChangeTab),
         (
          self.__stateObserver.onExitTab, self.__onExitTab),
         (
          self.__nyController.sacksHelper.onUpdated, self.__onSacksUpdated),
         (
          self.__friendsService.onBestFriendsUpdated, self.__onFriendsUpdated),
         (
          self.__friendsService.onSwitchFriendCollectingState, self.__onFriendsUpdated),
         (
          self.__friendsService.onFriendHangarEnter, self.__onFriendsUpdated),
         (
          self.__wallet.onWalletStatusChanged, self.__onWalletStatusChanged))

    def __onSwitchView(self, menuName):
        self.__nyController.setLastViewedTab(self.__currentViewName, self.__currentTab)
        selectedTab = None
        self.__tabsController = self.__controllers.get(menuName)
        if self.__tabsController is not None:
            self.__updateTabs(None, menuName)
            selectedTab = self.__tabsController.getSelectedName(self.viewModel.getItemsTabBar())
        else:
            self.__clearTabs()
        if self.__currentViewName != menuName or self.__currentTab != selectedTab:
            self.__currentViewName = menuName
            self.__currentTab = selectedTab
            if self.__regionName:
                uniprof.exitFromRegion(self.__regionName)
            self.__regionName = selectedTab
            if self.__regionName:
                uniprof.enterToRegion(self.__regionName)
        return

    def __updateTabs(self, tabName, menuName=None):
        if tabName is not None:
            if self.__tabsController.getCurrentTabName() != tabName:
                self.__tabsController.selectTab(tabName)
        self.__fillTabs(menuName)
        return

    def __fillTabs(self, menuName=None):
        with self.viewModel.transaction() as (model):
            tabsArray = model.getItemsTabBar()
            self.__tabsController.createTabModels(tabsArray)
            tabIdx = self.__tabsController.getSelectedTabIdx()
            model.setStartIndex(tabIdx)
            self.__triggerHintsController.setActiveSidebarTabs(model, menuName if menuName else self.__currentViewName, self.__tabsController.getCurrentTabName())

    def __validateTabs(self):
        if self.__tabsController is None:
            return
        else:
            self.__tabsController.updateTabModels(self.viewModel.getItemsTabBar())
            if self.__currentTab != self.__tabsController.getCurrentTabName():
                self.__onChangeTab(self.__tabsController.getDefaultTab())
            return

    def __clearTabs(self):
        with self.viewModel.transaction() as (model):
            tabsArray = model.getItemsTabBar()
            tabsArray.clear()
            tabsArray.invalidate()
            model.setStartIndex(0)

    def __onDataUpdated(self, keys, _):
        checkKeys = {
         SyncDataKeys.INVENTORY_TOYS, SyncDataKeys.SLOTS, SyncDataKeys.TOY_COLLECTION,
         SyncDataKeys.RESOURCE_COLLECTING,
         SyncDataKeys.SELECTED_DISCOUNTS}
        if set(keys) & checkKeys:
            self.__checkCooldown()
            self.__validateTabs()

    def __onSacksUpdated(self):
        if self.__currentViewName == NyWidgetTopMenu.CHALLENGE:
            self.__validateTabs()

    def __onQuestUpdated(self):
        self.__validateTabs()

    def __onCelebCompletedTokensUpdated(self):
        if self.__currentViewName == NyWidgetTopMenu.CHALLENGE:
            self.__validateTabs()

    def __onInventoryUpdate(self, invDiff):
        if GUI_ITEM_TYPE.CUSTOMIZATION in invDiff and self.__currentViewName == NyWidgetTopMenu.MARKETPLACE:
            self.__validateTabs()

    def __checkCooldown(self):
        cooldown = getCollectingCooldownTime()
        if cooldown > 0:
            self.__notifier.startNotification()
        else:
            self.__notifier.stopNotification()

    def __onResourcesUpdated(self):
        self.__checkCooldown()
        self.__validateTabs()

    def __onFriendsUpdated(self, _=None):
        if self.__currentViewName == NyWidgetTopMenu.FRIEND_GLADE:
            self.__validateTabs()

    def __onSettingsChanged(self, diff):
        if self.__tabsController is None:
            return
        else:
            tabSettingKeys = self.__tabsController.getSettingKeysForUpdate()
            if tabSettingKeys.intersection(set(diff.keys())):
                self.__updateTabs(self.__currentTab)
            else:
                customTabs = self.__tabsController.getCustomTabsKeyUpdate()
                intersect = set(diff.keys()).intersection(customTabs.keys())
                if intersect:
                    tabsToUpdate = [ data for key, data in customTabs.iteritems() if key in intersect ]
                    self.__tabsController.updateTabsModel(tabsToUpdate, self.viewModel.getItemsTabBar())
            return

    def __onTriggerHintsStateChanged(self):
        if self.__tabsController is None:
            return
        else:
            self.__fillTabs()
            return

    def __onWalletStatusChanged(self, *_):
        if self.__currentViewName == NyWidgetTopMenu.GLADE:
            self.__validateTabs()

    def __onChangeTab(self, tabName):
        self.__soundsManager.playEvent(NewYearSoundEvents.SIDE_BAR_CLICK)
        self.__selectTab(tabName)
        if self.__regionName:
            uniprof.exitFromRegion(self.__regionName)
        self.__regionName = tabName
        uniprof.enterToRegion(self.__regionName)

    def __onExitTab(self):
        self.__soundsManager.onExitView()

    def __selectTab(self, tabName):
        self.__currentTab = tabName
        self.__tabsController.selectTab(tabName)
        with self.viewModel.transaction() as (model):
            model.setStartIndex(self.__tabsController.getSelectedTabIdx())
            self.__triggerHintsController.setActiveSidebarTabs(model, self.__currentViewName, tabName)
        self.__soundsManager.onEnterView()

    def __getEntranceSoundEvent(self):
        return self.__getSoundEvent(NewYearSoundConfigKeys.ENTRANCE_EVENT)

    def __getExitSoundEvent(self):
        return self.__getSoundEvent(NewYearSoundConfigKeys.EXIT_EVENT)

    def __getSoundEvent(self, eventType):
        if self.__currentViewName in (NyWidgetTopMenu.GLADE, NyWidgetTopMenu.FRIEND_GLADE):
            return _GLADE_SOUNDS_MAP.get(eventType, {}).get(self.__currentTab)
        else:
            if self.__currentViewName == NyWidgetTopMenu.MARKETPLACE:
                return _MARKETPLACE_SOUNDS_MAP.get(eventType, {}).get(self.__currentTab)
            if self.__currentViewName in (NyWidgetTopMenu.CHALLENGE, NyWidgetTopMenu.FRIEND_CHALLENGE):
                camObj = CHALLENGE_TAB_TO_CAMERA_OBJ.get(self.__currentTab)
                return _GUESTS_SOUNDS_MAP.get(eventType, {}).get(camObj)
            return

    def __getSoundStateValue(self):
        if self.__currentViewName == NyWidgetTopMenu.GLADE:
            selectedTabName = self.__tabsController.getCurrentTabName()
            return _GLADE_SOUNDS_MAP.get(NewYearSoundConfigKeys.STATE_VALUE, {}).get(selectedTabName)
        else:
            if self.__currentViewName == NyWidgetTopMenu.CHALLENGE:
                camObj = CHALLENGE_TAB_TO_CAMERA_OBJ.get(self.__currentTab)
                return _GUESTS_SOUNDS_MAP.get(NewYearSoundConfigKeys.STATE_VALUE, {}).get(camObj)
            return

    def __getSoundStateGroup(self):
        if self.__currentViewName == NyWidgetTopMenu.CHALLENGE:
            return _GUESTS_SOUNDS_MAP.get(NewYearSoundConfigKeys.STATE_GROUP)
        else:
            return