from enum import IntEnum
import typing
from helpers.statistics import HARDWARE_SCORE_PARAMS
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Optional, Dict

class LimitType(IntEnum):
    SYSTEM_DATA = 0
    HARDWARE_PARAMS = 1


class PerformanceGroup(object):
    LOW_RISK = 0
    MEDIUM_RISK = 1
    HIGH_RISK = 2
    VERY_HIGH_RISK = 3


DEFAULT_PERFORMANCE_GROUP_LIMITS = {PerformanceGroup.HIGH_RISK: [{LimitType.SYSTEM_DATA: {'osBit': 1, 'graphicsEngine': 0}}, {LimitType.HARDWARE_PARAMS: {HARDWARE_SCORE_PARAMS.PARAM_GPU_MEMORY: 490}}, {LimitType.SYSTEM_DATA: {'graphicsEngine': 0}, LimitType.HARDWARE_PARAMS: {HARDWARE_SCORE_PARAMS.PARAM_RAM: 2900}}, {LimitType.HARDWARE_PARAMS: {HARDWARE_SCORE_PARAMS.PARAM_GPU_SCORE: 800}}], PerformanceGroup.MEDIUM_RISK: [{LimitType.HARDWARE_PARAMS: {HARDWARE_SCORE_PARAMS.PARAM_GPU_SCORE: 1400}}, {LimitType.HARDWARE_PARAMS: {HARDWARE_SCORE_PARAMS.PARAM_CPU_SCORE: 50000}}]}

class IPerformanceAnalyzer(IGameController):

    def getPerformanceGroup(self, groupLimitMap=None, defaultGroup=PerformanceGroup.LOW_RISK):
        raise NotImplementedError