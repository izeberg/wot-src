import typing
from adisp import adisp_process
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.ny_tabs import FriendGladeViewTabs
from gui.impl.gen.view_models.views.lobby.new_year.views.friend_glade.ny_friend_glade_view_model import NyFriendGladeViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.friend_glade.ny_resources_view_model import State
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.group_slots_model import GroupSlotsModel
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.slot_model import SlotModel
from gui.impl.lobby.new_year.friends.resource_box_presenter import ResourceBoxPresenter
from gui.impl.lobby.new_year.ho_selectable_logic_presenter import HOSelectableLogicPresenter
from gui.impl.lobby.new_year.ho_sidebar_component import ViewWithSidebarStateObserver
from gui.impl.lobby.new_year.scene_rotatable_view import SceneRotatableView
from gui.impl.lobby.new_year.states import FriendGladeState
from gui.impl.lobby.new_year.tooltips.ny_decoration_tooltip import NyDecorationTooltip
from gui.impl.lobby.new_year.tooltips.ny_resource_box_tooltip import NyResourceBoxTooltip
from gui.impl.new_year.new_year_helper import nyCreateToolTipContentDecorator
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import NyResourcesEvent
from helpers import dependency, time_utils
from helpers.CallbackDelayer import CallbackDelayer
from helpers.time_utils import ONE_SECOND
from items.components.ny_constants import TOY_TYPES_BY_FRIEND_OBJECT, INVALID_TOY_ID, FRIEND_CUSTOMIZATION_OBJECTS_MAP
from ny_common.GeneralConfig import GeneralConfig
from new_year.friend_service_controller import BestFriendsDataKeys, FriendsDataKeys
from new_year.ny_helper import getNYGeneralConfig
from new_year.ny_resource_collecting_helper import getAvgResourcesByCollecting
from skeletons.new_year import IFriendServiceController, INewYearController
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.new_year.views.friend_glade.ny_resources_view_model import NyResourcesViewModel
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine

