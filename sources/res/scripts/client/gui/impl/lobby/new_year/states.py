from functools import partial
import typing, CGF, BigWorld, adisp
from ClientSelectableCameraObject import ClientSelectableCameraObject
from HeroTank import HeroTank
from account_helpers.settings_core.settings_constants import NewYearStorageKeys
from cgf_components.hangar_camera_manager import HangarCameraManager
from frameworks.state_machine import StateFlags, visitor
from frameworks.state_machine.transitions import TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates, CameraRelatedEvents
from gui.shared.event_dispatcher import showHOInfoViewWindow, showHOGiftMachineLootListView, showHangar, showHeroTankPreview
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.app_loader import sf_lobby
from gui.impl import backport
from gui.impl.lobby.new_year.ny_views_helpers import executeContext
from gui.impl.new_year.navigation import NewYearNavigation
from gui.impl.new_year.sounds import NewYearSoundsManager, NewYearSoundEvents
from gui.lobby_state_machine.router import SubstateRouter
from gui.lobby_state_machine.states import ViewLobbyState, SubScopeSubLayerState, LobbyState, LobbyStateFlags, LobbyStateDescription
from gui.impl.gen import R
from helpers import dependency
from new_year.celebrity.celebrity_quests_helpers import checkSacksBuyingAbility
from new_year.ny_constants import NYObjects, GuestsQuestsTokens, NyWidgetTopMenu, NyTabBarMarketplaceView, NyTabBarFriendGladeView, NyTabBarMainView, FRIEND_GLADE_TAB_TO_OBJECTS, NyTabBarChallengeView, CHALLENGE_TAB_TO_CAMERA_OBJ
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.new_year import ICelebritySceneController, ICelebrityController, INewYearController, IFriendServiceController, INewYearTutorialController, IGiftMachineController
if typing.TYPE_CHECKING:
    from gui.impl.lobby.new_year.main_view import MainView
_SWITCH_OBJECT_SOUND_EVENTS = {NYObjects.TREE: NewYearSoundEvents.TRANSITION_TREE, 
   NYObjects.SCULPTURE: NewYearSoundEvents.TRANSITION_INSTALLATION, 
   NYObjects.FIELD_KITCHEN: NewYearSoundEvents.TRANSITION_FAIR, 
   NYObjects.RESOURCES: NewYearSoundEvents.TRANSITION_RESOURCES, 
   NYObjects.CHALLENGE: NewYearSoundEvents.TRANSITION_CELEBRITY, 
   NYObjects.CELEBRITY_A: NewYearSoundEvents.TRANSITION_CELEBRITY, 
   NYObjects.CELEBRITY_CAT: NewYearSoundEvents.TRANSITION_CELEBRITY, 
   NYObjects.CELEBRITY_D: NewYearSoundEvents.TRANSITION_CELEBRITY, 
   NYObjects.CELEBRITY: NewYearSoundEvents.TRANSITION_CELEBRITY}

def registerStates(machine):
    machine.addState(HolidayOpsState())


def registerTransitions(machine):
    holidayOpsMain = machine.getStateByCls(HolidayOpsState)
    machine.addNavigationTransitionFromParent(holidayOpsMain)


def getLastPathSegment(stateID):
    return stateID.split('/')[(-1)]


def getMainMenuName(stateID):
    keys = stateID.split('/')
    menuIndex = keys.index(VIEW_ALIAS.HOLIDAY_OPS)
    return keys[(menuIndex + 1)]


@adisp.adisp_process
@dependency.replace_none_kwargs(friendsService=IFriendServiceController)
def switchToFriendView(friendsService=None):
    yield friendsService.enterFriendHangar(None)
    if friendsService.isInFriendHangar:
        NewYearSoundsManager.setHangarPlaceFriends()
        FriendGladeResourcesState.goTo(instantly=True)
    return


holidayOpsNavigationButton = LobbyStateDescription.Info(onMoreInfoRequested=showHOInfoViewWindow, tooltipBody=backport.text(R.strings.ny.widget.menu.info.body()), tooltipHeader=backport.text(R.strings.ny.widget.menu.info.header()))

