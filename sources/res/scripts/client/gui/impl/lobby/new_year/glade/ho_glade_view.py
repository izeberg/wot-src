import logging
from functools import partial
import typing
from account_helpers.AccountSettings import NY_MAX_LEVEL_MESSAGE_CLOSE, NY_REWARD_KIT_OPEN
import CGF
from PlayerEvents import g_playerEvents
from account_helpers import AccountSettings
from account_helpers.settings_core import settings_constants
from adisp import adisp_process
from cgf_components.hangar_camera_manager import HangarCameraManager
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui import SystemMessages
from gui.SystemMessages import SM_TYPE
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_resource_collector_tooltip_model import CollectorTooltipType
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.group_slots_model import GroupSlotsModel
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.levelup_price_model import LevelupPriceModel
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.ny_resource_collector_model import CollectState
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.ny_glade_view_model import AnimationLevelUpStates, NyGladeViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.slot_model import SlotModel
from gui.impl.lobby.new_year.glade.ny_toys_list import NyToysList
from gui.impl.lobby.new_year.ho_selectable_logic_presenter import HOSelectableLogicPresenter
from gui.impl.lobby.new_year.ho_sidebar_component import ViewWithSidebarStateObserver
from gui.impl.lobby.new_year.ny_views_helpers import showInfoVideo
from gui.impl.lobby.new_year.scene_rotatable_view import SceneRotatableView
from gui.impl.lobby.new_year.states import GladeState
from gui.impl.lobby.new_year.tooltips.ny_customization_object_tooltip import NyCustomizationObjectTooltip
from gui.impl.lobby.new_year.tooltips.ny_decoration_tooltip import NyDecorationTooltip
from gui.impl.lobby.new_year.tooltips.ny_decoration_unavailable_tooltip import NyDecorationUnavailableTooltip
from gui.impl.lobby.new_year.tooltips.ny_resource_collector_tooltip import NyResourceCollectorTooltip
from gui.impl.lobby.new_year.tooltips.ny_slot_locked_tooltip import NySlotLockedTooltip
from gui.impl.new_year.navigation import NewYearNavigation
from gui.impl.new_year.new_year_helper import formatRomanNumber
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared import events, EVENT_BUS_SCOPE, g_eventBus
from gui.shared.events import ObjectHoverEvent
from gui.shared.lock_overlays import lockNotificationManager
from gui.shared.notifications import NotificationPriorityLevel
from gui.shared.utils.scheduled_notifications import PeriodicNotifier
from gui.shared.view_helpers.blur_manager import CachedBlur
from helpers import dependency, time_utils
from items.components.ny_constants import INVALID_TOY_ID, TOY_TYPES_BY_OBJECT, CurrentNYConstants, CustomizationObjects, NYFriendServiceDataTokens, ToyDropSources
from items.new_year import g_cache as toyCache
from messenger.proto.events import g_messengerEvents
from new_year.newyear_cgf_components.lobby_customization_components import LobbyCustomizableObjectsManager
from new_year.ny_constants import SyncDataKeys, NYObjects, NY_LEVEL_UP_NOTIFICATION_LOCK_KEY, MegaDecorationsObjects
from new_year.ny_helper import getNYGeneralConfig
from new_year.ny_level_helper import NewYearAtmospherePresenter
from new_year.ny_notifications_helpers import checkAndNotifyAllDecorationReceived
from new_year.ny_processor import BuyObjectLevel
from new_year.ny_resource_collecting_helper import getCollectingCooldownTime, getAvgResourcesByCollecting, isCollectingAvailable, isExtraCollectingAvailable, getSkippedDays
from new_year.ny_toy_info import NewYearCurrentToyInfo
from new_year.ny_trigger_hints import TriggerHintsStates
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IWalletController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.new_year import INewYearController, INewYearTriggerHintsController
from wg_async import wg_async, await_callback
if typing.TYPE_CHECKING:
    from ny_common.ObjectsConfig import ObjectsConfig
_logger = logging.getLogger(__name__)
_MEGA_DECORATION_CAMERA_BY_OBJECT = {CustomizationObjects.FIR: MegaDecorationsObjects.FIR, 
   CustomizationObjects.FAIR: MegaDecorationsObjects.FAIR, 
   CustomizationObjects.INSTALLATION: MegaDecorationsObjects.INSTALLATION}

