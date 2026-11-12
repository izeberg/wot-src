import typing
from new_year.tamagotchi.dto.base import BaseDto

class Config(BaseDto):

    class Dto(BaseDto):
        __slots__ = ('startTime', 'endTime', 'raidScalePoint', 'currentSeason', 'seasons',
                     'cumulative', 'states', 'indicators')

        def __init__(self):
            super(Config.Dto, self).__init__()
            self.startTime = 0.0
            self.endTime = 0.0
            self.raidScalePoint = 0
            self.currentSeason = None
            self.seasons = list()
            self.cumulative = None
            self.states = dict()
            self.indicators = dict()
            return

    class Season(BaseDto):

        class Dto(BaseDto):
            __slots__ = ('id', 'startTime', 'endTime', 'rewardTime', 'topConfig', 'drawReward',
                         'cumulative', 'resetPoints', 'positionReward')

            def __init__(self):
                super(Config.Season.Dto, self).__init__()
                self.id = 0
                self.startTime = 0.0
                self.endTime = 0.0
                self.rewardTime = 0.0
                self.cumulative = False
                self.resetPoints = True
                self.positionReward = ''
                self.topConfig = list()
                self.drawReward = Config.Season.DrawReward.Dto()

        class TopConfig(BaseDto):

            class Dto(BaseDto):
                __slots__ = ('startPos', 'endPos', 'rewards')

                def __init__(self):
                    super(Config.Season.TopConfig.Dto, self).__init__()
                    self.startPos = 0
                    self.endPos = 0
                    self.rewards = dict()

        class DrawReward(BaseDto):

            class Dto(BaseDto):
                __slots__ = ('count', 'rewards')

                def __init__(self):
                    super(Config.Season.DrawReward.Dto, self).__init__()
                    self.count = 0
                    self.rewards = dict()

    class Cumulative(BaseDto):

        class Dto(BaseDto):
            __slots__ = ('startTime', 'endTime', 'rewardTime', 'topConfig', 'drawReward',
                         'positionReward')

            def __init__(self):
                super(Config.Cumulative.Dto, self).__init__()
                self.startTime = 0.0
                self.endTime = 0.0
                self.rewardTime = 0.0
                self.positionReward = ''
                self.topConfig = list()
                self.drawReward = Config.Season.DrawReward.Dto()

    class States(BaseDto):

        class Dto(BaseDto):
            __slots__ = ('min', 'max')

            def __init__(self):
                super(Config.States.Dto, self).__init__()
                self.min = 0
                self.max = 0

    class Indicators(BaseDto):

        class Dto(BaseDto):
            __slots__ = ('maxPoints', 'levels', 'item')

            def __init__(self):
                super(Config.Indicators.Dto, self).__init__()
                self.maxPoints = 0
                self.levels = list()
                self.item = Config.Items.Dto()

        class Level(BaseDto):

            class Dto(BaseDto):
                __slots__ = ('debPercent', 'degradation', 'loyalty', 'points', 'state')

                def __init__(self):
                    super(Config.Indicators.Level.Dto, self).__init__()
                    self.debPercent = 0.0
                    self.degradation = 0
                    self.loyalty = 0
                    self.points = 0
                    self.state = 0

    class Items(BaseDto):

        class Dto(BaseDto):
            __slots__ = ('id', 'leaderboardPoint', 'dynCurrencyCode', 'currency', 'price',
                         'scalePoint')

            def __init__(self):
                super(Config.Items.Dto, self).__init__()
                self.id = 0
                self.leaderboardPoint = 0
                self.dynCurrencyCode = ''
                self.currency = ''
                self.price = 0
                self.scalePoint = 0