class HolidayOpsNavigationMixin(object):

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.ny.titles.newYear()), infos=(
         holidayOpsNavigationButton,))


class HolidayOpsStylePreviewMixin(object):

    def registerTransitions(self):
        from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import StylePreviewState
        lsm = self.getMachine()
        self.addNavigationTransition(lsm.getStateByCls(StylePreviewState), record=True)


@SubScopeSubLayerState.parentOf
class HolidayOpsState(HolidayOpsNavigationMixin, ViewLobbyState):
    STATE_ID = VIEW_ALIAS.HOLIDAY_OPS
    VIEW_KEY = ViewKey(VIEW_ALIAS.HOLIDAY_OPS)
    __DEFAULT_CAMERAS = ('HeroTank', 'Customization', 'Tank', 'Platoon')
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __nyController = dependency.descriptor(INewYearController)
    __friendsService = dependency.descriptor(IFriendServiceController)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(HolidayOpsState, self).__init__(flags=flags | LobbyStateFlags.HANGAR)
        self._router = None
        return

    def registerStates(self):
        lsm = self.getMachine()
        lsm.addState(GladeState(flags=StateFlags.INITIAL))
        lsm.addState(FriendsState())
        lsm.addState(ChallengeState())
        lsm.addState(GiftMachineState())
        lsm.addState(MarketplaceState())
        lsm.addState(RewardsState())
        lsm.addState(FriendGladeState())
        lsm.addState(FriendChallengeState())

    def registerTransitions(self):
        lsm = self.getMachine()
        children = self.getChildrenStates()
        for state in children:
            lsm.addNavigationTransitionFromParent(state)
            self.getParent().addNavigationTransition(state)

    def _onEntered(self, event):
        super(HolidayOpsState, self)._onEntered(event)
        self._router = SubstateRouter(self.getMachine(), self._getView(), self)
        self._router.init()
        ClientSelectableCameraObject.deselectAll()
        g_eventBus.addListener(CameraRelatedEvents.CAMERA_ENTITY_UPDATED, self.__handleSelectedEntityUpdated, EVENT_BUS_SCOPE.DEFAULT)

    def _getView(self):
        appLoader = dependency.instance(IAppLoader)
        app = appLoader.getApp()
        view = app.containerManager.getViewByKey(self.getViewKey())
        return view.content

    def _onExited(self):
        self._router.fini()
        self._router = None
        NewYearNavigation.setObject(None)
        if self.__friendsService.isInFriendHangar:
            self.__friendsService.leaveFriendHangar()
        g_eventBus.removeListener(CameraRelatedEvents.CAMERA_ENTITY_UPDATED, self.__handleSelectedEntityUpdated, EVENT_BUS_SCOPE.DEFAULT)
        self._switchCameraToTank()
        super(HolidayOpsState, self)._onExited()
        return

    def _switchCameraToTank(self):
        if self.__hangarSpace.space is None:
            return
        else:
            cameraManager = CGF.getManager(self.__hangarSpace.spaceID, HangarCameraManager)
            if not cameraManager:
                return
            if cameraManager.getCurrentCameraName() not in self.__DEFAULT_CAMERAS:
                cameraManager.switchToTank(instantly=not self.__nyController.isEnabled())
            return

    def __handleSelectedEntityUpdated(self, event):
        ctx = event.ctx
        if ctx['state'] != CameraMovementStates.FROM_OBJECT:
            entityId = ctx['entityId']
            entity = BigWorld.entities.get(entityId, None)
            if isinstance(entity, HeroTank):
                descriptor = entity.typeDescriptor
                if descriptor:
                    showHeroTankPreview(descriptor.type.compactDescr)
            elif self.__hangarSpace.space and entityId == self.__hangarSpace.space.vehicleEntityId:
                showHangar()
        return


