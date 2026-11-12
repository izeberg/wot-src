import typing
if typing.TYPE_CHECKING:
    from typing import List, Optional, Sequence
    from new_year.tamagotchi.dto.config import Config

def getLastFinishedSeason(seasons, now):
    finishedSeason = None
    for season in seasons:
        if season.endTime <= now:
            finishedSeason = season

    return finishedSeason


def getActiveSeasonId(seasons, now, isRecalcPeriod, currentSeason=None):
    if not seasons:
        return 0
    else:
        if isRecalcPeriod:
            finishedSeason = getLastFinishedSeason(seasons, now)
            if finishedSeason is not None:
                return finishedSeason.id
        for season in seasons:
            if season.startTime <= now <= season.endTime:
                return season.id

        if currentSeason is not None:
            return currentSeason.id
        return seasons[0].id


def getWeeklyStageTabIndex(stages, seasonId):
    for index, stage in enumerate(stages):
        if stage.getId() == seasonId and not stage.getIsFinalReward():
            return index

    return 0