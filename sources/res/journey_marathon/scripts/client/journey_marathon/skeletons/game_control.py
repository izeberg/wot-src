from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from Event import Event
    from journey_marathon.gui.game_control.jm_components import JmConfig, JmTime, JmQuests, JmTokens, JmSwitcher, JmNodesCtrl, JmSysMessages, JmBonuses

class IJourneyMarathonController(IGameController):
    onJmFeatureStateChange = None
    onJmTimeChange = None
    onJmNodesChange = None
    onJmQuestsChange = None
    onJmTokensChange = None
    onJmConfigChange = None
    onJmConfigErrors = None
    jmConfig = None
    jmSwitcher = None
    jmNodes = None
    jmTime = None
    jmQuests = None
    jmTokens = None
    jmSysMessages = None
    jmBonuses = None