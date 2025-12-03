import logging, typing, AnimationSequence, WebBrowser
from PlayerEvents import g_playerEvents
from account_helpers import AccountSettings
from account_helpers.AccountSettings import NY_FRIENDS_BANNER_SHOWN
from adisp import adisp_process
from constants import SECONDS_IN_DAY
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.views.friends.friend_model import FriendModel, UserStatus, FriendshipStatus
from gui.impl.lobby.new_year.friends.resource_box_presenter import ResourceBoxPresenter
from gui.impl.lobby.new_year.states import FriendGladeTownState, FriendGladeResourcesState, GladeTownState
from gui.shared.utils.scheduled_notifications import PeriodicNotifier
from new_year.ny_resource_collecting_helper import getAvgResourcesByCollecting, getPossibleResourcesByCollectingFromFriend
from gui.impl.lobby.new_year.tooltips.ny_friends_tooltip import NyFriendsTooltip
from gui.impl.lobby.new_year.tooltips.ny_resource_box_tooltip import NyResourceBoxTooltip
from gui.shared.utils import decorators
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from helpers import dependency, time_utils
from helpers.CallbackDelayer import CallbacksSetByID
from messenger.proto.events import g_messengerEvents
from messenger.storage import storage_getter
from ny_common.GeneralConfig import GeneralConfig
from new_year.ny_helper import getNYGeneralConfig
from realm import CURRENT_REALM
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.new_year import IFriendServiceController
from new_year.friend_service_controller import BestFriendsDataKeys, FriendsDataKeys
from gui.impl.gen.view_models.views.lobby.new_year.views.friends.ny_friends_view_model import LoadingState
from gui.impl.gen.view_models.views.lobby.new_year.views.friends.ny_friends_view_model import NyFriendsViewModel
if typing.TYPE_CHECKING:
    from messenger.proto.xmpp.entities import XMPPUserEntity
_logger = logging.getLogger(__name__)
_FRIENDSHIP_DELAY_ID = 1
_PERIODICAL_UPDATE_ID = 2
_PERIODICAL_UPDATE_TIMEOUT = time_utils.ONE_MINUTE * 5

