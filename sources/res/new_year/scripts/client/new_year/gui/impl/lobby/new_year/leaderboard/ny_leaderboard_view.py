import typing, BigWorld
from copy import deepcopy
from gui.impl.backport import BackportTooltipWindow
from gui.impl.gen import R
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.Waiting import Waiting
from new_year.gui.shared.events import NewYearEvent
from gui.impl.gui_decorators import args2params
from helpers import dependency
from helpers.time_utils import getServerUTCTime
from helpers.CallbackDelayer import CallbackDelayer
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.new_year_info_view_model import Tabs
from new_year.helpers.server_settings import getNewYearGeneralConfig
from new_year_account_settings import getNYSetting, setNYSettings
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_leaderboard_model import NyLeaderboardModel, State, LastAction
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_player_model import NyPlayerModel, PositionType
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_tabs_model import NyTabsModel
from new_year.gui.impl.lobby.new_year.sub_model_presenter import HistorySubModelPresenter
from new_year.gui.impl.new_year.navigation import NewYearNavigation
from new_year.gui.impl.new_year.new_year_model_helper import packNyLeaderboardRewards
from new_year.ny_constants import InternalViewState, NY_LEADERBOARD_INFO_SEEN, NY_IS_LEADERBOARD_REWARDS_CHECKED, NY_IS_SECRET_REWARDS_CHECKED
from new_year_common.items.components.ny_constants import TOKEN_LOOTBOX_FRAGMENT
from new_year.skeletons.new_year import ITamagotchiWebRequester, ITamagotchiDataProvider, INewYearMetricsLogger
from new_year.gui.shared.event_dispatcher import showNYLeaderboardInfoWindow, showNYWeeklyRewardsViewWindow
from new_year.tamagotchi.sys_msg.sys_msg_handler import TamagotchiSysMsgHandler
from new_year.ny_constants import NY_CUMULATIVE_LEADERBOARD_SEASON_ID
if typing.TYPE_CHECKING:
    from new_year.tamagotchi.dto.leaderboard import Leaderboard
    from new_year.tamagotchi.dto.config import Config
_PAGE_SIZE = 50
_MIN_REQ_DELAY = 10
_HIDE_WAITING_DELAY = 30
_TAB_WEEKLY = 0
_TAB_CUMULATIVE = 1

