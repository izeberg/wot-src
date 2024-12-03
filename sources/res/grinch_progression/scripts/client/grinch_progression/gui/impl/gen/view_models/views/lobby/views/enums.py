from enum import Enum

class VehicleRole(Enum):
    CARRIER = 'carrier'
    SUPPORT = 'support'
    ASSAULT = 'assault'


class RewardRarity(Enum):
    COMMON = 'common'
    UNCOMMON = 'uncommon'
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