class BaseState(HolidayOpsNavigationMixin, LobbyState):
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __settingsCore = dependency.descriptor(ISettingsCore)
    __nyTutorialController = dependency.descriptor(INewYearTutorialController)

    @classmethod
    def goTo(cls, **params):
        nyStorage = cls.__settingsCore.serverSettings.getNewYearStorage()
        isIntroShown = nyStorage.get(NewYearStorageKeys.NY_INTRO_SHOWN, False)
        if not isIntroShown:
            cls.__nyTutorialController.onIntroEnd += partial(cls.goTo, **params)
            cls.__nyTutorialController.startIntro(cameraSwitchNeeded=False)
            return
        super(BaseState, cls).goTo(**params)

    def getObject(self):
        return

    def _onEntered(self, event):
        super(BaseState, self)._onEntered(event)
        objectName = self.getObject()
        NewYearNavigation.setObject(objectName)
        if objectName is None:
            return
        else:
            instantly = event.params.get('instantly')
            self.switchCamera(objectName, instantly)
            self.playTransitionSound(objectName)
            executeAfterLoaded = event.params.get('executeAfterLoaded')
            if executeAfterLoaded:
                executeContext(executeAfterLoaded)
            return

    @sf_lobby
    def _app(self):
        return

    def switchCamera(self, cameraName, instantly=True):
        if self.__hangarSpace.space is None:
            return
        else:
            cameraManager = CGF.getManager(self.__hangarSpace.spaceID, HangarCameraManager)
            if cameraManager and cameraName:
                cameraManager.switchByCameraName(cameraName, instantly)
            return

    def playTransitionSound(self, objectName):
        lsm = self.getMachine()
        if not visitor.isDescendantOf(self, lsm.getStateByCls(GladeState)) and not visitor.isDescendantOf(self, lsm.getStateByCls(ChallengeState)):
            return
        eventName = _SWITCH_OBJECT_SOUND_EVENTS.get(objectName)
        if eventName:
            NewYearSoundsManager.playEvent(eventName)


@HolidayOpsState.parentOf
class GladeState(LobbyState):
    STATE_ID = NyWidgetTopMenu.GLADE

    def getObject(self):
        return NYObjects.TREE

    def registerStates(self):
        lsm = self.getMachine()
        lsm.addState(GladeResourcesState())
        lsm.addState(GladeTownState())
        lsm.addState(GladeFirState(flags=StateFlags.INITIAL))
        lsm.addState(GladeFairState())
        lsm.addState(GladeInstallationState())

    def registerTransitions(self):
        lsm = self.getMachine()
        holidayOpsMain = lsm.getStateByCls(HolidayOpsState)
        children = self.getChildrenStates()
        for state in children:
            lsm.addNavigationTransitionFromParent(state)
            holidayOpsMain.addNavigationTransition(state)
            holidayOpsMain.getParent().addNavigationTransition(state)


class GladeTabState(BaseState):

    def getObject(self):
        return getLastPathSegment(self.getStateID())


@GladeState.parentOf
class GladeResourcesState(GladeTabState):
    STATE_ID = NyTabBarMainView.RESOURCES


@GladeState.parentOf
class GladeTownState(GladeTabState):
    STATE_ID = NyTabBarMainView.TOWN


@GladeState.parentOf
class GladeFirState(GladeTabState):
    STATE_ID = NyTabBarMainView.FIR


@GladeState.parentOf
class GladeFairState(GladeTabState):
    STATE_ID = NyTabBarMainView.FAIR


@GladeState.parentOf
class GladeInstallationState(GladeTabState):
    STATE_ID = NyTabBarMainView.INSTALLATION


@HolidayOpsState.parentOf
class FriendsState(BaseState):
    STATE_ID = NyWidgetTopMenu.FRIENDS


@HolidayOpsState.parentOf
class ChallengeState(LobbyState):
    STATE_ID = NyWidgetTopMenu.CHALLENGE

    def getObject(self):
        return NYObjects.CHALLENGE

    def registerStates(self):
        lsm = self.getMachine()
        lsm.addState(EntryState(flags=StateFlags.INITIAL))
        lsm.addState(TournamentState())
        lsm.addState(TournamentCompletedState())
        lsm.addState(AssignmentsState())
        lsm.addState(GuestCState())
        lsm.addState(GuestDState())
        lsm.addState(HeadquartersState())

    def registerTransitions(self):
        lsm = self.getMachine()
        children = self.getChildrenStates()
        holidayOpsMain = lsm.getStateByCls(HolidayOpsState)
        for state in children:
            lsm.addNavigationTransitionFromParent(state)
            holidayOpsMain.addNavigationTransition(state)
            holidayOpsMain.getParent().addNavigationTransition(state)


