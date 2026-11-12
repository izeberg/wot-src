import typing
from helpers.time_utils import ONE_MINUTE, getServerUTCTime
from new_year.ny_constants import TamagotchiState
from new_year.tamagotchi.dto.leaderboard import Leaderboard
from new_year.tamagotchi.dto.config import Config
from new_year.tamagotchi.dto.player_info import PlayerInfo
from new_year.tamagotchi.dto.player_stats import PlayerStats
_OptDict = typing.Optional[typing.Dict]
_SeasonList = typing.List[Config.Season.Dto]
_TopConfigList = typing.List[Config.Season.TopConfig.Dto]
_CumulativeDto = typing.Optional[Config.Cumulative.Dto]

def _getUserDataSectionName(cumulative):
    if cumulative:
        return 'cumulative_leaderboard'
    return 'leaderboard'


def _readRewards(rawRewards):
    if not rawRewards:
        return {}
    return rawRewards


def _readStatRewards(rawRewards):
    if not rawRewards:
        return {}
    return _readRewards(rawRewards.get('rewards'))


def _readTopConfig(rawTops):
    result = []
    for top in rawTops:
        topDto = Config.Season.TopConfig.Dto()
        topDto.startPos = top['start_pos']
        topDto.endPos = top['end_pos']
        if 'rewards' in top:
            topDto.rewards = _readRewards(top['rewards'])
        result.append(topDto)

    return result


def _readDrawReward(giftReward, drawRewardDto):
    if giftReward is None:
        return
    else:
        drawRewardDto.count = giftReward['count']
        if 'rewards' in giftReward:
            drawRewardDto.rewards = _readRewards(giftReward['rewards'])
        return


def _readCumulativeConfig(rawCumulative, seasons, eventStartTime, eventEndTime):
    if not isinstance(rawCumulative, dict):
        return None
    else:
        cumulativeDto = Config.Cumulative.Dto()
        cumulativeDto.positionReward = rawCumulative.get('position_reward') or ''
        cumulativeDto.topConfig = _readTopConfig(rawCumulative['rewards_to_position'])
        _readDrawReward(rawCumulative.get('gift_reward'), cumulativeDto.drawReward)
        cumulativeSeasons = [ season for season in seasons if season.cumulative ]
        if cumulativeSeasons:
            cumulativeDto.startTime = rawCumulative.get('start_time', cumulativeSeasons[0].startTime)
            cumulativeDto.endTime = rawCumulative.get('end_time', cumulativeSeasons[(-1)].endTime)
            cumulativeDto.rewardTime = rawCumulative.get('reward_time', cumulativeSeasons[(-1)].rewardTime)
        else:
            cumulativeDto.startTime = rawCumulative.get('start_time', eventStartTime)
            cumulativeDto.endTime = rawCumulative.get('end_time', eventEndTime)
            cumulativeDto.rewardTime = rawCumulative.get('reward_time', cumulativeDto.endTime)
        return cumulativeDto


def _readUserData(userData, cumulative=False):
    userDto = Leaderboard.User.Dto()
    if not userData:
        return userDto
    section = userData.get(_getUserDataSectionName(cumulative))
    if not section:
        return userDto
    userDto.position = section.get('position') or 0
    userDto.points = section.get('points') or 0
    userDto.pointsByNextPlayer = section.get('points_by_next_player') or 0
    userDto.pointsByNextTop = section.get('points_by_next_top') or 0
    userDto.rewardsPlaces = section.get('rewards_places') or 0
    userDto.upDown = section.get('up_down') or 0
    if section.get('rewards'):
        userDto.rewards = _readRewards(section['rewards'])
    return userDto


def readTamagotchiLeaderboardUser(rawData, cumulative=False):
    userData = rawData.get('user_data')
    if not userData or _getUserDataSectionName(cumulative) not in userData:
        return None
    return _readUserData(userData, cumulative=cumulative)


