from uilogging.base.logger import MetricsLogger
from uilogging.holiday_ops.logging_constants import FEATURE, HOLogActions, HOObjects, HOParentScreens, ENVIRONMENT_STATE_MAPPING
from wotdecorators import noexcept

class HOLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(HOLogger, self).__init__(FEATURE)


class HOBalloonLogger(HOLogger):
    __slots__ = ()

    @noexcept
    def logClick(self, state):
        self.log(action=HOLogActions.CLICK, item=HOObjects.BALLOON, itemState=ENVIRONMENT_STATE_MAPPING[state], parentScreen=HOParentScreens.HANGAR)