class ChallengeTabState(BaseState):

    def getObject(self):
        name = getLastPathSegment(self.STATE_ID)
        return CHALLENGE_TAB_TO_CAMERA_OBJ.get(name)


@ChallengeState.parentOf
class TournamentState(HolidayOpsStylePreviewMixin, ChallengeTabState):
    STATE_ID = NyTabBarChallengeView.TOURNAMENT

    def getBackNavigationDescription(self, params):
        return backport.text(R.strings.ny.tournament.backLabel())

    def _onEntered(self, event):
        objectName = self.getObject()
        NewYearNavigation.setObject(objectName)
        self.playTransitionSound(objectName)
        BigWorld.worldDrawEnabled(False)
        self.switchCamera(objectName, instantly=True)
        executeAfterLoaded = event.params.get('executeAfterLoaded')
        if executeAfterLoaded:
            executeContext(executeAfterLoaded)

    def _onExited(self):
        BigWorld.worldDrawEnabled(True)
        super(TournamentState, self)._onExited()


@ChallengeState.parentOf
class TournamentCompletedState(TournamentState):
    STATE_ID = NyTabBarChallengeView.TOURNAMENT_COMPLETED


@ChallengeState.parentOf
class AssignmentsState(HolidayOpsStylePreviewMixin, ChallengeTabState):
    STATE_ID = NyTabBarChallengeView.GUEST_A

    def getBackNavigationDescription(self, params):
        return backport.text(R.strings.ny.celebrityChallenge.backLabel())


@ChallengeState.parentOf
class GuestCState(HolidayOpsStylePreviewMixin, ChallengeTabState):
    STATE_ID = NyTabBarChallengeView.GUEST_CAT

    def getBackNavigationDescription(self, params):
        return backport.text(R.strings.ny.celebrityChallenge.backLabel())


@ChallengeState.parentOf
class GuestDState(ChallengeTabState):
    STATE_ID = NyTabBarChallengeView.GUEST_D


@ChallengeState.parentOf
class HeadquartersState(ChallengeTabState):
    STATE_ID = NyTabBarChallengeView.HEADQUARTERS


@ChallengeState.parentOf
class EntryState(ChallengeTabState):
    STATE_ID = 'entry'
    __nyController = dependency.descriptor(INewYearController)
    __celebrityController = dependency.descriptor(ICelebrityController)
    __celebritySceneController = dependency.descriptor(ICelebritySceneController)

    def _onEntered(self, event):
        doAutoRouting = event.params.get('doAutoRouting')
        instantly = event.params.get('instantly')
        if doAutoRouting:
            if not self.__celebritySceneController.isChallengeCompleted:
                TournamentState.goTo(instantly=instantly)
            elif not self.__celebrityController.isGuestQuestsCompletedFully((GuestsQuestsTokens.GUEST_A,)):
                AssignmentsState.goTo(instantly=instantly)
            elif self.__nyController.isTokenReceived(GuestsQuestsTokens.TOKEN_CAT) and not self.__celebrityController.isGuestQuestsCompletedFully((GuestsQuestsTokens.GUEST_C,)):
                GuestCState.goTo(instantly=instantly)
            elif self.__nyController.isTokenReceived(GuestsQuestsTokens.TOKEN_CAT) and self.__nyController.isTokenReceived(GuestsQuestsTokens.TOKEN_DOG) and checkSacksBuyingAbility():
                GuestDState.goTo(instantly=instantly)
            else:
                HeadquartersState.goTo(instantly=instantly)
        else:
            TournamentState.goTo(instantly=instantly)


