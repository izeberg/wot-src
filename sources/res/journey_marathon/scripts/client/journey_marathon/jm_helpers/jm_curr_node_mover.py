from __future__ import absolute_import
import logging, typing, BigWorld
from adisp import adisp_process
from journey_marathon.gui.shared.processors import MoveJmCurrentNode
from journey_marathon.jm_helpers import jmCtrl
from journey_marathon_common.journey_marathon_constants import JM_CMDS_COOLDOWN
if typing.TYPE_CHECKING:
    from typing import Optional
    from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_map_view_model import JmMapViewModel
_logger = logging.getLogger(__name__)
_COOLDOWN = JM_CMDS_COOLDOWN * 1.25
_TIMEOUT = 2.0

class JmCurrNodeMover(object):

    def __init__(self):
        self.__mapViewModel = None
        self.__cooldownCBId = None
        self.__timeoutCBId = None
        self.__nodeId = None
        return

    def init(self, mapViewModel):
        self.__mapViewModel = mapViewModel

    def fini(self):
        self.__cancelCooldownCB()
        self.__cancelTimeoutCB()
        self.__mapViewModel = None
        self.__nodeId = None
        return

    def moveJmCurrNode(self, nodeId):
        if self.__validate(nodeId):
            self.__nodeId = nodeId
            self.__move()

    @adisp_process
    def __move(self):
        success = False
        self.__startCooldownCB()
        self.__startTimeoutCB()
        try:
            result = yield MoveJmCurrentNode(self.__nodeId).request()
            success = result.success
        finally:
            self.__cancelTimeoutCB()
            if not success:
                self.__error('Moving failed, reverting view state')

    def __cooldownCB(self):
        self.__cooldownCBId = None
        self.__mapViewModel.setIsInteractivityLocked(False)
        return

    def __startCooldownCB(self):
        self.__cooldownCBId = BigWorld.callback(_COOLDOWN, self.__cooldownCB)
        self.__mapViewModel.setIsInteractivityLocked(True)

    def __cancelCooldownCB(self):
        if self.__cooldownCBId is not None:
            BigWorld.cancelCallback(self.__cooldownCBId)
            self.__cooldownCBId = None
            self.__mapViewModel.setIsInteractivityLocked(False)
        return

    def __timeoutCB(self):
        self.__timeoutCBId = None
        self.__error('Moving failed no response from server')
        return

    def __startTimeoutCB(self):
        self.__cancelTimeoutCB()
        self.__timeoutCBId = BigWorld.callback(_TIMEOUT, self.__timeoutCB)

    def __cancelTimeoutCB(self):
        if self.__timeoutCBId is not None:
            BigWorld.cancelCallback(self.__timeoutCBId)
            self.__timeoutCBId = None
        return

    def __validate(self, newNodeId):
        nodes = jmCtrl().jmNodes.getJmNodes()
        if newNodeId not in nodes:
            return self.__error('NodeId not found in nodes cache %s' % newNodeId)
        else:
            oldNodeId = nodes.getJmCurrNodeId()
            if oldNodeId == newNodeId:
                return self.__error('Trying to move node to its current position %s' % newNodeId)
            newNode = nodes[newNodeId]
            if not newNode.isExplored:
                return self.__error('Trying to move current node to an unexplored node %s' % newNode)
            if self.__cooldownCBId is not None:
                return self.__error()
            return True

    def __error(self, msg=None):
        if msg:
            _logger.error(msg)
        self.__mapViewModel.setMovingFailed(True)
        return False