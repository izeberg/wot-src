from __future__ import absolute_import
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.settings import FUNCTIONAL_FLAG
from helpers.dependency import descriptor
from journey_marathon.jm_constants import JmFtState
from journey_marathon.jm_helpers import jmCtrl
from skeletons.gui.shared.utils import IHangarSpace

class JmSwitcher(object):
    __hangarSpace = descriptor(IHangarSpace)

    def __init__(self):
        self.__ftState = JmFtState.HIDDEN

    def getJmFtState(self):
        return self.__ftState

    def invalidateJmFeatureState(self):
        oldState = self.__ftState
        newState = _makeFeatureState()
        if oldState == newState:
            return
        self.__ftState = newState
        jmCtrl().onJmFeatureStateChange()


def _makeFeatureState():
    isEnabled, isSuspended = jmCtrl().jmConfig.getJmStatuses()
    if not isEnabled:
        return JmFtState.DISABLED
    if isSuspended:
        return JmFtState.PAUSED
    if not _isJmPrebattleActive():
        return JmFtState.HIDDEN
    return JmFtState.ACTIVE


def _isJmPrebattleActive():
    dispatcher = g_prbLoader.getDispatcher()
    if dispatcher:
        prbEntity = dispatcher.getEntity()
        if prbEntity:
            return bool(prbEntity.getModeFlags() & FUNCTIONAL_FLAG.RANDOM)
    return False