def readTamagotchiConfig(rawData):
    result = Config.Dto()
    result.startTime = rawData['start_time']
    result.endTime = rawData['end_time']
    result.raidScalePoint = rawData['raid_scale_point']
    result.currentSeason = None
    leaderboards = rawData['leaderboards']
    now = getServerUTCTime()
    for seasonId, season in enumerate(leaderboards['seasons'], start=1):
        seasonDto = Config.Season.Dto()
        seasonDto.id = int(seasonId)
        seasonDto.rewardTime = season['reward_time']
        seasonDto.startTime = season['start_time']
        seasonDto.endTime = season['end_time']
        seasonDto.cumulative = bool(season.get('cumulative', False))
        seasonDto.resetPoints = bool(season.get('reset_points', True))
        seasonDto.positionReward = season.get('position_reward') or ''
        seasonDto.topConfig = _readTopConfig(season['rewards_to_position'])
        _readDrawReward(season.get('gift_reward'), seasonDto.drawReward)
        if seasonDto.startTime <= now <= seasonDto.endTime:
            result.currentSeason = seasonDto
        result.seasons.append(seasonDto)

    result.cumulative = _readCumulativeConfig(leaderboards.get('cumulative'), result.seasons, result.startTime, result.endTime)
    for attrName, value in rawData.get('states', {}).iteritems():
        state = Config.States.Dto()
        state.min = value['scale_sum_level_min']
        state.max = value['scale_sum_level_max']
        result.states[attrName] = state

    for attrName, value in rawData['indicators'].iteritems():
        indicator = Config.Indicators.Dto()
        indicator.maxPoints = value['maxPoint']
        result.indicators[attrName] = indicator
        for state, level in enumerate(value['levels']):
            levelDto = Config.Indicators.Level.Dto()
            levelDto.debPercent = level['debPercent']
            levelDto.degradation = level['degradation']
            levelDto.loyalty = level['loyalty']
            levelDto.points = level['point']
            levelDto.state = state
            indicator.levels.append(levelDto)

    for item in rawData['items']:
        itemDto = result.indicators[item['type']].item
        itemDto.id = item['id']
        itemDto.dynCurrencyCode = item['currency_code']
        itemDto.leaderboardPoint = item['leaderboard_point']
        itemDto.currency = item['price']['currency']
        itemDto.price = item['price']['amount']
        itemDto.scalePoint = item['scale_point']

    return result


def readTamagotchiLeaderboard(rawData, cumulative=False):
    result = Leaderboard.Dto()
    result.updateTime = rawData.get('update_time')
    if result.updateTime is None:
        result.updateTime = getServerUTCTime()
    result.nextUpdateTime = rawData.get('next_update_time')
    if result.nextUpdateTime is None:
        result.nextUpdateTime = result.updateTime + ONE_MINUTE * 5
    result.isRecalcTime = rawData.get('is_recalc_time', False)
    result.cumulative = cumulative
    pageData = rawData['page_data']
    pageDto = result.page
    pageDto.totalPage = pageData['total_page']
    pageDto.currentPage = pageData['current_page']
    for row in pageData['leaderboard']:
        rowDto = Leaderboard.Page.Row.Dto()
        rowDto.spaId = row['spa_id']
        rowDto.position = row['position']
        rowDto.point = row['point']
        rowDto.nickname = row['nickname']
        rowDto.upDown = row['up_down']
        pageDto.leaderboard.append(rowDto)

    result.user = _readUserData(rawData.get('user_data'), cumulative=cumulative)
    return result


def _readTamagotchiWeekStat(rawWeekStat):
    weekStat = PlayerStats.WeekStat.Dto()
    weekStat.week = rawWeekStat['week'] + 1
    weekStat.position = rawWeekStat['position']
    weekStat.point = rawWeekStat['point']
    weekStat.isRewarded = rawWeekStat['isRewarded']
    weekStat.rewardedDate = rawWeekStat['rewarded_date']
    weekStat.rewards = _readStatRewards(rawWeekStat.get('rewards'))
    return weekStat


def readTamagotchiPlayerInfo(rawData, lastPlayerInfo=None):
    result = PlayerInfo.Dto()
    result.state = rawData.get('state', lastPlayerInfo.state if lastPlayerInfo is not None else TamagotchiState.SAD.value)
    result.leaderboardPoint = rawData['leaderboard_point']
    result.cumulativePoint = rawData['cumulative_point']
    result.lastUpdateTime = rawData['last_update']
    result.indicators = rawData['indicators']
    for rawDebHist in rawData['deb_history']:
        hist = PlayerInfo.DebHistory.Dto()
        hist.value = rawDebHist['value']
        hist.expirationTime = rawDebHist['expired_date']
        result.debHistory.append(hist)

    return result


def readTamagotchiPlayerStats(rawData):
    result = PlayerStats.Dto()
    result.leaderboardPoint = rawData['leaderboard_point']
    for rawWeekStat in rawData['week_stats']:
        result.weekStats.append(_readTamagotchiWeekStat(rawWeekStat))

    rawCumulativeStat = rawData.get('cumulative_stat')
    if rawCumulativeStat is not None:
        result.cumulativeStats.append(_readTamagotchiWeekStat(rawCumulativeStat))
    return result