@HolidayOpsState.parentOf
class GiftMachineState(BaseState):
    STATE_ID = NyWidgetTopMenu.GIFT_MACHINE
    __objectName = NYObjects.GIFT_MACHINE
    __nyGiftMachineCtrl = dependency.descriptor(IGiftMachineController)

    def _onEntered(self, event):
        self.__objectName = event.params.get('objectName', NYObjects.GIFT_MACHINE)
        self.__nyGiftMachineCtrl.onLootListInfoUpdated += self.__update
        super(GiftMachineState, self)._onEntered(event)

    def _onExited(self):
        self.__nyGiftMachineCtrl.onLootListInfoUpdated -= self.__update
        super(GiftMachineState, self)._onExited()

    def __update(self):
        GiftMachineState.goTo(instantly=True)

    def getObject(self):
        return self.__objectName

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(lsm.getStateByCls(GiftMachineState), transitionType=TransitionType.EXTERNAL)

    def getNavigationDescription(self):
        if bool(self.__nyGiftMachineCtrl.getLootListInfo()):
            lootListButton = LobbyStateDescription.Info(label=backport.text(R.strings.ny.menu.showGiftMachineLootList()), type=LobbyStateDescription.Info.Type.GIFT_MACHINE, onMoreInfoRequested=showHOGiftMachineLootListView)
            return LobbyStateDescription(title=backport.text(R.strings.ny.titles.newYear()), infos=(
             holidayOpsNavigationButton, lootListButton))
        return super(GiftMachineState, self).getNavigationDescription()


@HolidayOpsState.parentOf
class MarketplaceState(LobbyState):
    STATE_ID = NyWidgetTopMenu.MARKETPLACE
    __nyController = dependency.descriptor(INewYearController)

    def getObject(self):
        return NYObjects.MARKETPLACE

    def registerStates(self):
        lsm = self.getMachine()
        lsm.addState(PreviousCollectionsState())
        lsm.addState(CollectionEntryState(flags=StateFlags.INITIAL))
        lsm.addState(Collection1State())
        lsm.addState(Collection2State())
        lsm.addState(Collection3State())
        lsm.addState(Collection4State())
        lsm.addState(Collection5State())

    def registerTransitions(self):
        lsm = self.getMachine()
        children = self.getChildrenStates()
        for state in children:
            lsm.addNavigationTransitionFromParent(state)

    def _onEntered(self, event):
        lsm = self.getMachine()
        instantly = event.params.get('instantly')
        _, self.__tabName = self.__nyController.getFirstNonReceivedMarketPlaceCollectionData()
        lastViewedTab = self.__nyController.getLastViewedTab(NyWidgetTopMenu.MARKETPLACE)
        if lastViewedTab:
            category = lastViewedTab
        else:
            category = NyTabBarMarketplaceView.PREVIOUS_CATEGORY if self.__tabName in NyTabBarMarketplaceView.PREVIOUS_CATEGORIES else self.__tabName
        targetState = lsm.getStateByID(event.targetStateID + '/' + category)
        targetState.goTo(instantly=instantly)


class CollectionState(BaseState):

    def getObject(self):
        return NYObjects.MARKETPLACE


@MarketplaceState.parentOf
class PreviousCollectionsState(CollectionState):
    STATE_ID = NyTabBarMarketplaceView.PREVIOUS_CATEGORY


@MarketplaceState.parentOf
class CollectionEntryState(BaseState):
    STATE_ID = 'entry'


@MarketplaceState.parentOf
class Collection1State(CollectionState):
    STATE_ID = NyTabBarMarketplaceView.VISIBLE_CATEGORIES[0]


@MarketplaceState.parentOf
class Collection2State(CollectionState):
    STATE_ID = NyTabBarMarketplaceView.VISIBLE_CATEGORIES[1]


@MarketplaceState.parentOf
class Collection3State(CollectionState):
    STATE_ID = NyTabBarMarketplaceView.VISIBLE_CATEGORIES[2]


@MarketplaceState.parentOf
class Collection4State(CollectionState):
    STATE_ID = NyTabBarMarketplaceView.VISIBLE_CATEGORIES[3]


