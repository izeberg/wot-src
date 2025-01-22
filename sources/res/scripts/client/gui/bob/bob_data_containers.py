from collections import namedtuple
from helpers import time_utils

class TeamSkillData(namedtuple('TeamSkillData', ('team', 'skill', 'activated_at', 'expire_at', 'count_left'))):

    def __new__(cls, **kwargs):
        defaults = dict(team=None, skill='', activated_at=0, expire_at=0, count_left=0)
        defaults.update(kwargs)
        return super(TeamSkillData, cls).__new__(cls, **defaults)

    def __cmp__(self, other):
        if other.expire_at is None:
            return -1
        else:
            if other.expire_at == 0:
                return 1
            return cmp(self.expire_at, other.expire_at)

    @property
    def timeLeft(self):
        if self.expire_at is not None:
            return max(self.expire_at - time_utils.getServerUTCTime(), 0)
        else:
            return 0

    def isActiveAt(self, timestamp):
        if self.expire_at is None or self.activated_at is None:
            return False
        return self.activated_at <= timestamp <= self.expire_at

    def asDict(self):
        return self._asdict()

    @classmethod
    def requiredFields(cls):
        return set(cls._fields) - {'count_left'}


class TeamData(namedtuple('TeamData', ('team', 'score', 'rank', 'level', 'can_join', 'correcting_coefficient'))):

    def __new__(cls, **kwargs):
        defaults = dict(team=None, score=0, rank=0, can_join=False, correcting_coefficient=None)
        defaults.update(kwargs)
        return super(TeamData, cls).__new__(cls, **defaults)

    def __cmp__(self, other):
        if cmp(self.score, other.score) == 0:
            return cmp(self.rank, other.rank)
        return cmp(self.score, other.score)

    def asDict(self):
        return self._asdict()

    @classmethod
    def requiredFields(cls):
        return set(cls._fields) - {'correcting_coefficient'}


class RecalculationData(namedtuple('RecalculationData', ('next_recalculation_timestamp', 'is_recalculating'))):

    def asDict(self):
        return self._asdict()