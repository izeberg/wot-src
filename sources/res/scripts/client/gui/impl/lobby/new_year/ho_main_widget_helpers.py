import typing, Event
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_widget_friend_info_model import NyWidgetFriendInfoModel, UserStatus
from gui.impl.lobby.new_year.tooltips.ny_friends_tooltip import NyFriendsTooltip
from gui.impl.lobby.new_year.tooltips.ny_main_widget_tooltip import NyMainWidgetTooltip
from gui.impl.new_year.new_year_helper import IS_ROMAN_NUMBERS_ALLOWED
from helpers import dependency, getLanguageCode
from messenger.proto.events import g_messengerEvents
from new_year.ny_constants import SyncDataKeys
from new_year.ny_level_helper import NewYearAtmospherePresenter
from ny_common.GeneralConfig import GeneralConfig
from skeletons.connection_mgr import IConnectionManager
from skeletons.new_year import INewYearController, IFriendServiceController
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.new_year.components.ny_widget_level_progress_model import NyWidgetLevelProgressModel
    from messenger.proto.xmpp.entities import XMPPUserEntity

class WidgetLevelProgressHelper(object):
    __nyController = dependency.descriptor(INewYearController)
    __friendsService = dependency.descriptor(IFriendServiceController)

    def __init__(self, model):
        super(WidgetLevelProgressHelper, self).__init__()
        self.__model = model
        self.__level = None
        self.onLevelChanged = Event.Event()
        return

    def initialize(self):
        self.__subscribe()
        self.__initWidgetModel()
        self.__updateWidgetLevel()

    def update(self):
        self.__updateHangarName()
        self.__updateWidgetLevel()

    @property
    def viewModel(self):
        return self.__model

    def clear(self):
        self.__unsubscribe()
        self.__model = None
        self.onLevelChanged.clear()
        return

    @staticmethod
    def createToolTipContent(event, contentID):
        if contentID == R.views.mono.holiday_ops.tooltips.ho_main_widget_tooltip():
            return NyMainWidgetTooltip()
        else:
            if contentID == R.views.mono.holiday_ops.tooltips.ho_friends_tooltips():
                return NyFriendsTooltip(kind=event.getArgument('type'), payload=event.getArgument('payload'))
            return

    def __getEvents(self):
        return (
         (
          self.__nyController.onDataUpdated, self.__onDataUpdated),
         (
          self.viewModel.onAnimationEnd, self.__onAnimationEnd),
         (
          self.__friendsService.onFriendHangarEnter, self.__onFriendHangarUpdate),
         (
          self.__friendsService.onFriendHangarExit, self.__onFriendHangarUpdate))

    def __initWidgetModel(self):
        maxLevel = NewYearAtmospherePresenter.getMaxLevel()
        self.__updateHangarName()
        with self.viewModel.transaction() as (model):
            model.setMaxLevel(maxLevel)
            model.setIsRomanNumbersAllowed(IS_ROMAN_NUMBERS_ALLOWED)
            model.setUserLanguage(str(getLanguageCode()).upper())

    def __updateHangarName(self):
        hangarMask = self.__nyController.getHangarNameMask()
        if hangarMask is None:
            return
        else:
            titleId, descriptionId = GeneralConfig.parseHangarNameMask(hangarMask)
            with self.viewModel.transaction() as (model):
                model.hangarName.setTitle(titleId)
                model.hangarName.setDescription(descriptionId)
            return

    def __updateWidgetLevel(self):
        level = NewYearAtmospherePresenter.getLevel()
        currentPoints, maxPoints = NewYearAtmospherePresenter.getLevelProgress()
        isLevelChanged = level != self.__level
        if isLevelChanged:
            self.__level = level
            self.onLevelChanged()
        with self.viewModel.transaction() as (model):
            if isLevelChanged:
                model.setLevel(level)
                model.setMaxPoints(maxPoints)
            model.setCurrentPoints(currentPoints)

    def __onFriendHangarUpdate(self, *_):
        self.__reset()

    def __reset(self):
        self.__initWidgetModel()
        self.__updateWidgetLevel()

    def __subscribe(self):
        for event, handler in self.__getEvents():
            event += handler

    def __unsubscribe(self):
        for event, handler in reversed(self.__getEvents()):
            event -= handler

    def __onDataUpdated(self, keys, _):
        if SyncDataKeys.POINTS in keys:
            self.__updateWidgetLevel()
        if SyncDataKeys.HANGAR_NAME_MASK in keys:
            self.__updateHangarName()

    def __onAnimationEnd(self):
        self.__nyController.setWidgetLevelUpAnimationEnd()

    def __onObjectStateChanged(self):
        self.__updateHangarName()
        self.__updateWidgetLevel()


class WidgetFriendStatusHelper(object):
    __friendsService = dependency.descriptor(IFriendServiceController)
    __connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self, model):
        super(WidgetFriendStatusHelper, self).__init__()
        self.__model = model

    def initialize(self):
        self.__subscribe()
        self.__updateWidgetModel()

    @property
    def viewModel(self):
        return self.__model

    def clear(self):
        self.__unsubscribe()
        self.__model = None
        return

    def __getEvents(self):
        return (
         (
          self.__friendsService.onFriendHangarEnter, self.__onFriendHangarUpdate),
         (
          self.__friendsService.onFriendHangarExit, self.__onFriendHangarUpdate),
         (
          g_messengerEvents.users.onUserStatusUpdated, self.__updateFriendOnlineStatus))

    def __updateWidgetModel(self):
        isInService = self.__friendsService.isInFriendHangar
        with self.viewModel.transaction() as (model):
            model.setIsShow(isInService)
            if isInService:
                spaId = self.__friendsService.friendHangarSpaId
                status = UserStatus.ONLINE if self.__friendsService.isFriendOnline(spaId) else UserStatus.OFFLINE
                model.setId(spaId)
                model.setNickname(self.__friendsService.getFriendName(spaId) or '')
                model.setServerName(self.__connectionMgr.serverUserNameShort)
                model.setUserStatus(status)

    def __onFriendHangarUpdate(self, *_):
        self.__updateWidgetModel()

    def __subscribe(self):
        for event, handler in self.__getEvents():
            event += handler

    def __unsubscribe(self):
        for event, handler in reversed(self.__getEvents()):
            event -= handler

    def __updateFriendOnlineStatus(self, user):
        with self.viewModel.transaction() as (model):
            if model.getId() == user.getID():
                model.setUserStatus(UserStatus.ONLINE if user.isOnline() else UserStatus.OFFLINE)