import BigWorld
from frameworks.wulf import ViewSettings, WindowLayer
from new_year.gui.impl.new_year.sounds import OVERLAY_HANGAR_SOUND_SPACE
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.ny_leaderboard_reward_view_model import NyLeaderboardRewardViewModel
from new_year.gui.impl.lobby.new_year.tooltips.ny_common_tooltip import NyCommonTooltip, getCommonTooltipArgsFromEvent
from new_year.skeletons.new_year import ITamagotchiDataProvider, ITamagotchiWebRequester
from new_year.gui.impl.new_year.new_year_model_helper import packNyLeaderboardRewards
from new_year_common.items.components.ny_constants import CurrentNYConstants
from new_year.ny_constants import NY_CUMULATIVE_LEADERBOARD_SEASON_ID
from dog_tags_common.components_config import componentConfigAdapter as cca
from dog_tags_common.config.common import ComponentViewType
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from helpers import dependency
from shared_utils import findFirst

class NyLeaderboardRewardView(ViewImpl):
    __slots__ = ('__rewards', '__seasonID', '__top', '__isRequestInProgress', '__tooltips',
                 '__isPreorder')
    _COMMON_SOUND_SPACE = OVERLAY_HANGAR_SOUND_SPACE
    __dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    __webRequester = dependency.descriptor(ITamagotchiWebRequester)

    def __init__(self, layoutID, rewards, seasonID=0, isPreorder=False):
        settings = ViewSettings(layoutID)
        settings.model = NyLeaderboardRewardViewModel()
        self.__rewards = rewards.copy()
        dogTagComponents = rewards.get('dogTagComponents')
        if dogTagComponents:
            self.__rewards['dogTagComponents'] = list(dogTagComponents)
        self.__seasonID = seasonID
        self.__top = 0
        self.__isRequestInProgress = False
        self.__tooltips = {}
        self.__isPreorder = isPreorder
        super(NyLeaderboardRewardView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyLeaderboardRewardView, self).getViewModel()

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        return self.__tooltips.get(tooltipId)

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(NyLeaderboardRewardView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if R.views.dyn('gui_lootboxes').isValid() and contentID == R.views.dyn('gui_lootboxes').lobby.gui_lootboxes.tooltips.LootboxTooltip():
            tooltipData = self.__tooltips[event.getArgument('tooltipId')]
            return tooltipData.tooltip(*tooltipData.specialArgs)
        else:
            if contentID == R.views.new_year.lobby.new_year.tooltips.CommonTooltip():
                return NyCommonTooltip(*getCommonTooltipArgsFromEvent(event))
            return

    def _getEvents(self):
        events = (
         (
          self.getViewModel().onClose, self.__onClose),)
        if not self.__isPreorder:
            events += (
             (
              self.__dataProvider.onPlayerStatsUpdated, self.__onPlayerStatsUpdated),)
        return events

    def _onLoading(self, *args, **kwargs):
        super(NyLeaderboardRewardView, self)._onLoading(*args, **kwargs)
        if self.__isPreorder:
            with self.getViewModel().transaction() as (tx):
                self.__fillModel(tx)
            return
        self.__makeRequestPlayerStats()
        with self.getViewModel().transaction() as (tx):
            self.__filterDogtags()
            if not self.__isRequestInProgress:
                self.__fillModel(tx)

    def __fillModel(self, model):
        if self.__isPreorder:
            model.setIsPreorder(True)
            packNyLeaderboardRewards(self.__rewards, model.rewards, self.__tooltips)
            return
        playerPos, playerTop = self.__getPlayerPositionAndTop()
        isFinal = self.__dataProvider.isCumulativeFinished if self.__seasonID == NY_CUMULATIVE_LEADERBOARD_SEASON_ID else self.__dataProvider.isLeaderboardFinished
        model.setStage(self.__seasonID)
        model.setPosition(playerPos)
        model.setTop(playerTop)
        model.setIsFinal(isFinal)
        packNyLeaderboardRewards(self.__rewards, model.rewards, self.__tooltips, (
         CurrentNYConstants.NY_STATIC_DOGTAG, self.__ctxUpdater))

    def __makeRequestPlayerStats(self):
        dogTagRewards = self.__rewards.get('dogTagComponents', [])
        if dogTagRewards or not self.__dataProvider.raccoonState or self.__dataProvider.hasFinalPlayerStatsCache:
            return
        self.__isRequestInProgress = True
        if self.__dataProvider.canCacheFinalPlayerStats():
            self.__webRequester.requestPlayerStats(forFinalCache=True)
        else:
            self.__webRequester.requestPlayerStats()

    def __onPlayerStatsUpdated(self, isSuccess):
        self.__isRequestInProgress = False
        with self.getViewModel().transaction() as (tx):
            self.__fillModel(tx)

    def __getPlayerPositionAndTop(self):
        dogTagRewards = self.__rewards.get('dogTagComponents', [])
        if dogTagRewards:
            return self.__getDataFromDogTag(dogTagRewards[0])
        return self.__getDataFromPlayerStats()

    def __getDataFromDogTag(self, dogTag):
        playerPos = 0
        playerTop = 0
        compId = dogTag.get('id')
        comp = cca.getComponentById(compId)
        if comp is None:
            return (playerPos, playerTop)
        else:
            componentProgress = BigWorld.player().dogTags.getComponentProgress(compId)
            playerPos = componentProgress.value
            playerGrade = componentProgress.grade
            if not comp.grades:
                return (playerPos, playerTop)
            playerTop = self.__getGrade(playerGrade, comp)
            self.__top = playerTop
            return (
             playerPos, playerTop)

    def __getDataFromPlayerStats(self):
        playerPos = -1
        playerTop = 0
        if self.__isRequestInProgress:
            return (playerPos, playerTop)
        playerStats = self.__dataProvider.playerStats
        config = self.__dataProvider.config
        if not (playerStats and config):
            return (playerPos, playerTop)
        playerPos = self.__getPlayerPos(self.__seasonID)
        top = self.__dataProvider.getRewardedTopThreshold(self.__seasonID, playerPos)
        self.__top = top if top else playerTop
        return (
         playerPos, top)

    def __getGrade(self, playerGrade, comp):
        nextGrade = playerGrade + 1
        if nextGrade >= len(comp.grades):
            return self.__getMaxGrade()
        return comp.grades[nextGrade] - 1

    def __getMaxGrade(self):
        config = self.__dataProvider.config
        if not config:
            return 0
        else:
            if self.__seasonID == NY_CUMULATIVE_LEADERBOARD_SEASON_ID:
                rewardSeason = config.cumulative
            else:
                rewardSeason = findFirst(lambda season: season.id == self.__seasonID, config.seasons)
            if rewardSeason is None or not rewardSeason.topConfig:
                return 0
            return rewardSeason.topConfig[(-1)].endPos

    def __getPlayerPos(self, seasonID):
        if seasonID == NY_CUMULATIVE_LEADERBOARD_SEASON_ID:
            cumulativeStats = None
            if self.__dataProvider.playerStats and self.__dataProvider.playerStats.cumulativeStats:
                cumulativeStats = self.__dataProvider.playerStats.cumulativeStats[0]
            if cumulativeStats is None:
                return -1
            if cumulativeStats.position == -1:
                return 0
            return cumulativeStats.position
        else:
            playerWeekStat = self.__dataProvider.getPlayerWeekStat(seasonID)
            if playerWeekStat is None:
                return -1
            if playerWeekStat.position == -1:
                return 0
            return playerWeekStat.position

    def __filterDogtags(self):
        dogTagRewards = self.__rewards.get('dogTagComponents', [])
        if dogTagRewards:
            dogTagRewards = filter(self.__isEngraving, dogTagRewards)
            self.__rewards['dogTagComponents'] = dogTagRewards

    def __isEngraving(self, dogTag):
        compId = dogTag.get('id')
        if compId is None:
            return False
        else:
            comp = cca.getComponentById(compId)
            return comp is not None and comp.viewType == ComponentViewType.ENGRAVING

    def __ctxUpdater(self):
        return int(self.__top)

    def __onClose(self):
        self.destroyWindow()


class NyLeaderboardRewardsViewWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, rewards, seasonID=0, isPreorder=False, parent=None):
        super(NyLeaderboardRewardsViewWindow, self).__init__(content=NyLeaderboardRewardView(R.views.new_year.lobby.new_year.NyLeaderboardRewardView(), rewards, seasonID, isPreorder=isPreorder), layer=WindowLayer.OVERLAY, parent=parent)