class NewYearLeaderboardView(HistorySubModelPresenter):
    __slots__ = ('__timer', '__subviewTabIdx', '__isPrefetch', '__tooltips')
    _WAITING_NAME = 'leaderboardRewards'
    _SECRET_REWARD_NAME = 'vehicles'
    _STOP_DELAY = -1.0
    _INTERNAL_VIEW_STATE = InternalViewState.RACCOON
    _webRequester = dependency.descriptor(ITamagotchiWebRequester)
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    __uiLogger = dependency.descriptor(INewYearMetricsLogger)

    def __init__(self, viewModel, parentView, soundConfig=None):
        super(NewYearLeaderboardView, self).__init__(viewModel, parentView, soundConfig)
        self.__subviewTabIdx = _TAB_WEEKLY
        self.__timer = CallbackDelayer()
        self.__isPrefetch = False
        self.__tooltips = {}

    @property
    def isLeaderboardReady(self):
        return not self.getViewModel().getIsLoading() and not self.__isRequiredDataMissed() and self.getViewModel().getState() != State.ERROR

    @property
    def timeToNextUpdate(self):
        return max(self.__getActiveLeaderboard().nextUpdateTime + _MIN_REQ_DELAY - getServerUTCTime(), _MIN_REQ_DELAY)

    def initialize(self, *args, **kwargs):
        self.getViewModel().setState(State.INITIAL)
        self._requestUpdate(isUserPage=True)
        if not getNYSetting(NY_LEADERBOARD_INFO_SEEN):
            setNYSettings(NY_LEADERBOARD_INFO_SEEN, True)
            showNYLeaderboardInfoWindow(self.getParentWindow())
        super(NewYearLeaderboardView, self).initialize(*args, **kwargs)
        self.__uiLogger.logLeaderboardScreenOpened()

    def finalize(self):
        self.__subviewTabIdx = _TAB_WEEKLY
        self.__isPrefetch = False
        self.__tooltips = {}
        self.__timer.clearCallbacks()
        Waiting.hide(self._WAITING_NAME)
        super(NewYearLeaderboardView, self).finalize()

    def _getEvents(self):
        return (
         (
          self._nyController.onNySettingsChanged, self.__onNySettingsChanged),
         (
          self.getViewModel().onPageClick, self._onPageClick),
         (
          self.getViewModel().onTypeSelect, self.__onTypeSelect),
         (
          self.getViewModel().onPersonalPositionClick, self._onPersonalPositionClick),
         (
          self.getViewModel().onTopClick, self._onTopClick),
         (
          self.getViewModel().onInfoClick, self._onInfoClick),
         (
          self.getViewModel().onClose, self._onCloseClick),
         (
          self.getViewModel().onRewardsClick, self._onRewardsClick),
         (
          self.getViewModel().onRefresh, self._onRefresh),
         (
          self._dataProvider.onLeaderBoardUpdated, self._onLeaderBoardUpdated),
         (
          self._dataProvider.onPlayerStatsUpdated, self.__onPlayerStatsUpdated),
         (
          self._dataProvider.onSeasonEnded, self._onRefresh),
         (
          self._dataProvider.onNextSeasonStarted, self._onRefresh))

    def _getListeners(self):
        return (
         (
          NewYearEvent.ON_SWITCH_VIEW, self.__onSwitchViewEvent, EVENT_BUS_SCOPE.LOBBY),)

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltips.get(tooltipId)

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument('tooltipId')
            window = None
            if tooltipId is not None and tooltipId in self.__tooltips:
                window = BackportTooltipWindow(self.__tooltips[tooltipId], self.getParentWindow())
                window.load()
            return window
        return super(NewYearLeaderboardView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if R.views.dyn('gui_lootboxes').isValid() and contentID == R.views.dyn('gui_lootboxes').lobby.gui_lootboxes.tooltips.LootboxTooltip():
            tooltipData = self.__tooltips.get(event.getArgument('tooltipId'))
            if tooltipData is not None and tooltipData.tooltip is not None:
                return tooltipData.tooltip(*tooltipData.specialArgs)
        return

    def _onPersonalPositionClick(self):
        self._requestUpdate(isUserPage=True, actionType=LastAction.PLAYER)

    def _onPageClick(self, args):
        self._requestUpdate(args['page'], actionType=LastAction.PAGE)

    def _onInfoClick(self):
        NewYearNavigation.showInfoView(startTab=Tabs.LEADERBOARD)

    def _onTopClick(self, args):
        top = args['top']
        for reward in self.__getActiveTopConfig():
            if reward.endPos == top:
                page = int(reward.startPos / _PAGE_SIZE) + 1
                self._requestUpdate(page, actionType=LastAction.TOP)
                with self.getViewModel().transaction() as (tx):
                    tx.setCurrentTab(top)
                break

    def _onCloseClick(self):
        NewYearNavigation.closeMainView()

    def __onNySettingsChanged(self):
        config = getNewYearGeneralConfig()
        if config is not None and not config.getPetVisible():
            NewYearNavigation.closeMainView()
        return

    def _onRewardsClick(self):
        if not self.isLeaderboardReady and not Waiting.isOpened(self._WAITING_NAME):
            Waiting.show(self._WAITING_NAME, isAlwaysOnTop=True, isSingle=True)
            self.__delayedHideWaiting()
            return
        self._goToRewards()

    def _goToRewards(self):
        showNYWeeklyRewardsViewWindow(self.getParentWindow())
        setNYSettings(NY_IS_LEADERBOARD_REWARDS_CHECKED, True)
        if self.getViewModel().getIsVehicleAvailable():
            setNYSettings(NY_IS_SECRET_REWARDS_CHECKED, True)

    def _onRefresh(self, *_):
        lastRequestedPage = self.getViewModel().getCurrentPage()
        self._requestUpdate(lastRequestedPage, actionType=self.getViewModel().getLastAction())

    def _requestUpdate(self, page=0, isUserPage=False, actionType=LastAction.PLAYER):
        self.__isPrefetch = False
        self._webRequester.requestLeaderboardPage(page, isUserPage, cumulative=self.__isCumulativeTab())
        with self.getViewModel().transaction() as (tx):
            tx.setCurrentPage(page)
            tx.setLastAction(actionType)
            tx.setIsLoading(True)

    def _onLeaderBoardUpdated(self, result):
        if self.__isPrefetch:
            self.__isPrefetch = False
            if result:
                with self.getViewModel().transaction() as (tx):
                    self.__fillPersonalInfos(tx)
                self.__ensureFinishedPlayerStats()
            return
        with self.getViewModel().transaction() as (tx):
            if not result or self.__isRequiredDataMissed():
                tx.setState(State.ERROR)
                tx.setIsLoading(False)
                return
            self._updateModel(tx)
            self._updateTopTabs(tx)
            self.__runDelayedUpdate()
            self.__checkRunningWaiting()
            self.__prefetchInactiveLeaderboard()
            self.__ensureFinishedPlayerStats()

    def __onPlayerStatsUpdated(self, isSuccess):
        if isSuccess:
            self.__ensureFinishedPlayerStats()

    def __ensureFinishedPlayerStats(self):
        if not self._dataProvider.raccoonState:
            return
        if self._dataProvider.hasFinalPlayerStatsCache:
            with self.getViewModel().transaction() as (tx):
                tx.setWasInLeaderboard(self._dataProvider.wasInLeaderboard)
            return
        if not self._dataProvider.canCacheFinalPlayerStats():
            return
        self._webRequester.requestPlayerStats(forFinalCache=True)

    def _updateTopTabs(self, model):
        leaderboard = self.__getActiveLeaderboard()
        topConfig = self.__getActiveTopConfig()
        season = self._dataProvider.currentSeason
        cumulative = self._dataProvider.config.cumulative
        isNotRecalcTime = not leaderboard.isRecalcTime
        if season is not None:
            model.personalInfoWeekly.setFromTimestamp(season.startTime)
            model.personalInfoWeekly.setToTimestamp(season.endTime)
            model.personalInfoWeekly.setIsFinal(self._dataProvider.isLeaderboardFinished and isNotRecalcTime)
        if cumulative is not None:
            model.personalInfoAll.setFromTimestamp(cumulative.startTime)
            model.personalInfoAll.setToTimestamp(cumulative.endTime)
            isFinal = self._dataProvider.isLeaderboardFinished or self._dataProvider.isCumulativeFinished and isNotRecalcTime
            model.personalInfoAll.setIsFinal(isFinal)
        model.setIsFinal(self.__isActiveBoardFinished() and not self.__isRecalcActiveBoard())
        model.setIsRewardsCheck(getNYSetting(NY_IS_LEADERBOARD_REWARDS_CHECKED))
        model.setIsVehicleAvailable(self.__checkIsVehicleAvailable())
        totalPages = leaderboard.page.totalPage
        tabs = model.getTabs()
        tabs.clear()
        for item in reversed(topConfig):
            startPos = item.startPos
            endPos = item.endPos
            tab = NyTabsModel()
            tab.setTop(endPos)
            tab.setIsAvailable(totalPages * _PAGE_SIZE >= startPos)
            tabs.addViewModel(tab)

        tabs.invalidate()
        return

    def _updateModel(self, model):
        leaderboard = self.__getActiveLeaderboard()
        user = leaderboard.user
        page = leaderboard.page
        season = self._dataProvider.currentSeason
        model.setCurrentTabIdx(self.__subviewTabIdx)
        model.setUpdatedTimestamp(leaderboard.updateTime)
        model.setPagesCount(page.totalPage)
        model.setCurrentPage(page.currentPage)
        model.setStage(season.id if season is not None else 0)
        model.setPointsToTop(user.pointsByNextTop if user.position == 0 else 0)
        self.__fillPersonalInfos(model)
        model.selfRank.setPosition(user.position)
        model.selfRank.setUserName(BigWorld.player().name)
        model.selfRank.setScore(user.points)
        self.__updateLeaderboard(leaderboard, model)
        if not page.leaderboard:
            state = State.INITIAL
        else:
            state = State.RECALC if leaderboard.isRecalcTime else State.SUCCESS
        model.setState(state)
        model.setIsLoading(False)
        return

    def __fillPersonalInfos(self, model):
        weeklyTopConfig = self._dataProvider.currentSeason.topConfig if self._dataProvider.currentSeason is not None else []
        weeklyDrawReward = self._dataProvider.currentSeason.drawReward if self._dataProvider.currentSeason is not None else None
        cumulative = self._dataProvider.config.cumulative
        cumulativeTopConfig = cumulative.topConfig if cumulative is not None else []
        cumulativeDrawReward = cumulative.drawReward if cumulative is not None else None
        self.__tooltips = {}
        self.__fillPersonalInfo(model.personalInfoWeekly, self._dataProvider.leaderboard, weeklyTopConfig, weeklyDrawReward)
        self.__fillPersonalInfo(model.personalInfoAll, self._dataProvider.cumulativeLeaderboard, cumulativeTopConfig, cumulativeDrawReward)
        return

    def __fillPersonalInfo(self, infoModel, leaderboard, topConfig, drawReward):
        user = leaderboard.user
        if not (leaderboard.updateTime or user.position or user.points):
            return
        position, points = self.__getPlayerPosition(leaderboard, user)
        top, rewards = self.__resolveTopRewards(position, topConfig, drawReward)
        infoModel.setNextTopPoints(user.pointsByNextTop)
        infoModel.setOpponentPoints(user.pointsByNextPlayer)
        infoModel.setPosition(position)
        infoModel.setScore(points)
        infoModel.setTop(top)
        packNyLeaderboardRewards(deepcopy(rewards), infoModel.rewards, self.__tooltips, (
         (
          TOKEN_LOOTBOX_FRAGMENT,), infoModel.getTop))

    def __getPlayerPosition(self, leaderboard, user):
        if leaderboard is self._dataProvider.leaderboard:
            seasonFinished = self._dataProvider.isLeaderboardFinished
            seasonID = self._dataProvider.currentSeason.id if self._dataProvider.currentSeason else None
        else:
            seasonFinished = self._dataProvider.isCumulativeFinished
            seasonID = NY_CUMULATIVE_LEADERBOARD_SEASON_ID
        if not seasonFinished or seasonID is None:
            return (user.position, user.points)
        else:
            stat = self._dataProvider.getPlayerStat(seasonID)
            if stat is not None:
                return (stat.position, stat.point)
            return (
             user.position, user.points)

    @staticmethod
    def __resolveTopRewards(position, topConfig, drawReward):
        if position and topConfig:
            for top in topConfig:
                if top.startPos <= position <= top.endPos:
                    return (top.endPos, top.rewards)

        if position and drawReward and drawReward.rewards:
            return (0, drawReward.rewards)
        return (
         0, {})

    def __updateLeaderboard(self, leaderboard, model):
        user = leaderboard.user
        page = leaderboard.page
        leaderboardRows = page.leaderboard
        infoModel = model.personalInfoAll if self.__isCumulativeTab() else model.personalInfoWeekly
        rows = []
        topConfig = self.__getActiveTopConfig()
        if not leaderboardRows:
            players = model.getPlayers()
            players.clear()
            players.invalidate()
            model.setCurrentTab(topConfig[(-1)].endPos if topConfig else 0)
            return
        isSelfOnPage = False
        pID = BigWorld.player().databaseID
        for row in leaderboardRows:
            playerModel = NyPlayerModel()
            playerModel.setUserName(row.nickname)
            playerModel.setPosition(row.position)
            playerModel.setScore(row.point)
            playerModel.setPositionType(self.__getPositionType(row.upDown))
            if pID == row.spaId:
                isSelfOnPage = True
                self.__setSelfRankModel(model, row.position, row.point, self.__getPositionType(row.upDown))
            if row.position + 1 == user.position:
                infoModel.setOpponentPoints(max(row.point - user.points, 0))
            rows.append(playerModel)

        self.__updateSelfRankModel(model, user, isSelfOnPage)
        start, end = leaderboardRows[0].position, leaderboardRows[(-1)].position
        for top in reversed(topConfig):
            topStart, topEnd = top.startPos, top.endPos
            if start <= topStart <= end:
                topModel = NyPlayerModel()
                topModel.setTop(topEnd)
                topModel.setStartPos(topStart)
                topModel.setEndPos(topEnd)
                rows.insert(topStart - start, topModel)
            if topStart <= user.position <= topEnd:
                model.selfRank.setStartPos(topStart)
                model.selfRank.setEndPos(topEnd)
                model.setTop(topEnd)
                infoModel.setTop(topEnd)

        players = model.getPlayers()
        players.clear()
        for row in rows:
            players.addViewModel(row)

        players.invalidate()
        currentTab = self.__getCurrentTab(rows, model)
        model.setCurrentTab(currentTab)

    def __updateSelfRankModel(self, model, user, isSelfOnPage):
        if isSelfOnPage:
            return
        else:
            if self.__isActiveBoardFinished() and not self.__isRecalcActiveBoard():
                stat = self.__getLastSeasonStat()
                if stat is not None:
                    self.__setSelfRankModel(model, stat.position, stat.point, self.__getPositionType(user.upDown))
                    return
            self.__setSelfRankModel(model, user.position, user.points, self.__getPositionType(user.upDown))
            return

    def __setSelfRankModel(self, model, position, points, positionType):
        model.selfRank.setPositionType(positionType)
        model.selfRank.setPosition(position)
        model.selfRank.setScore(points)
        topConfig = self.__getActiveTopConfig()
        if topConfig is None:
            return
        else:
            top, _ = self.__resolveTopRewards(position, topConfig, None)
            model.selfRank.setTop(top)
            return

    def __getLastSeasonStat(self):
        if self.__subviewTabIdx == _TAB_CUMULATIVE:
            return self._dataProvider.getPlayerStat(NY_CUMULATIVE_LEADERBOARD_SEASON_ID)
        season = self._dataProvider.currentSeason
        return self._dataProvider.getPlayerStat(season.id)

    def __onSwitchViewEvent(self, event):
        switchCallback = event.ctx.kwargs.get('switchCallback')
        if switchCallback:
            switchCallback(parent=self.getParentWindow())

    @args2params(int)
    def __onTypeSelect(self, typeId):
        newTabIdx = typeId
        if newTabIdx == self.__subviewTabIdx:
            return
        self.__subviewTabIdx = newTabIdx
        self.__timer.clearCallbacks()
        with self.getViewModel().transaction() as (tx):
            tx.setCurrentTabIdx(self.__subviewTabIdx)
        cached = self.__getActiveLeaderboard()
        if cached.updateTime and cached.page.totalPage and not self.__isPrefetch:
            with self.getViewModel().transaction() as (tx):
                self._updateModel(tx)
                self._updateTopTabs(tx)
            self.__runDelayedUpdate()
            self.__ensureFinishedPlayerStats()
            return
        self._requestUpdate(isUserPage=True, actionType=LastAction.PLAYER)

    def __runDelayedUpdate(self):
        self.__timer.delayCallback(self.timeToNextUpdate, self.__timerUpdate)

    def __delayedHideWaiting(self):
        self.__timer.delayCallback(_HIDE_WAITING_DELAY, self.__hideRewardWaiting)

    def __timerUpdate(self):
        activeDone = self.__isActiveBoardFinished() and not self.__getActiveLeaderboard().isRecalcTime
        if activeDone and (not self._dataProvider.isLeaderboardFinished or self._dataProvider.hasFinalPlayerStatsCache or self._dataProvider.canCacheFinalPlayerStats()):
            return self._STOP_DELAY
        self._requestUpdate(self.getViewModel().getCurrentPage(), actionType=self.getViewModel().getLastAction())
        return self.timeToNextUpdate

    def __hideRewardWaiting(self):
        Waiting.hide(self._WAITING_NAME)
        TamagotchiSysMsgHandler.sendLeaderboardNotAvailableMessage()

    def __checkRunningWaiting(self):
        if self.isLeaderboardReady and Waiting.isOpened(self._WAITING_NAME):
            Waiting.hide(self._WAITING_NAME)
            self._goToRewards()

    def __prefetchInactiveLeaderboard(self):
        if not self._dataProvider.hasCumulativeLeaderboard:
            return
        self.__isPrefetch = True
        self._webRequester.requestLeaderboardPage(isUserPage=True, cumulative=not self.__isCumulativeTab())

    def __isCumulativeTab(self):
        return self.__subviewTabIdx == _TAB_CUMULATIVE

    def __getActiveLeaderboard(self):
        if self.__isCumulativeTab():
            return self._dataProvider.cumulativeLeaderboard
        return self._dataProvider.leaderboard

    def __getActiveTopConfig(self):
        if self.__isCumulativeTab():
            return self._dataProvider.config.cumulative.topConfig
        return self._dataProvider.currentSeason.topConfig

    def __isActiveBoardFinished(self):
        if self.__isCumulativeTab():
            return self._dataProvider.isCumulativeFinished
        return self._dataProvider.isLeaderboardFinished

    def __isRecalcActiveBoard(self):
        if self.__isCumulativeTab():
            return self._dataProvider.cumulativeLeaderboard.isRecalcTime and not self._dataProvider.isLeaderboardFinished
        return self._dataProvider.leaderboard.isRecalcTime

    def __isRequiredDataMissed(self):
        config = self._dataProvider.config
        leaderboard = self.__getActiveLeaderboard()
        if not (config and leaderboard and leaderboard.updateTime and leaderboard.user):
            return True
        if self.__isCumulativeTab():
            return not config.cumulative
        return not self._dataProvider.currentSeason

    @staticmethod
    def __getPositionType(pos):
        if pos > 0:
            return PositionType.UP
        if pos < 0:
            return PositionType.DOWN
        return PositionType.NOCHANGES

    def __getCurrentTab(self, rows, model):
        if self.getViewModel().getLastAction() == LastAction.TOP:
            return model.getCurrentTab()
        topConfig = self.__getActiveTopConfig()
        for row in rows:
            if row.getTop():
                return row.getTop()

        playerPos = 0
        for row in rows:
            if not row.getTop():
                playerPos = row.getPosition()
                break

        for top in reversed(topConfig):
            if top.startPos <= playerPos <= top.endPos:
                return top.endPos

        return topConfig[(-1)].endPos

    def __checkIsVehicleAvailable(self):
        wasRewardsChecked = getNYSetting(NY_IS_LEADERBOARD_REWARDS_CHECKED)
        wasSecretRewardsChecked = getNYSetting(NY_IS_SECRET_REWARDS_CHECKED)
        rewardSources = list(self._dataProvider.config.seasons)
        if self._dataProvider.config.cumulative is not None:
            rewardSources.append(self._dataProvider.config.cumulative)
        for source in rewardSources:
            for top in source.topConfig:
                rewards = top.rewards
                if self._SECRET_REWARD_NAME in rewards:
                    if wasRewardsChecked and not wasSecretRewardsChecked:
                        setNYSettings(NY_IS_LEADERBOARD_REWARDS_CHECKED, False)
                    return True

        return False