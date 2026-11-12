import copy, typing
from shared_utils import first
from new_year.ny_constants import NY_LEADERBOARD_TANK_REWARD_STATE
from new_year_account_settings import getNYSetting, setNYSettings
if typing.TYPE_CHECKING:
    from typing import Dict, Optional, Tuple
_VEHICLE_CD = 'vehicleCD'
_REWARDS = 'rewards'
_IS_SEEN = 'isSeen'

def extractVehicleCD(rewards):
    if not rewards:
        return
    else:
        vehicles = rewards.get('vehicles')
        if not vehicles:
            return
        if isinstance(vehicles, dict):
            vehicleCD = first(vehicles.iterkeys())
            if vehicleCD is not None:
                return int(vehicleCD)
            return
        if isinstance(vehicles, (list, tuple)):
            for vehiclesDict in vehicles:
                if isinstance(vehiclesDict, dict) and vehiclesDict:
                    vehicleCD = first(vehiclesDict.iterkeys())
                    if vehicleCD is not None:
                        return int(vehicleCD)

        return


def getLeaderboardTankRewardState():
    return copy.deepcopy(getNYSetting(NY_LEADERBOARD_TANK_REWARD_STATE) or {})


def _saveState(state):
    setNYSettings(NY_LEADERBOARD_TANK_REWARD_STATE, state)


def _seasonKey(seasonId):
    return str(seasonId)


def isLeaderboardTankRewardSeen(seasonId):
    entry = getLeaderboardTankRewardState().get(_seasonKey(seasonId))
    return bool(entry and entry.get(_IS_SEEN))


def shouldShowLeaderboardTankReward(seasonId=None):
    state = getLeaderboardTankRewardState()
    if seasonId is not None:
        entry = state.get(_seasonKey(seasonId))
        return bool(entry) and not entry.get(_IS_SEEN, False)
    else:
        return any(not entry.get(_IS_SEEN, False) for entry in state.itervalues())


def getUnseenLeaderboardTankReward(seasonId=None):
    state = getLeaderboardTankRewardState()
    if seasonId is not None:
        key = _seasonKey(seasonId)
        entry = state.get(key)
        if entry and not entry.get(_IS_SEEN, False):
            return (int(key), copy.deepcopy(entry))
        return
    for key, entry in sorted(state.iteritems(), key=lambda item: int(item[0])):
        if not entry.get(_IS_SEEN, False):
            return (int(key), copy.deepcopy(entry))

    return


def registerLeaderboardTankReward(seasonId, rewards):
    vehicleCD = extractVehicleCD(rewards)
    if vehicleCD is None:
        return False
    else:
        key = _seasonKey(seasonId)
        state = getLeaderboardTankRewardState()
        existing = state.get(key)
        if existing and existing.get(_IS_SEEN):
            return False
        state[key] = {_VEHICLE_CD: vehicleCD, 
           _REWARDS: copy.deepcopy(rewards), 
           _IS_SEEN: False}
        _saveState(state)
        return True


def markLeaderboardTankRewardSeen(seasonId):
    key = _seasonKey(seasonId)
    state = getLeaderboardTankRewardState()
    entry = state.get(key)
    if entry is None:
        state[key] = {_VEHICLE_CD: None, _REWARDS: {}, _IS_SEEN: True}
    else:
        entry[_IS_SEEN] = True
        state[key] = entry
    _saveState(state)
    return