class HOFriendsView(SubModelPresenter):
    __connectionMgr = dependency.descriptor(IConnectionManager)
    __friendsService = dependency.descriptor(IFriendServiceController)

    def __init__(self, viewModel, parentView):
        super(HOFriendsView, self).__init__(viewModel, parentView)
        self.__resourceBoxPresenter = None
        self.__delayer = CallbacksSetByID()
        self.__notifier = None
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    @storage_getter('users')
    def usersStorage(self):
        return

    def initialize(self, *args, **kwargs):
        super(HOFriendsView, self).initialize(*args, **kwargs)
        self.__requestFriendList()
        self.__resourceBoxPresenter = ResourceBoxPresenter(self.viewModel.resourceBoxModel, self)
        self.__resourceBoxPresenter.initialize()
        self.__delayer.delayCallback(_PERIODICAL_UPDATE_ID, _PERIODICAL_UPDATE_TIMEOUT, self.__periodicalUpdate)
        AnimationSequence.setEnableAnimationSequenceUpdate(False)
        WebBrowser.pauseExternalCache(True)
        self.__notifier = PeriodicNotifier(lambda : time_utils.ONE_SECOND, self.__updateFriendlyTimers, periods=(
         time_utils.ONE_SECOND,))

    def finalize(self):
        if self.__resourceBoxPresenter is not None:
            self.__resourceBoxPresenter.finalize()
            self.__resourceBoxPresenter = None
        self.__delayer.clear()
        AnimationSequence.setEnableAnimationSequenceUpdate(True)
        WebBrowser.pauseExternalCache(False)
        self.__notifier.stopNotification()
        self.__notifier.clear()
        super(HOFriendsView, self).finalize()
        return

    def createToolTipContent(self, event, contentID):
        if event.contentID == R.views.mono.holiday_ops.tooltips.ho_friends_tooltips():
            return NyFriendsTooltip(kind=event.getArgument('type'), payload=event.getArgument('payload'))
        if event.contentID == R.views.mono.holiday_ops.tooltips.ho_resource_box_tooltip():
            return NyResourceBoxTooltip(event.getArgument('isFriendsList'))
        return super(HOFriendsView, self).createToolTipContent(event, contentID)

    def createToolTip(self, event):
        if self.__resourceBoxPresenter is None:
            super(HOFriendsView, self).createToolTip(event)
        return self.__resourceBoxPresenter.createToolTip(event) or super(HOFriendsView, self).createToolTip(event)

    def _getEvents(self):
        return super(HOFriendsView, self)._getEvents() + (
         (
          self.viewModel.onGoToFriend, self.__goToFriend),
         (
          self.viewModel.onGoToCollect, self.__goToCollect),
         (
          self.viewModel.onChooseBestFriend, self.__addBestFriend),
         (
          self.viewModel.onDeleteBestFriend, self.__deleteBestFriend),
         (
          self.viewModel.onBannerChangeDisplay, self.__onBannerChangeDisplay),
         (
          self.__friendsService.onFriendServiceStateChanged, self.__onChangeFriendService),
         (
          g_messengerEvents.users.onUserActionReceived, self.__delayedRequestFriendList),
         (
          g_messengerEvents.users.onUserStatusUpdated, self.__updateFriendOnlineStatus),
         (
          g_playerEvents.onDisconnected, self.__stopNotification))

    @decorators.adisp_process()
    def __requestFriendList(self):
        if not self.isLoaded:
            return
        self.viewModel.setFriendListLoadingState(LoadingState.PENDING)
        isSuccess = yield self.__friendsService.updateFriendList()
        if not self.isLoaded:
            return
        if isSuccess:
            self.__updateAll()
            self.viewModel.setFriendListLoadingState(LoadingState.LOADED)
        else:
            self.viewModel.setFriendListLoadingState(LoadingState.FAILURE)

    def __delayedRequestFriendList(self, *args, **kwargs):
        isServiceEnabled = getNYGeneralConfig().getFriendServiceEnabled()
        if isServiceEnabled:
            delay = getNYGeneralConfig().getFriendServiceRequestDelay()
            self.__delayer.delayCallback(_FRIENDSHIP_DELAY_ID, delay, self.__requestFriendList)

    @adisp_process
    def __goToCollect(self, spaId):
        spaId = spaId.get('id')
        if spaId is None:
            _logger.info('account id is not provided from ui')
            return
        else:
            yield self.__friendsService.enterFriendHangar(spaId)
            if self.__friendsService.isInFriendHangar:
                if not self.isLoaded:
                    self.__friendsService.leaveFriendHangar()
                    return
                if getPossibleResourcesByCollectingFromFriend() > 0:
                    FriendGladeResourcesState.goTo(instantly=True)
                else:
                    FriendGladeTownState.goTo(instantly=True)
            return

    @adisp_process
    def __goToFriend(self, spaId):
        spaId = spaId.get('id')
        if spaId is None:
            _logger.info('account id is not provided from ui')
            return
        else:
            yield self.__friendsService.enterFriendHangar(spaId)
            if self.__friendsService.isInFriendHangar:
                if not self.isLoaded:
                    self.__friendsService.leaveFriendHangar()
                    return
                if len(self.viewModel.getBestFriends()) < self.viewModel.getMaxBestFriendsCount() and spaId not in self.__friendsService.bestFriendList.keys():
                    FriendGladeResourcesState.goTo(instantly=True)
                else:
                    FriendGladeTownState.goTo(instantly=True)
            return

    @decorators.adisp_process()
    def __addBestFriend(self, spaId):
        spaId = spaId.get('id')
        if spaId is None:
            _logger.info('account id is not provided from ui')
            return
        else:
            isSuccess = yield self.__friendsService.addBestFriend(spaId)
            if not self.isLoaded:
                return
            if isSuccess:
                self.__updateAll()
            return

    @decorators.adisp_process()
    def __deleteBestFriend(self, spaId):
        spaId = spaId.get('id')
        if spaId is None:
            _logger.info('account id is not provided from ui')
            return
        else:
            isSuccess = yield self.__friendsService.deleteBestFriend(spaId)
            if not self.isLoaded:
                return
            if isSuccess:
                self.__updateAll()
            return

    def __onChangeFriendService(self):
        if self.__friendsService.isServiceEnabled is False:
            GladeTownState.goTo()

    def __updateAll(self):
        with self.viewModel.transaction() as (model):
            model.setIsFinished(self.__isCollectFinished())
            self.__updateBestFriends(model)
            self.__updateFriendList(model)
            model.setRealm(CURRENT_REALM)
            model.setMaxBestFriendsCount(self.__friendsService.maxBestFriendsCount)
            model.setPossibleCollectAmount(getAvgResourcesByCollecting(forceFriend=True))
            model.setShowBanner(AccountSettings.getUIFlag(NY_FRIENDS_BANNER_SHOWN) is False)

    def __updateFriendList(self, model):
        friendList = self.__friendsService.friendList
        count = len(friendList)
        model.setTotalFriendsCount(count)
        friends = model.getFriends()
        friends.clear()
        friends.reserve(count)
        existedFriendIds = set()
        for info in friendList.itervalues():
            friendInfo = self.__makeFriendInfo(info)
            if friendInfo is not None:
                friends.addViewModel(friendInfo)
                existedFriendIds.add(friendInfo.getId())

        for spaId, bestFriendInfo in self.__friendsService.bestFriendList.iteritems():
            if bestFriendInfo[BestFriendsDataKeys.IS_REMOVED] or spaId not in existedFriendIds:
                if not bestFriendInfo[BestFriendsDataKeys.IS_REMOVED]:
                    _logger.warning('Something wrong with friend service, player %s not in friend list, but exist in best friend list with "removed" field == False', spaId)
                friend = FriendModel()
                friend.setId(spaId)
                friend.setIsRemoved(True)
                friend.setUserStatus(UserStatus.OFFLINE)
                cooldown = self.__cooldown(bestFriendInfo[BestFriendsDataKeys.RESOURCES_COOLDOWN])
                friend.setCanCollectResourcesTime(cooldown)
                if cooldown > 0:
                    friends.addViewModel(friend)
                    self.__notifier.startNotification()

        friends.invalidate()
        return

    @staticmethod
    def __cooldown(timeTill):
        cd = timeTill - time_utils.getServerUTCTime()
        if cd <= 0:
            return 0
        return cd + time_utils.ONE_MINUTE

    def __stopNotification(self):
        self.__notifier.stopNotification()

    def __updateFriendlyTimers(self):
        noneLeft = True
        with self.viewModel.transaction() as (model):
            friends = model.getFriends()
            for friendModel in friends:
                fuid = friendModel.getId()
                bestFriendInfo = self.__friendsService.bestFriendList.get(fuid, None)
                if bestFriendInfo is not None:
                    cooldown = self.__cooldown(bestFriendInfo[BestFriendsDataKeys.RESOURCES_COOLDOWN])
                    friendModel.setCanCollectResourcesTime(self.__cooldown(bestFriendInfo[BestFriendsDataKeys.RESOURCES_COOLDOWN]))
                    if cooldown > 0:
                        noneLeft = False

            friends.invalidate()
        if noneLeft:
            self.__notifier.stopNotification()
            self.__updateAll()
        return

    def __updateBestFriends(self, model):
        bestFriendList = self.__friendsService.bestFriendList
        bestFriends = model.getBestFriends()
        bestFriends.clear()
        bestFriends.reserve(len(bestFriendList))
        for info in bestFriendList.itervalues():
            if not info[BestFriendsDataKeys.IS_REMOVED] or self.__cooldown(info[BestFriendsDataKeys.RESOURCES_COOLDOWN]) > 0:
                bestFriends.addNumber(info[BestFriendsDataKeys.SPA_ID])

        bestFriends.invalidate()

    def __makeFriendInfo(self, serviceData):
        friend = FriendModel()
        spaId = serviceData[FriendsDataKeys.SPA_ID]
        if spaId is None:
            return
        else:
            friend.setId(spaId)
            friend.setNickname(self.__friendsService.getFriendName(spaId) or '')
            friend.setUserStatus(UserStatus.ONLINE if self.__friendsService.isFriendOnline(spaId) else UserStatus.OFFLINE)
            friend.setServerName(self.__connectionMgr.serverUserNameShort)
            friend.setLevel(serviceData.get(FriendsDataKeys.ATM_LEVEL, 1))
            currentPoints, toPoints = getNYGeneralConfig().getAtmosphereProgress(serviceData.get(FriendsDataKeys.ATM_POINTS, 0))
            if toPoints > 0:
                friend.setLevelProgress(float(currentPoints))
            else:
                friend.setLevelProgress(0)
            friend.setMaxLevelProgress(toPoints)
            friend.setAmountOfCollectedResources(serviceData.get(FriendsDataKeys.RESOURCES_GATHERED_BY_FRIEND, 0))
            friend.setAmountOfVisits(serviceData.get(FriendsDataKeys.HANGAR_VISITS_BY_FRIEND, 0))
            titleIdx, descriptionIdx = GeneralConfig.parseHangarNameMask(serviceData.get(FriendsDataKeys.HANGAR_NAME, 0))
            friend.hangarName.setTitle(titleIdx)
            friend.hangarName.setDescription(descriptionIdx)
            bestFriendInfo = self.__friendsService.bestFriendList.get(spaId, None)
            if bestFriendInfo is not None:
                cooldown = self.__cooldown(bestFriendInfo[BestFriendsDataKeys.RESOURCES_COOLDOWN])
                friend.setCanCollectResourcesTime(cooldown)
                if cooldown > 0:
                    self.__delayer.delayCallback(spaId, cooldown + time_utils.ONE_SECOND, self.__requestFriendList)
                    friend.setFriendshipStatus(FriendshipStatus.BEST)
                    self.__notifier.startNotification()
            else:
                friend.setFriendshipStatus(FriendshipStatus.DEFAULT)
            return friend

    def __onBannerChangeDisplay(self, spaId):
        display = spaId.get('display')
        AccountSettings.setUIFlag(NY_FRIENDS_BANNER_SHOWN, display is False)
        self.viewModel.setShowBanner(display)

    def __periodicalUpdate(self):
        self.__requestFriendList()
        self.__delayer.delayCallback(_PERIODICAL_UPDATE_ID, _PERIODICAL_UPDATE_TIMEOUT, self.__periodicalUpdate)

    def __updateFriendOnlineStatus(self, user):
        friends = self.viewModel.getFriends()
        for friendModel in friends:
            if friendModel.getId() == user.getID():
                friendModel.setUserStatus(UserStatus.ONLINE if user.isOnline() else UserStatus.OFFLINE)

        friends.invalidate()

    @dependency.replace_none_kwargs(lobbyCtx=ILobbyContext)
    def __isCollectFinished(self, lobbyCtx=None):
        serverDay = time_utils.getServerGameDay()
        eventEndDay, rest = divmod(lobbyCtx.getServerSettings().getNewYearGeneralConfig().getEventEndTime() - time_utils.getStartOfNewGameDayOffset(), SECONDS_IN_DAY)
        lastDayOfCollects = eventEndDay + (rest > 0)
        isFinished = lastDayOfCollects - serverDay <= 1
        return isFinished