import typing
from copy import deepcopy
from functools import partial
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_stage_model import NyStageModel, StageState, StageInfoTip
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_top_reward_model import NyTopRewardModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_weekly_rewards_view_model import NyWeeklyRewardsViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.new_year_info_view_model import Tabs
from new_year.gui.impl.lobby.new_year.tooltips.ny_common_tooltip import NyCommonTooltip, getCommonTooltipArgsFromEvent
from new_year.gui.impl.new_year.navigation import NewYearNavigation
from new_year.gui.impl.new_year.new_year_model_helper import packNyLeaderboardRewards
from new_year.gui.impl.new_year.sounds import OVERLAY_HANGAR_SOUND_SPACE
from new_year.gui.shared.event_dispatcher import showNYWeeklyRewardsViewWindow, showNyVehiclePreview
from new_year.helpers.ny_weekly_rewards_stage import getActiveSeasonId, getWeeklyStageTabIndex
from new_year.ny_constants import ViewAliases, NY_CUMULATIVE_LEADERBOARD_SEASON_ID
from new_year.skeletons.new_year import ITamagotchiDataProvider, ITamagotchiWebRequester, INewYearController, INewYearMetricsLogger
from new_year.tamagotchi.dto.config import Config
from new_year_common.items.components.ny_constants import CurrentNYConstants, NewYearObjects
from constants import CUSTOMIZATION_PROGRESS_PREFIX
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.gui_decorators import args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.shared.event_dispatcher import showHangar
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from helpers.time_utils import getServerUTCTime
from items.vehicles import getVehicleClassFromVehicleType
from shared_utils import findFirst
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array