class HOFriendGladeView(SceneRotatableView, HOSelectableLogicPresenter):
    __nyController = dependency.descriptor(INewYearController)
    __friendsService = dependency.descriptor(IFriendServiceController)

    def __init__(self, model, parent, *args, **kwargs):
        super(HOFriendGladeView, self).__init__(model, parentView=parent)
        self.__currentObject = None
        self.__resourceBoxPresenter = None
        self.__isFirstVisit = True
        self.__delayer = CallbackDelayer()
        self.__isCollectRequestPending = False
        self.__stateObserver = None
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def initialize(self, *args, **kwargs):
        self.__stateObserver = ViewWithSidebarStateObserver(FriendGladeState)
        lsm = getLobbyStateMachine()
        lsm.connect(self.__stateObserver)
        super(HOFriendGladeView, self).initialize(*args, **kwargs)
        self.__resourceBoxPresenter = ResourceBoxPresenter(self.viewModel.resourceBoxModel, self)
        self.__resourceBoxPresenter.initialize()

    def finalize(self):
        self.__delayer.clearCallbacks()
        self.__resourceBoxPresenter.finalize()
        self.__resourceBoxPresenter = None
        super(HOFriendGladeView, self).finalize()
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__stateObserver)
        self.__stateObserver.clear()
        self.__stateObserver = None
        return

    def createToolTip(self, event):
        return self.__resourceBoxPresenter.createToolTip(event) or super(HOFriendGladeView, self).createToolTip(event)

    @nyCreateToolTipContentDecorator
    def createToolTipContent(self, event, contentID):
        if event.contentID == R.views.mono.holiday_ops.tooltips.ho_resource_box_tooltip():
            return NyResourceBoxTooltip(event.getArgument('isFriendsList'))
        if contentID == R.views.mono.holiday_ops.tooltips.ho_decoration_tooltip():
            toyID = event.getArgument('toyID')
            return NyDecorationTooltip(toyID)
        return super(HOFriendGladeView, self).createToolTipContent(event, contentID)

    def _getEvents(self):
        events = super(HOFriendGladeView, self)._getEvents()
        return events + (
         (
          self.viewModel.resourcesViewModel.onCollect, self.__onCollect),
         (
          self.viewModel.resourcesViewModel.onSetFavoriteFriend, self.__onSetFavoriteFriend),
         (
          self.viewModel.resourcesViewModel.onHideFinishedStatus, self.__onHideFinishedStatus),
         (
          self.__stateObserver.onSidebarSelected, self.__onSideBarSelected),
         (
          self.__friendsService.onFriendHangarEnter, self.__onFriendHangarUpdate))

    def __onSideBarSelected(self, tabName, _):
        self.__currentObject = tabName
        self.__updateAll()

    def __onFriendHangarUpdate(self, *_):
        with self.viewModel.transaction() as (model):
            self.__updateResourcesViewModel(model=model.resourcesViewModel)

    def __updateAll(self):
        with self.viewModel.transaction() as (model):
            model.setTabName(self.__currentObject)
            self.__updateWelcomeText(model=model)
            self.__updateSlots(fullUpdate=True, model=model)
            self.__updateResourcesViewModel(model=model.resourcesViewModel)

    def __updateSlots(self, fullUpdate, model):
        slotsData = self.__nyController.requester.getSlotsData()
        groups = TOY_TYPES_BY_FRIEND_OBJECT.get(self.__currentObject, {})
        toys = self.__nyController.requester.getToys()
        actualLength = len(groups)
        currentLength = model.toySlotsBar.groupSlots.getItemsLength()
        if currentLength != actualLength:
            fullUpdate = True
            if actualLength > currentLength:
                for _ in range(actualLength - currentLength):
                    model.toySlotsBar.groupSlots.addViewModel(GroupSlotsModel())

            else:
                for _ in range(currentLength - actualLength):
                    model.toySlotsBar.groupSlots.removeItemByIndex(model.toySlotsBar.groupSlots.getItemsLength() - 1)

        slots = self.__nyController.getSlotDescrs()
        for groupIdx, groupName in enumerate(groups):
            descrSlots = [ slot for slot in slots if slot.type == groupName ]
            groupModel = model.toySlotsBar.groupSlots.getItem(groupIdx)
            currentLevel = self.__nyController.customizationObjects.getLevel(FRIEND_CUSTOMIZATION_OBJECTS_MAP[self.__currentObject])
            if fullUpdate:
                groupModel.slots.clear()
            for slotIdx, slotDescr in enumerate(descrSlots):
                toyID = slotsData[slotDescr.id]
                slotType = slotDescr.type
                isEmpty = toyID == INVALID_TOY_ID
                if isEmpty:
                    icon = R.images.gui.maps.icons.newYear.decoration_types.craft_small.dyn(slotType)()
                else:
                    toy = toys[slotDescr.id][toyID]
                    icon = toy.getIcon()
                slot = SlotModel() if fullUpdate else groupModel.slots.getItem(slotIdx)
                slot.setSlotId(slotDescr.id)
                slot.setIsEmpty(isEmpty)
                slot.setUnlockLevel(slotDescr.unlockLevelID)
                slot.setIsLocked(slotDescr.unlockLevelID > currentLevel)
                slot.setToyId(toyID)
                slot.setIcon(icon)
                if fullUpdate:
                    groupModel.slots.addViewModel(slot)

        if fullUpdate:
            model.toySlotsBar.groupSlots.invalidate()

    def __updateResourcesViewModel(self, model):
        bestFriends = self.__friendsService.bestFriendList
        if self.__friendsService.friendHangarSpaId not in bestFriends:
            if len(bestFriends) >= self.__friendsService.maxBestFriendsCount:
                friendsCooldown = self.__friendsResourcesCollectCooldown(bestFriends)
                if friendsCooldown > 0.0:
                    model.setCooldown(friendsCooldown)
                    model.setState(State.LIMITTIMER)
                else:
                    model.setState(State.LIMIT)
            else:
                model.setState(State.NOTFAVORITE)
        else:
            cooldown = self.__friendsService.getFriendCollectingCooldownTime()
            eventEndTimeTill = getNYGeneralConfig().getEventEndTime() - time_utils.getServerUTCTime()
            friendHangarSpaId = self.__friendsService.friendHangarSpaId
            isFinishVisited = self.__nyController.getFriendsResourcesFinishVisited(friendHangarSpaId)
            if cooldown > 0.0:
                if cooldown > eventEndTimeTill:
                    model.setState(State.FINISHEDHIDDEN if isFinishVisited else State.FINISHED)
                else:
                    model.setCooldown(self.__friendsService.getFriendCollectingCooldownTime())
                    model.setState(State.TIMER)
                    self.__delayer.stopCallback(self.__cooldownUpdate)
                    self.__delayer.delayCallback(cooldown + ONE_SECOND, self.__cooldownUpdate)
            else:
                model.setState(State.AVAILABLE)
        model.setCollectAmount(getAvgResourcesByCollecting())

    @staticmethod
    def __friendsResourcesCollectCooldown(bestFriends):
        return min(max(bestFriendInfo[BestFriendsDataKeys.RESOURCES_COOLDOWN] - time_utils.getServerUTCTime(), 0) for bestFriendInfo in bestFriends.itervalues())

    @adisp_process
    def __cooldownUpdate(self):
        isSuccess = yield self.__friendsService.updateFriendList()
        if isSuccess:
            with self.viewModel.transaction() as (model):
                self.__updateResourcesViewModel(model=model.resourcesViewModel)

    def __updateWelcomeText(self, model):
        if not self.__isFirstVisit:
            model.setIsFirstVisit(False)
        elif self.__currentObject != FriendGladeViewTabs.RESOURCES:
            friendHangarState = self.__friendsService.getFriendState()
            titleIdx, descriptionIdx = GeneralConfig.parseHangarNameMask(friendHangarState.get(FriendsDataKeys.HANGAR_NAME, 0))
            model.setIsFirstVisit(True)
            model.hangarName.setTitle(titleIdx)
            model.hangarName.setDescription(descriptionIdx)
            model.setFriendName(self.__friendsService.getFriendName(self.__friendsService.friendHangarSpaId))
            self.__isFirstVisit = False

    @adisp_process
    def __onSetFavoriteFriend(self):
        isSuccess = yield self.__friendsService.addBestFriend(self.__friendsService.friendHangarSpaId)
        if isSuccess and self.__friendsService.friendHangarSpaId in self.__friendsService.bestFriendList:
            with self.viewModel.transaction() as (model):
                self.__updateResourcesViewModel(model=model.resourcesViewModel)

    @adisp_process
    def __onCollect(self):
        if self.__isCollectRequestPending:
            return
        self.__isCollectRequestPending = True
        isSuccess = yield self.__friendsService.collectFriendResources()
        self.__isCollectRequestPending = False
        if isSuccess:
            g_eventBus.handleEvent(NyResourcesEvent(eventType=NyResourcesEvent.FRIEND_RESOURCE_COLLECTED), scope=EVENT_BUS_SCOPE.LOBBY)
            with self.viewModel.transaction() as (model):
                self.__updateResourcesViewModel(model=model.resourcesViewModel)

    def __onHideFinishedStatus(self):
        self.__nyController.setFriendsResourcesFinishVisited(self.__friendsService.friendHangarSpaId)
        self.viewModel.resourcesViewModel.setState(State.FINISHEDHIDDEN)