class HOGladeView(SceneRotatableView, HOSelectableLogicPresenter):
    __lobbyCtx = dependency.descriptor(ILobbyContext)
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __nyController = dependency.descriptor(INewYearController)
    __wallet = dependency.instance(IWalletController)
    __triggerHintsController = dependency.descriptor(INewYearTriggerHintsController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, model, parent):
        self.__currentObject = None
        self.__currentMenu = None
        self.__toysList = NyToysList()
        self.__notifier = None
        self.__blur = None
        self.__hoveredObjectName = None
        self.__levelUpInProgress = False
        self.__resourceCollectingLock = False
        self.__levelUpNotificationsLock = False
        self.__cameraManager = None
        self.__totalAtmPoints = None
        self.__stateObserver = None
        super(HOGladeView, self).__init__(model, parent)
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    @property
    def currentTab(self):
        return self.__currentObject

    @property
    def currentMenu(self):
        return self.__currentMenu

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.mono.holiday_ops.tooltips.ho_customization_object_tooltip() and self.__hoveredObjectName:
            return NyCustomizationObjectTooltip(self.__hoveredObjectName)
        if contentID == R.views.mono.holiday_ops.tooltips.ho_decoration_tooltip():
            toyID = event.getArgument('toyID')
            return NyDecorationTooltip(toyID)
        if contentID == R.views.mono.holiday_ops.tooltips.ho_decoration_unavailable_tooltip():
            toyID = event.getArgument('toyID')
            return NyDecorationUnavailableTooltip(toyID)
        if contentID == R.views.mono.holiday_ops.tooltips.ho_resource_collector_tooltip():
            collectorTooltipType = CollectorTooltipType(event.getArgument('type'))
            return NyResourceCollectorTooltip(collectorTooltipType)
        if contentID == R.views.mono.holiday_ops.tooltips.ho_slot_locked_tooltip():
            level = event.getArgument('level')
            return NySlotLockedTooltip(level)
        return super(HOGladeView, self).createToolTipContent(event, contentID)

    def initialize(self, *args, **kwargs):
        self.__stateObserver = ViewWithSidebarStateObserver(GladeState)
        super(HOGladeView, self).initialize(*args, **kwargs)
        lsm = getLobbyStateMachine()
        lsm.connect(self.__stateObserver)
        self.__blur = CachedBlur(blurRadius=0.1)
        self.__notifier = PeriodicNotifier(lambda : time_utils.ONE_SECOND, self.__updateResourceCollectingByNotifier, periods=(
         time_utils.ONE_SECOND,))
        self.__cameraManager = CGF.getManager(self.__hangarSpace.spaceID, HangarCameraManager)
        self.__cameraManager.onCameraSwitched += self.__onCameraSwitched
        self.__itemsCache.onSyncCompleted += self.__onSyncCompleted
        self.__totalAtmPoints = NewYearAtmospherePresenter.getTotalAtmospherePoints()
        with self.viewModel.transaction() as (model):
            model.toySlotsBar.setHasNewToysAnimation(False)
            model.setAnimationLevelUpState(AnimationLevelUpStates.IDLE)
            self.__updateSlots(fullUpdate=True, model=model)
            self.__updateResourceCollecting(model=model)
            self.__updateUpgradeInfo(model=model)
            self.__switchCarouselType(model=model)

    def finalize(self):
        super(HOGladeView, self).finalize()
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__stateObserver)
        self.__hideMaxLevelReward()
        self.__stateObserver.clear()
        self.__stateObserver = None
        self.__itemsCache.onSyncCompleted -= self.__onSyncCompleted
        if self.__cameraManager:
            self.__cameraManager.onCameraSwitched -= self.__onCameraSwitched
        self.__toysList.finalize()
        self.__notifier.stopNotification()
        self.__notifier.clear()
        self.__totalAtmPoints = None
        self.__currentMenu = None
        for slot in self.__nyController.getSlotDescrs():
            self.__setSlotHighlight(slot.id, False)

        self.__clearPopovers()
        if self.__blur is not None:
            self.__blur.fini()
            self.__blur = None
        self.__checkAndStopAnimation()
        g_eventBus.handleEvent(events.NyGladeVisibilityEvent(events.NyGladeVisibilityEvent.GLADE_FINALIZE), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _getEvents(self):
        return super(HOGladeView, self)._getEvents() + (
         (
          self.viewModel.toySlotsBar.onHoverSlot, self.__onHoverSlot),
         (
          self.viewModel.toySlotsBar.onHoverOutSlot, self.__onHoverOutSlot),
         (
          self.viewModel.toySlotsBar.onSelectSlot, partial(self.__onSelectSlot, self.viewModel.toySlotsBar)),
         (
          self.viewModel.toySlotsBar.onAnimationEnd, self.__onUpdateToysAnimationEnd),
         (
          self.viewModel.resourceCollector.onCollect, self.__onCollect),
         (
          self.viewModel.resourceCollector.onHideFinishedStatus, self.__onHideFinishedStatus),
         (
          self.viewModel.customizationLevelUp.onLevelUp, self.__onLevelUp),
         (
          self.viewModel.maxLevelReward.onAccept, self.__onMaxLevelRewardAccept),
         (
          self.viewModel.onMaxLevelMessageClosed, self.__onMaxLevelMessageClosed),
         (
          self.viewModel.onUpdateContentModel, self.__onUpdateContentModel),
         (
          self.__nyController.onDataUpdated, self.__onDataUpdated),
         (
          self.__nyController.currencies.onBalanceUpdated, self.__onBalanceUpdated),
         (
          self.__nyController.onWidgetLevelUpAnimationEnd, self.__setAnimationEnd),
         (
          self.__nyController.resourceCollecting.onCollectingUpdateLock, self.__onCollectingLock),
         (
          self.__nyController.resourceCollecting.onStartCollectingAvailableAnim, self.__onCollectigAvailable),
         (
          self.__wallet.onWalletStatusChanged, self.__onWalletStatusChanged),
         (
          self.__stateObserver.onSidebarSelected, self.__onSideBarSelected),
         (
          self.__stateObserver.onExitView, self.__checkAndStopAnimation),
         (
          g_playerEvents.onDisconnected, self.__stopNotification))

    def __lockNotifications(self):
        if self.__levelUpNotificationsLock:
            return
        self.__levelUpNotificationsLock = True
        g_messengerEvents.onLockPopUpMessages(key=self.__class__.__name__, lockHigh=True)
        lockNotificationManager(lock=True, postponeActive=True, source=NY_LEVEL_UP_NOTIFICATION_LOCK_KEY)

    def __unlockNotifications(self):
        if not self.__levelUpNotificationsLock:
            return
        self.__levelUpNotificationsLock = False
        g_messengerEvents.onUnlockPopUpMessages(key=self.__class__.__name__)
        lockNotificationManager(lock=False, releasePostponed=True, source=NY_LEVEL_UP_NOTIFICATION_LOCK_KEY)

    def __onConverterOpen(self, event):
        with self.viewModel.transaction() as (model):
            model.setIsConverterOpened(True)

    def __onConverterClose(self, event):
        with self.viewModel.transaction() as (model):
            model.setIsConverterOpened(False)

    def _getListeners(self):
        return (
         (
          ObjectHoverEvent.HOVER_IN,
          self.__customizationObjectHoverIn,
          EVENT_BUS_SCOPE.DEFAULT),
         (
          ObjectHoverEvent.HOVER_OUT,
          self.__customizationObjectHoverOut,
          EVENT_BUS_SCOPE.DEFAULT),
         (
          events.NyResourcesConverterPopup.SHOW,
          self.__onConverterOpen,
          EVENT_BUS_SCOPE.DEFAULT),
         (
          events.NyResourcesConverterPopup.HIDE,
          self.__onConverterClose,
          EVENT_BUS_SCOPE.DEFAULT))

    def __onSideBarSelected(self, tabName, menuName):
        self.__hideMaxLevelReward()
        self.__currentObject = tabName
        self.__currentMenu = menuName
        self.viewModel.setIsTabSwitching(True)
        self.__clearPopovers()

    def __onUpdateContentModel(self):
        g_eventBus.handleEvent(events.HOLevelUpAnimation(events.HOLevelUpAnimation.CHANGED_VIEW, ctx={'hasChanged': False}), scope=EVENT_BUS_SCOPE.LOBBY)
        with self.viewModel.transaction() as (model):
            model.setIsTabSwitching(False)
            model.setTabName(self.__currentObject)
            self.__hoveredObjectName = None
            model.setShowCustomizationObjectTooltip(False)
            model.toySlotsBar.setHasNewToysAnimation(False)
            self.__updateSlots(fullUpdate=True, model=model)
            self.__updateResourceCollecting(model=model)
            self.__updateUpgradeInfo(model=model)
            model.setIsMaxLevelMessageClosed(AccountSettings.getUIFlag(NY_MAX_LEVEL_MESSAGE_CLOSE))
        return

    def __onDataUpdated(self, keys, diff):
        checkKeys = {SyncDataKeys.INVENTORY_TOYS,
         SyncDataKeys.SLOTS,
         SyncDataKeys.OBJECTS_LEVELS,
         SyncDataKeys.RESOURCE_COLLECTING}
        if checkKeys.intersection(set(keys)):
            with self.viewModel.transaction() as (model):
                self.__updateResourceCollecting(model=model)
                if self.__currentObject not in NYObjects.UPGRADABLE_GROUP or self.__nyController.customizationObjects.getLevel(self.__currentObject) == 0:
                    return
                self.__updateSlots(fullUpdate=False, model=model)
                self.__updateUpgradeInfo(model=model)
                if SyncDataKeys.INVENTORY_TOYS in keys:
                    if SyncDataKeys.INVENTORY_TOYS not in diff[CurrentNYConstants.PDATA_KEY]:
                        return
                    slotInventory = diff[CurrentNYConstants.PDATA_KEY][SyncDataKeys.INVENTORY_TOYS]
                    slots = diff[CurrentNYConstants.PDATA_KEY].get(SyncDataKeys.SLOTS, {})
                    if self.__hasNewToysInDiff(slotInventory, slots) and not AccountSettings.getUIFlag(NY_REWARD_KIT_OPEN):
                        self.__updateNewToys(model=model, diff=slotInventory)

    @staticmethod
    def __hasNewToysInDiff(diff, slotsDiff):
        for slotId, toys in diff.iteritems():
            for toyId, toyInfo in toys.iteritems():
                _, isUnseen, _ = toyInfo
                if slotsDiff.get(slotId, INVALID_TOY_ID) == toyId:
                    return False
                return isUnseen > 0

    def __updateSlots(self, fullUpdate, model):
        if self.__currentObject not in CustomizationObjects.ALL:
            return
        slotsData = self.__itemsCache.items.festivity.getSlotsData()
        groups = TOY_TYPES_BY_OBJECT.get(self.__currentObject, {})
        toys = self.__itemsCache.items.festivity.getToys()
        currentLevel = self.__nyController.customizationObjects.getLevel(self.__currentObject)
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
            if fullUpdate:
                groupModel.slots.clear()
            for slotIdx, slotDescr in enumerate(descrSlots):
                toyID = slotsData[slotDescr.id]
                slotType = slotDescr.type
                if toyID == INVALID_TOY_ID:
                    icon = R.images.gui.maps.icons.newYear.decoration_types.craft.dyn(slotType)()
                    isEmpty = True
                else:
                    toy = toys[slotDescr.id][toyID]
                    icon = toy.getIcon()
                    isEmpty = False
                slot = SlotModel() if fullUpdate else groupModel.slots.getItem(slotIdx)
                slot.setSlotId(slotDescr.id)
                slot.setIsEmpty(isEmpty)
                slot.setToyId(toyID)
                slot.setIcon(icon)
                slot.setUnlockLevel(slotDescr.unlockLevelID)
                slot.setIsLocked(slotDescr.unlockLevelID > currentLevel)
                slot.setIsNew(self.__nyController.checkForNewToysInSlot(slotDescr.id) and slotDescr.unlockLevelID <= currentLevel)
                if fullUpdate:
                    groupModel.slots.addViewModel(slot)

        if fullUpdate:
            model.toySlotsBar.groupSlots.invalidate()

    def __onHoverSlot(self, args):
        self.__setSlotHighlight(int(args['slotId']), True)

    def __onHoverOutSlot(self, args):
        self.__setSlotHighlight(int(args['slotId']), False)

    def __onSelectSlot(self, viewModel, args):
        selectedSlotId = int(args['slotId'])
        viewModel.setSelectedSlot(selectedSlotId)
        self.__toysList.open(selectedSlotId, viewModel)

    def __onUpdateToysAnimationEnd(self):
        with self.viewModel.transaction() as (model):
            model.toySlotsBar.setHasNewToysAnimation(False)
            currentLevel = self.__nyController.customizationObjects.getLevel(self.__currentObject)
            curObject = self.__currentObject
            if self.__totalAtmPoints == NewYearAtmospherePresenter.getTotalAtmospherePoints():
                return
            self.__totalAtmPoints = NewYearAtmospherePresenter.getTotalAtmospherePoints()
            if self.__nyController.customizationObjects.isMaxLevel(curObject, currentLevel):
                self.__showMaxLevelReward()
            else:
                model.setAnimationLevelUpState(AnimationLevelUpStates.WIDGET)
                g_eventBus.handleEvent(events.HOLevelUpAnimation(events.HOLevelUpAnimation.START), scope=EVENT_BUS_SCOPE.LOBBY)

    def __setSlotHighlight(self, slotId, isEnabled):
        if self.__hangarSpace.space is None:
            return
        else:
            customizationManager = CGF.getManager(self.__hangarSpace.spaceID, LobbyCustomizableObjectsManager)
            if customizationManager:
                customizationManager.updateSlotHighlight(slotId, isEnabled)
            return

    def __customizationObjectHoverIn(self, event):
        if self.currentTab == NYObjects.TOWN:
            self.viewModel.setShowCustomizationObjectTooltip(True)
            self.__hoveredObjectName = event.ctx.get('customizationObjectName')

    def __customizationObjectHoverOut(self, _):
        if self.currentTab == NYObjects.TOWN:
            self.viewModel.setShowCustomizationObjectTooltip(False)
            self.__hoveredObjectName = None
        return

    @replaceNoneKwargsModel
    def __updateResourceCollecting(self, model=None):
        cooldownTime = getCollectingCooldownTime()
        state = self.__getState(cooldownTime)
        model = model.resourceCollector
        model.setCollectState(state)
        model.setCooldown(cooldownTime)
        oneDayCollects = getAvgResourcesByCollecting(forceExtraCollect=False)
        manyDayCollects = getAvgResourcesByCollecting(forceExtraCollect=True)
        model.setBaseCollectAmount(oneDayCollects)
        model.setExtraCollectAmount(manyDayCollects - oneDayCollects)
        model.setSkippedDays(getSkippedDays())
        model.setIsTriggerHintAnimationShown(self.__triggerHintsController.triggerHintsState == TriggerHintsStates.RESOURCES)
        if cooldownTime > 0:
            self.__notifier.startNotification()
        else:
            self.__notifier.stopNotification()

    def __updateResourceCollectingByNotifier(self):
        if self.__resourceCollectingLock:
            return
        self.__updateResourceCollecting()

    def __stopNotification(self):
        self.__notifier.stopNotification()

    def __onCollectingLock(self, lock):
        if lock:
            self.__notifier.stopNotification()
        self.__resourceCollectingLock = True

    def __onCollectigAvailable(self):
        self.__resourceCollectingLock = False
        self.__updateResourceCollecting()

    def __getState(self, cooldownTime):
        isAvailable = isCollectingAvailable()
        isExtraAvailable = isExtraCollectingAvailable()
        eventEndTimeTill = getNYGeneralConfig().getEventEndTime() - time_utils.getServerUTCTime()
        isFinishVisited = self.__nyController.getIsResourcesFinishVisited()
        if isAvailable:
            if not self.__wallet.isAvailable:
                if isExtraAvailable:
                    state = CollectState.UNAVAILABLEEXTRA
                else:
                    state = CollectState.UNAVAILABLE
            elif isExtraAvailable:
                state = CollectState.AVAILABLEEXTRA
            else:
                state = CollectState.AVAILABLE
        elif isFinishVisited:
            state = CollectState.FINISHEDHIDDEN
        elif cooldownTime > eventEndTimeTill:
            state = CollectState.FINISHED
        else:
            state = CollectState.COLLECTED
        return state

    @wg_async
    def __onCollect(self):
        result = yield await_callback(self.__nyController.resourceCollecting.collect)()
        if result:
            self.__updateResourceCollecting()

    def __onHideFinishedStatus(self):
        self.__nyController.setIsResourcesFinishVisited(True)
        self.viewModel.resourceCollector.setCollectState(CollectState.FINISHEDHIDDEN)

    @adisp_process
    def __onLevelUp(self):
        if self.__levelUpInProgress:
            return
        self.__levelUpInProgress = True
        self.viewModel.setAnimationLevelUpState(AnimationLevelUpStates.PENDING)
        result = yield BuyObjectLevel(self.__currentObject).request()
        if result.userMsg:
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType, priority=result.msgPriority)
        if result.success and result.auxData:
            data = result.auxData
            tokens = data.get('tokens')
            objectName = data.get('objectName')
            level = data.get('level', 0)
            self.viewModel.setAnimationLevelUpState(AnimationLevelUpStates.CUSTOMIZATION)
            self.__lockNotifications()
            decorationTokens = []
            if tokens:
                tokenIDs = tokens.keys()
                decorationTokens = [ tID for tID in NYFriendServiceDataTokens.HANGAR_DECORATIONS if tID in tokenIDs ]
            toysCount = 0
            if decorationTokens and objectName in CustomizationObjects.ALL and self.__nyController.customizationObjects.isMaxLevel(objectName, level):
                slotTypes = TOY_TYPES_BY_OBJECT[objectName]
                for slotType in slotTypes:
                    slotCount = self.__nyController.getNumberOfSlotsByType(slotType)
                    toysCount += len([ toy for toy in toyCache.toys.itervalues() if toy.type == slotType and toy.dropSource == ToyDropSources.CUSTOMIZATION_OBJECTS
                                     ]) * slotCount

                SystemMessages.pushMessage(backport.text(R.strings.system_messages.newYear.objectMaxLevel.dyn(objectName)()), type=SM_TYPE.InformationHeader, priority=NotificationPriorityLevel.LOW, messageData={'header': backport.text(R.strings.system_messages.newYear.objectLevelUp.header())})
                self.__updateMaxLevelReward(objectName, level, toysCount)
                checkAndNotifyAllDecorationReceived()
            else:
                for group in data.get(CurrentNYConstants.TOYS, {}).values():
                    toysCount += sum(count for count in group.values())

                SystemMessages.pushMessage(backport.text(R.strings.system_messages.newYear.objectLevelUp.dyn(objectName)(), level=formatRomanNumber(level), items=toysCount), type=SM_TYPE.InformationHeader, priority=NotificationPriorityLevel.LOW, messageData={'header': backport.text(R.strings.system_messages.newYear.objectLevelUp.header())})
        else:
            self.viewModel.setAnimationLevelUpState(AnimationLevelUpStates.IDLE)
            self.__levelUpInProgress = False

    def __setAnimationEnd(self):
        self.__levelUpInProgress = False
        self.viewModel.setAnimationLevelUpState(AnimationLevelUpStates.IDLE)
        self.__unlockNotifications()

    def __checkAndStopAnimation(self):
        self.viewModel.toySlotsBar.setHasNewToysAnimation(False)
        if self.viewModel.getAnimationLevelUpState() is not AnimationLevelUpStates.IDLE:
            g_eventBus.handleEvent(events.HOLevelUpAnimation(events.HOLevelUpAnimation.CHANGED_VIEW, ctx={'hasChanged': True}), scope=EVENT_BUS_SCOPE.LOBBY)
            self.__setAnimationEnd()

    def __updateMaxLevelReward(self, objectID, level, toysCount):
        with self.viewModel.transaction() as (model):
            maxLevelReward = model.maxLevelReward
            maxLevelReward.setObjectType(objectID)
            maxLevelReward.setLevel(level)
            maxLevelReward.setToysCount(toysCount)

    def __showMaxLevelReward(self):
        self.viewModel.maxLevelReward.setIsVisible(True)
        cameraName = _MEGA_DECORATION_CAMERA_BY_OBJECT[NewYearNavigation.getCurrentObject()]
        self.__cameraManager.switchByCameraName(cameraName, instantly=False)

    def __onCameraSwitched(self, cameraName):
        if cameraName not in MegaDecorationsObjects.ALL():
            return
        self.viewModel.setAnimationLevelUpState(AnimationLevelUpStates.MAXLEVEL)

    def __hideMaxLevelReward(self):
        if self.viewModel.maxLevelReward.getIsVisible():
            self.viewModel.setAnimationLevelUpState(AnimationLevelUpStates.WIDGET)
            self.viewModel.maxLevelReward.setIsVisible(False)
            self.__cameraManager.switchByCameraName(NewYearNavigation.getCurrentObject(), instantly=False)
            g_eventBus.handleEvent(events.HOLevelUpAnimation(events.HOLevelUpAnimation.START), scope=EVENT_BUS_SCOPE.LOBBY)

    def __onMaxLevelRewardAccept(self):
        self.__hideMaxLevelReward()

    def __onMaxLevelMessageClosed(self):
        AccountSettings.setUIFlag(NY_MAX_LEVEL_MESSAGE_CLOSE, True)
        self.viewModel.setIsMaxLevelMessageClosed(True)

    def __clearPopovers(self):
        with self.viewModel.transaction() as (model):
            model.toySlotsBar.setSelectedSlot(-1)

    def __onSyncCompleted(self, *_):
        self.__updateResourceCollecting()

    @staticmethod
    def __onClickVideo():
        showInfoVideo()

    def __updateUpgradeInfo(self, model):
        if self.__currentObject not in NYObjects.UPGRADABLE_GROUP:
            model.setIsShowLevelUp(False)
            return
        else:
            currentLevel = self.__nyController.customizationObjects.getLevel(self.__currentObject)
            objectsConfig = self.__nyController.customizationObjects.getConfig()
            nextLevelDescr = objectsConfig.getObjectByID(self.__currentObject).getNextLevel(currentLevel)
            model.customizationLevelUp.setTargetLevel(currentLevel + 1)
            model.customizationLevelUp.setIsTriggerHintAnimationShown(self.__triggerHintsController.triggerHintsState <= TriggerHintsStates.DECORATION_ZONES)
            if nextLevelDescr is None:
                model.setIsShowLevelUp(False)
                return
            model.customizationLevelUp.setObject(self.__currentObject)
            model.setIsShowLevelUp(True)
            isEnoughToBuy = True
            pricesModel = model.customizationLevelUp.price
            pricesModel.clear()
            for currency, count in nextLevelDescr.getLevelPrice().iteritems():
                priceItem = LevelupPriceModel()
                priceItem.setCurrency(currency)
                priceItem.setValue(count)
                enoughCurrency = self.__nyController.currencies.getResouceBalance(currency) >= count
                priceItem.setIsEnough(enoughCurrency)
                pricesModel.addViewModel(priceItem)
                if not enoughCurrency:
                    isEnoughToBuy = False

            model.customizationLevelUp.setIsEnoughToBuy(isEnoughToBuy)
            pricesModel.invalidate()
            return

    def __onBalanceUpdated(self):
        with self.viewModel.transaction() as (model):
            self.__updateUpgradeInfo(model=model)

    def __updateNewToys(self, model, diff):
        groups = TOY_TYPES_BY_OBJECT.get(self.__currentObject, {})
        slots = self.__nyController.getSlotDescrs()
        newToysCount = 0
        for groupIdx, groupName in enumerate(groups):
            descrSlots = [ slot for slot in slots if slot.type == groupName ]
            groupModel = model.toySlotsBar.groupSlots.getItem(groupIdx)
            for slotIdx, slotDescr in enumerate(descrSlots):
                slot = groupModel.slots.getItem(slotIdx)
                newToys = slot.getNewToys()
                newToys.clear()
                for toyId in diff.get(slotDescr.id, []):
                    newToysCount += 1
                    newToys.addString(NewYearCurrentToyInfo(toyId).getIconName())

        if newToysCount > 0:
            model.toySlotsBar.setHasNewToysAnimation(True)

    def __onWalletStatusChanged(self, *args):
        self.__updateResourceCollecting()

    def __switchCarouselType(self, model):
        setting = self.__settingsCore.options.getSetting(settings_constants.GAME.CAROUSEL_TYPE)
        carouselTypeIndex = setting.getRowCount() - 1
        model.setCarouselType(setting.CAROUSEL_TYPES[carouselTypeIndex])