class NewYearWeeklyRewardsView(ViewImpl):
    __slots__ = ('__tooltips', '__stageId', '__isFromMainView')
    _COMMON_SOUND_SPACE = OVERLAY_HANGAR_SOUND_SPACE
    _DEFAULT_POSITION = 0
    _NOT_HAVE_TOP_PLACE = -1
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    _webRequester = dependency.descriptor(ITamagotchiWebRequester)
    _itemsCache = dependency.descriptor(IItemsCache)
    _nyController = dependency.descriptor(INewYearController)
    _c11nService = dependency.descriptor(ICustomizationService)
    __uiLogger = dependency.descriptor(INewYearMetricsLogger)

    def __init__(self, stageId=None, isFromMainView=True):
        settings = ViewSettings(R.views.new_year.lobby.new_year.WeeklyRewardsView())
        settings.model = NyWeeklyRewardsViewModel()
        super(NewYearWeeklyRewardsView, self).__init__(settings)
        self.__tooltips = {}
        self.__stageId = stageId
        self.__isFromMainView = isFromMainView

    @property
    def viewModel(self):
        return super(NewYearWeeklyRewardsView, self).getViewModel()

    @property
    def currentSeasonId(self):
        seasons = self._dataProvider.config.seasons
        nowTime = getServerUTCTime()
        seasonAboutToStart = findFirst(lambda season: season.startTime - nowTime > 0, seasons)
        if seasonAboutToStart is None:
            return self._dataProvider.currentSeason.id + 1
        else:
            return seasonAboutToStart.id

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltips.get(tooltipId)

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(NewYearWeeklyRewardsView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if R.views.dyn('gui_lootboxes').isValid() and contentID == R.views.dyn('gui_lootboxes').lobby.gui_lootboxes.tooltips.LootboxTooltip():
            tooltipData = self.__tooltips[event.getArgument('tooltipId')]
            return tooltipData.tooltip(*tooltipData.specialArgs)
        else:
            if contentID == R.views.new_year.lobby.new_year.tooltips.CommonTooltip():
                return NyCommonTooltip(*getCommonTooltipArgsFromEvent(event))
            return

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onInfoClick, self.__onInfoClick),
         (
          self.viewModel.onPreviewClick, self.__onPreviewVehicle),
         (
          self.viewModel.onTabSelected, self.__onTabSelected),
         (
          self._dataProvider.onLeaderBoardUpdated, self.__onLeaderboardUpdated),
         (
          self._dataProvider.onPlayerStatsUpdated, self.__onPlayerStatsUpdated),
         (
          self._dataProvider.onSeasonEnded, self.__onSeasonEnded),
         (
          self._dataProvider.onNextSeasonStarted, self.__onSeasonStarted),
         (
          self._itemsCache.onSyncCompleted, self.__onInventoryUpdate))

    def _onLoading(self, *args, **kwargs):
        super(NewYearWeeklyRewardsView, self)._onLoading(*args, **kwargs)
        self.viewModel.setIsFromMainView(self.__isFromMainView)
        self.__uiLogger.logWeeklyRewardsScreenOpened()
        self.__updateModel()
        self.__makeRequestPlayerStats()
        if self.__stageId is None:
            self.__stageId = self.__getActiveStageIndex()
        self.viewModel.setCurrentStage(self.__stageId)
        return

    def __onSeasonEnded(self, seasonId):
        self.__updateModel()
        self.__updateRecalcState(seasonId)

    def __onSeasonStarted(self, _):
        self.__updateModel()

    def __onLeaderboardUpdated(self, isSuccess):
        if not isSuccess:
            return
        self.__updateModel()

    def __updateModel(self):
        with self.viewModel.transaction() as (tx):
            self.__fillModel(tx)

    def __fillModel(self, model):
        stagesModel = model.getStages()
        stagesModel.clear()
        seasons = self._dataProvider.config.seasons
        currSeasonId = self.currentSeasonId
        isRecalcPeriod = self._dataProvider.isLeaderboardRecalcPeriod
        stageNum = 1
        cumulativeSeasons = [ season for season in seasons if season.cumulative ]
        nonCumulativeSeasons = [ season for season in seasons if not season.cumulative ]
        for season in cumulativeSeasons:
            self.__appendSeasonStage(stagesModel, season, currSeasonId, stageNum, isRecalcPeriod)
            stageNum += 1

        self.__appendCumulativeStage(stagesModel)
        model.setFinalStageComplete(self._dataProvider.isCumulativeFinished)
        for season in nonCumulativeSeasons:
            self.__appendSeasonStage(stagesModel, season, currSeasonId, stageNum, isRecalcPeriod)
            stageNum += 1

        model.setIsRecalc(self._dataProvider.leaderboard.isRecalcTime)
        self.__updateReceivedTopRewards(model)
        stagesModel.invalidate()

    def __appendSeasonStage(self, stagesModel, season, currSeasonId, stageNum, isRecalcPeriod):
        stageState = self.__getStageState(season.startTime, season.endTime)
        stageModel = NyStageModel()
        stageModel.setInfoTip(self.__getStageInfoTip(season.id, stageState))
        stageModel.setId(season.id)
        stageModel.setStartDate(season.startTime)
        stageModel.setEndDate(season.endTime)
        stageModel.setState(stageState)
        stageModel.setIsFinalReward(False)
        stageModel.setStageNum(stageNum)
        stageModel.setIsRecalc(isRecalcPeriod if season.id == currSeasonId - 1 else False)
        position, topPlace = self.__getUserPositionData(season.id, stageState)
        stageModel.setPosition(position)
        stageModel.setCurrentTop(topPlace)
        self.__fillTops(stageModel, season)
        stagesModel.addViewModel(stageModel)

    def __appendCumulativeStage(self, stagesModel):
        cumulative = self._dataProvider.config.cumulative
        if cumulative is None:
            return
        else:
            stageState = self.__getStageState(cumulative.startTime, cumulative.endTime)
            stageModel = NyStageModel()
            stageModel.setInfoTip(self.__getStageInfoTip(NY_CUMULATIVE_LEADERBOARD_SEASON_ID, stageState))
            stageModel.setId(NY_CUMULATIVE_LEADERBOARD_SEASON_ID)
            stageModel.setStartDate(cumulative.startTime)
            stageModel.setEndDate(cumulative.endTime)
            stageModel.setState(stageState)
            stageModel.setIsFinalReward(True)
            stageModel.setStageNum(0)
            stageModel.setIsRecalc(self._dataProvider.cumulativeLeaderboard.isRecalcTime if self._dataProvider.cumulativeLeaderboard and self._dataProvider.cumulativeLeaderboard.updateTime else False)
            position, topPlace = self.__getUserPositionData(NY_CUMULATIVE_LEADERBOARD_SEASON_ID, stageState)
            stageModel.setPosition(position)
            stageModel.setCurrentTop(topPlace)
            self.__fillFinalReward(stageModel, cumulative, True)
            self.__fillTops(stageModel, cumulative)
            stagesModel.addViewModel(stageModel)
            return

    def __getStageInfoTip(self, seasonID, stageState):
        if self._dataProvider.isLeaderboardFinished and self._dataProvider.isCumulativeFinished:
            return StageInfoTip.LEADERBOARDCOMPLETED
        if stageState == StageState.ACTIVE:
            hasPoints = self._dataProvider.getLeaderboard(seasonID).user.points > 0
            if hasPoints:
                return StageInfoTip.ACTIVE
            return StageInfoTip.NOTENOUGHPOINTS
        if stageState == StageState.NOTSTARTED:
            return StageInfoTip.NOTSTARTED
        return StageInfoTip.FINISHED

    def __getUserPositionData(self, seasonId, stageState):
        defaultPositionData = (
         self._DEFAULT_POSITION, self._NOT_HAVE_TOP_PLACE)
        if stageState == StageState.NOTSTARTED:
            return defaultPositionData
        else:
            if stageState == StageState.FINISHED:
                playerStat = self._dataProvider.getPlayerStat(seasonId)
            else:
                playerStat = self._dataProvider.getLeaderboard(seasonId).user
            if playerStat is None:
                return defaultPositionData
            position = playerStat.position
            topPlace = self._dataProvider.getRewardedTopThreshold(seasonId, position)
            return (
             position, topPlace or self._NOT_HAVE_TOP_PLACE)

    def __fillFinalReward(self, stageModel, season, rewardState):
        if not rewardState:
            return
        else:
            finalRewardModel = stageModel.finalReward
            cumulativeStats = self._dataProvider.getPlayerCumulativeStat(NY_CUMULATIVE_LEADERBOARD_SEASON_ID)
            badgesWithTop = self.__getCumulativeBadgesWithTop(season)
            if cumulativeStats is not None:
                finalRewardModel.setIsRewarded(bool(cumulativeStats.isRewarded and cumulativeStats.rewards))
                currentTop = self._dataProvider.getRewardedTopThreshold(NY_CUMULATIVE_LEADERBOARD_SEASON_ID, cumulativeStats.position)
                finalRewardModel.setClaimedBadgeIndex(self.__getCumulativeBadgeIndex(badgesWithTop, currentTop))
            vehicleCD = self._dataProvider.getCumulativeReward()
            if vehicleCD is None:
                return
            vehicle = self._itemsCache.items.getItemByCD(vehicleCD)
            if vehicle is None:
                return
            finalRewardModel.setVehicleName(vehicle.userName)
            finalRewardModel.setVehicleLvl(vehicle.level)
            finalRewardModel.setVehicleType(getVehicleClassFromVehicleType(vehicle.descriptor.type))
            finalRewardModel.setIsElite(vehicle.isElite or vehicle.isPremium)
            finalRewardModel.setVehicleCD(vehicle.intCD)
            finalRewardModel.setRoleName(vehicle.roleLabel or '')
            badges = [ badge for _, badge in badgesWithTop ]
            packNyLeaderboardRewards({'playerBadges': badges}, finalRewardModel.badges, self.__tooltips, preserveBadgeDuplicates=True)
            return

    @staticmethod
    def __getCumulativeBadgesWithTop(cumulative):
        result = []
        for top in sorted(cumulative.topConfig, key=lambda item: item.endPos, reverse=True):
            for badge in (top.rewards or {}).get('playerBadges') or []:
                result.append((top.endPos, badge))

        return result

    @staticmethod
    def __getCumulativeBadgeIndex(badgesWithTop, currentTop):
        if currentTop <= 0:
            return -1
        for index, (topEndPos, _) in enumerate(badgesWithTop):
            if topEndPos == currentTop:
                return index

        return -1

    def __fillTops(self, stageModel, season):
        topsModel = stageModel.getTops()
        topsModel.clear()
        self.__fillDrawRewards(season, topsModel)
        self.__fillTopRewards(stageModel, season, topsModel)
        topsModel.invalidate()

    def __fillDrawRewards(self, season, topsModel):
        drawReward = season.drawReward.rewards
        topRewardModel = NyTopRewardModel()
        self.__removeReceivedProgressionStyleReward(drawReward, season)
        packNyLeaderboardRewards(drawReward, topRewardModel.rewards, self.__tooltips)
        topsModel.addViewModel(topRewardModel)

    def __fillTopRewards(self, stageModel, season, topsModel):
        nextUserTopIdx = 1
        topConfig = season.topConfig
        position = stageModel.getPosition()
        user = self._dataProvider.getLeaderboard(stageModel.getId()).user
        for i, top in enumerate(reversed(topConfig), start=len(topsModel)):
            topRewardModel = NyTopRewardModel()
            topRewardModel.setTop(top.endPos)
            if top.startPos <= position <= top.endPos:
                nextUserTopIdx = i + 1
            rewardsInTop = deepcopy(top.rewards.copy()) or {}
            self.__removeReceivedProgressionStyleReward(rewardsInTop, season)
            packNyLeaderboardRewards(rewardsInTop, topRewardModel.rewards, self.__tooltips, (
             CurrentNYConstants.NY_STATIC_DOGTAG, partial(self.__ctxUpdater, top)))
            topsModel.addViewModel(topRewardModel)

        if nextUserTopIdx < len(topsModel):
            nextTopRewardModel = topsModel[nextUserTopIdx]
            nextTopRewardModel.setPointsToTop(user.pointsByNextTop)

    def __removeReceivedProgressionStyleReward(self, rewards, season):
        tokens = rewards.get('tokens', {})
        if isinstance(season, Config.Cumulative.Dto):
            return
        if season.cumulative:
            return
        if not tokens:
            return
        tokensToRemove = []
        for tokenID in tokens:
            if tokenID.startswith(CUSTOMIZATION_PROGRESS_PREFIX):
                styleID = int(tokenID.split('_')[2])
                style = self._c11nService.getItemByID(GUI_ITEM_TYPE.STYLE, styleID)
                if style and style.isQuestsProgression and style.descriptor.questsProgression:
                    totalItems = style.descriptor.questsProgression.getTotalCount()
                    itemsOpened = sum([ style.descriptor.questsProgression.getUnlockedCount(token, self._itemsCache.items.tokens.getTokenCount(token)) for token in style.descriptor.questsProgression.getGroupTokens()
                                      ])
                    if itemsOpened >= totalItems:
                        tokensToRemove.append(tokenID)

        for tokenToRemove in tokensToRemove:
            tokens.pop(tokenToRemove)

    def __updateRecalcState(self, seasonId):
        with self.getViewModel().transaction() as (tx):
            stagesModel = tx.getStages()
            isRecalcPeriod = self._dataProvider.isLeaderboardRecalcPeriod
            tx.setIsRecalc(self._dataProvider.leaderboard.isRecalcTime)
            for stageModel in stagesModel:
                if stageModel.getId() == seasonId:
                    stageModel.setIsRecalc(isRecalcPeriod)

            stagesModel.invalidate()

    def __updateReceivedTopRewards(self, model):
        stagesModel = model.getStages()
        top = -1
        for stageModel in stagesModel:
            topsModels = stageModel.getTops()
            playerStat = self._dataProvider.getPlayerStat(stageModel.getId())
            top = self._dataProvider.getRewardedTopThreshold(stageModel.getId(), stageModel.getPosition())
            topsModel = findFirst(lambda topRewardModel: topRewardModel.getTop() == top, topsModels)
            if topsModel is None:
                continue
            isRewarded = bool(playerStat.rewards) and playerStat.isRewarded if playerStat is not None else False
            topsModel.setIsRewarded(isRewarded)
            topsModels.invalidate()

        stagesModel.invalidate()
        return

    def __onInventoryUpdate(self, _, invDiff):
        if GUI_ITEM_TYPE.VEHICLE in invDiff:
            self.__updateModel()

    @staticmethod
    def __getStageState(startTime, endTime):
        currTime = getServerUTCTime()
        if currTime < startTime:
            return StageState.NOTSTARTED
        if startTime <= currTime < endTime:
            return StageState.ACTIVE
        return StageState.FINISHED

    def __getActiveStageIndex(self):
        seasonId = getActiveSeasonId(self._dataProvider.config.seasons, getServerUTCTime(), self._dataProvider.isLeaderboardRecalcPeriod, self._dataProvider.currentSeason)
        return getWeeklyStageTabIndex(self.viewModel.getStages(), seasonId)

    def __makeRequestPlayerStats(self):
        if not self._dataProvider.raccoonState:
            return
        if not self._dataProvider.hasFinalPlayerStatsCache and self._dataProvider.canCacheFinalPlayerStats():
            self._webRequester.requestPlayerStats(forFinalCache=True)
            return
        self._webRequester.requestPlayerStats()

    def __onPlayerStatsUpdated(self, isSuccess):
        if isSuccess:
            self.__updateModel()

    def __ctxUpdater(self, top):
        return top.endPos

    @args2params(int)
    def __onPreviewVehicle(self, vehicleCD):
        callback = partial(self.__vehiclePreviewCallback, stageId=self.__stageId)
        showNyVehiclePreview(vehicleCD, previewBackCb=callback)

    @args2params(int)
    def __onTabSelected(self, id):
        self.__stageId = id

    @classmethod
    def __vehiclePreviewCallback(cls, stageId):
        if cls._dataProvider.raccoonState and cls._nyController.isInProgress():
            NewYearNavigation.switchTo(NewYearObjects.CITY_VIEW, True, ViewAliases.LEADERS_VIEW, switchCallback=partial(showNYWeeklyRewardsViewWindow, stageId=stageId, isFromMainView=False))
            return
        showHangar()

    def __onClose(self):
        self.destroyWindow()

    def __onInfoClick(self):
        self.destroyWindow()
        NewYearNavigation.showInfoView(startTab=Tabs.LEADERBOARD)


class NewYearWeeklyRewardsViewWindow(LobbyNotificationWindow):

    def __init__(self, parent=None, stageId=None, isFromMainView=True):
        super(NewYearWeeklyRewardsViewWindow, self).__init__(content=NewYearWeeklyRewardsView(stageId=stageId, isFromMainView=isFromMainView), wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, parent=parent, layer=WindowLayer.TOP_SUB_VIEW, decorator=None)
        return