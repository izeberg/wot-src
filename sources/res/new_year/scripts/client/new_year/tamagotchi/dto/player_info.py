from collections import deque
import typing
from new_year.tamagotchi.dto.base import BaseDto

class PlayerInfo(BaseDto):

    class Dto(BaseDto):
        __slots__ = ('leaderboardPoint', 'lastUpdateTime', 'giftTime', 'giftCount',
                     'giftCollected', 'state', 'indicators', 'debHistory')

        def __init__(self):
            super(PlayerInfo.Dto, self).__init__()
            self.leaderboardPoint = 0.0
            self.lastUpdateTime = 0.0
            self.giftTime = 0
            self.giftCount = 0
            self.giftCollected = 0
            self.state = ''
            self.indicators = dict()
            self.debHistory = deque()

    class DebHistory(BaseDto):

        class Dto(BaseDto):
            __slots__ = ('value', 'expirationTime')

            def __init__(self):
                super(PlayerInfo.DebHistory.Dto, self).__init__()
                self.value = 0
                self.expirationTime = 0.0