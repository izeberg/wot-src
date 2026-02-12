import typing
from gui.shared.event_bus import SharedEvent
if typing.TYPE_CHECKING:
    from lunar_constants import RoundEndReasonEnum

class BuffEvents(SharedEvent):
    VEHICLE_GET_BUFF = 'lunar/vehicleGetBuff'
    VEHICLE_LOSE_BUFF = 'lunar/vehicleLoseBuff'

    def __init__(self, eventType, vehicleID):
        super(BuffEvents, self).__init__(eventType)
        self.vehicleID = vehicleID


class TeamScoreEvents(SharedEvent):
    TEAM_SCORE_UPDATE = 'lunar/teamScoreUpdate'

    def __init__(self, eventType, teamScore):
        super(TeamScoreEvents, self).__init__(eventType)
        self.teamScore = teamScore


class PointZoneAnimationEvents(SharedEvent):
    VEHICLE_DELIVERED_SPIRIT = 'lunar/vehicleSpiritDelivered'
    VEHICLE_DESTROYED_WITH_SPIRIT = 'lunar/vehicleDestroyedWithSpirit'

    def __init__(self, eventType, vehicleID, animationType):
        super(PointZoneAnimationEvents, self).__init__(eventType)
        self.vehicleID = vehicleID
        self.animationType = animationType


class MatchRoundsEvents(SharedEvent):
    ROUND_START = 'lunar/onRoundStart'
    ROUND_END = 'lunar/onRoundEnd'

    def __init__(self, eventType, timer, roundEndReason=None):
        super(MatchRoundsEvents, self).__init__(eventType)
        self.timer = timer
        self.roundEndReason = roundEndReason


class PlayerScoreUpdatedEvents(SharedEvent):
    PLAYER_SCORE_UPDATED = 'lunar/playerScoreUpdated'

    def __init__(self, eventType, score):
        super(PlayerScoreUpdatedEvents, self).__init__(eventType)
        self.score = score


class SpiritEvents(SharedEvent):
    SPIRIT_SPAWNED = 'lunar/spiritSpawned'