@MarketplaceState.parentOf
class Collection5State(CollectionState):
    STATE_ID = NyTabBarMarketplaceView.VISIBLE_CATEGORIES[4]


@HolidayOpsState.parentOf
class RewardsState(BaseState):
    STATE_ID = NyWidgetTopMenu.REWARDS


class HolidayOpsFriendHangarNavigationMixin(object):

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.ny.titles.friendHangar()), infos=(
         holidayOpsNavigationButton,))


@HolidayOpsState.parentOf
class FriendGladeState(LobbyState):
    STATE_ID = NyWidgetTopMenu.FRIEND_GLADE

    def getObject(self):
        return NYObjects.TREE

    def registerStates(self):
        lsm = self.getMachine()
        lsm.addState(FriendGladeResourcesState())
        lsm.addState(FriendGladeTownState())
        lsm.addState(FriendGladeFirState(flags=StateFlags.INITIAL))
        lsm.addState(FriendGladeFairState())
        lsm.addState(FriendGladeInstallationState())

    def registerTransitions(self):
        lsm = self.getMachine()
        children = self.getChildrenStates()
        for state in children:
            lsm.addNavigationTransitionFromParent(state)
            self.getParent().addNavigationTransition(state)

        holidayOps = lsm.getStateByCls(HolidayOpsState)
        friendResources = lsm.getStateByCls(FriendGladeResourcesState)
        holidayOps.getParent().addNavigationTransition(friendResources)


class FriendGladeTabState(HolidayOpsFriendHangarNavigationMixin, BaseState):

    def getObject(self):
        name = getLastPathSegment(self.STATE_ID)
        return FRIEND_GLADE_TAB_TO_OBJECTS.get(name)


@FriendGladeState.parentOf
class FriendGladeResourcesState(FriendGladeTabState):
    STATE_ID = NyTabBarFriendGladeView.RESOURCES


@FriendGladeState.parentOf
class FriendGladeTownState(FriendGladeTabState):
    STATE_ID = NyTabBarFriendGladeView.TOWN


@FriendGladeState.parentOf
class FriendGladeFirState(FriendGladeTabState):
    STATE_ID = NyTabBarFriendGladeView.FIR


@FriendGladeState.parentOf
class FriendGladeFairState(FriendGladeTabState):
    STATE_ID = NyTabBarFriendGladeView.FAIR


@FriendGladeState.parentOf
class FriendGladeInstallationState(FriendGladeTabState):
    STATE_ID = NyTabBarFriendGladeView.INSTALLATION


@HolidayOpsState.parentOf
class FriendChallengeState(HolidayOpsFriendHangarNavigationMixin, BaseState):
    STATE_ID = NyWidgetTopMenu.FRIEND_CHALLENGE

    def getObject(self):
        return NYObjects.CELEBRITY


STATES_BY_OBJECT = {NYObjects.RESOURCES: GladeResourcesState, 
   NYObjects.TOWN: GladeTownState, 
   NYObjects.TREE: GladeFirState, 
   NYObjects.FIELD_KITCHEN: GladeFairState, 
   NYObjects.SCULPTURE: GladeInstallationState, 
   NYObjects.CHALLENGE: EntryState, 
   NYObjects.CELEBRITY_A: AssignmentsState, 
   NYObjects.CELEBRITY_CAT: GuestCState, 
   NYObjects.CELEBRITY_D: GuestDState, 
   NYObjects.CELEBRITY: HeadquartersState, 
   NYObjects.GIFT_MACHINE: GiftMachineState, 
   NYObjects.GIFT_MACHINE_SIDE: GiftMachineState, 
   NYObjects.MARKETPLACE: MarketplaceState}
FRIEND_STATES_BY_OBJECT = {NYObjects.RESOURCES: FriendGladeResourcesState, 
   NYObjects.TOWN: FriendGladeTownState, 
   NYObjects.TREE: FriendGladeFirState, 
   NYObjects.FIELD_KITCHEN: FriendGladeFairState, 
   NYObjects.SCULPTURE: FriendGladeInstallationState, 
   NYObjects.CELEBRITY: FriendChallengeState}