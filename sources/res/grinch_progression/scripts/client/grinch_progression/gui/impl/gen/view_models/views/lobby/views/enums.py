from enum import Enum

class MissionTypeEnum(Enum):
    RANDOM = 'random'
    CARRIER = 'carrier'
    DEFENDER = 'defender'
    ASSAULT = 'assault'


class VehicleRole(Enum):
    CARRIER = 'carrier'
    SUPPORT = 'support'
    ASSAULT = 'assault'


class RewardRarity(Enum):
    COMMON = 'common'
    RARE = 'rare'
    EPIC = 'epic'


class RewardState(Enum):
    NOTAVAILABLE = 'notAvailable'
    AVAILABLE = 'available'
    CLAIMED = 'claimed'


class HintState(Enum):
    NONE = 'none'
    VEHICLE = 'vehicle'
    COINS = 'coins'
    BATTLE = 'battle'
    MOVE = 'move'
    MISSIONS = 'missions'
    FINISH = 'finish'