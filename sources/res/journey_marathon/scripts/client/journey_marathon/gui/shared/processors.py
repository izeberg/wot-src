import logging, typing, BigWorld
from gui.shared.gui_items.processors import Processor
from helpers import dependency
from journey_marathon.jm_helpers import jmCtrl
from journey_marathon.skeletons.game_control import IJourneyMarathonController
from skeletons.gui.customization import ICustomizationService
if typing.TYPE_CHECKING:
    from typing import List
_logger = logging.getLogger(__name__)

class OpenJMNodesProcessor(Processor):
    c11n = dependency.descriptor(ICustomizationService)
    jmCtrl = dependency.descriptor(IJourneyMarathonController)

    def __init__(self, nodeIds):
        super(OpenJMNodesProcessor, self).__init__()
        self.__nodeIds = nodeIds

    def _errorHandler(self, code, errStr='', ctx=None):
        _logger.error('Failed to open node Ids=%s, errorCode=%d, errorMsg=%s', self.__nodeIds, code, errStr)
        return super(OpenJMNodesProcessor, self)._errorHandler(code, errStr, ctx)

    def _successHandler(self, code, ctx=None):
        jmCtrl().jmSysMessages.onJmNodesExplored(self.__nodeIds, ctx)
        return super(OpenJMNodesProcessor, self)._successHandler(code, ctx)

    def _request(self, callback):
        _logger.debug('Make server request to open nodes: %s', self.__nodeIds)
        BigWorld.player().JourneyMarathonAccountComponent.openJMNodeIds(self.__nodeIds, lambda code, errStr, ext: self._response(code, callback, errStr, ext))


class MoveJmCurrentNode(Processor):

    def __init__(self, nodeId):
        super(MoveJmCurrentNode, self).__init__()
        self.__nodeId = nodeId

    def _errorHandler(self, code, errStr='', ctx=None):
        _logger.error('Failed to move node Ids=%s, errorCode=%d, errorMsg=%s', self.__nodeId, code, errStr)
        return super(MoveJmCurrentNode, self)._errorHandler(code, errStr, ctx)

    def _request(self, callback):
        _logger.debug('Make server request to open nodes: %s', self.__nodeId)
        BigWorld.player().JourneyMarathonAccountComponent.moveJmCurrentNode(self.__nodeId, lambda code, errStr: self._response(code, callback, errStr))