from __future__ import absolute_import
import logging, typing
from collections import defaultdict
from PlayerEvents import g_playerEvents
from helpers_common import reprSlots
from journey_marathon.jm_constants import JmNodesUpdType, JM_TOKENS_CURRENCY_UPDATE_TYPES
from journey_marathon.jm_helpers import jmCtrl, makeJmPathBetweenNodes
from journey_marathon.jm_helpers.jm_path_finding import makeJmPathBetweenExploredNodes
from journey_marathon_common.journey_marathon_constants import JmPdataKeys as Keys
from journey_marathon_common.journey_marathon_constants import NodeType as ServerNodeType
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_node_model import NodeType as ModelNodeType
from shared_utils import findFirst
if typing.TYPE_CHECKING:
    from typing import Set, Dict, Optional, List
    from journey_marathon.gui.game_control.jm_components import JmConfig, JmTokens
    from journey_marathon.gui.game_control.jm_components.jm_configs import Position
    from journey_marathon.jm_constants import JmNodesUpdTypes, JmTokensUpdTypes
_logger = logging.getLogger(__name__)
_NODE_TYPES_MAP = {ServerNodeType.START: ModelNodeType.START, 
   ServerNodeType.SMALL: ModelNodeType.SMALL, 
   ServerNodeType.MEDIUM: ModelNodeType.MEDIUM, 
   ServerNodeType.LARGE: ModelNodeType.LARGE, 
   ServerNodeType.LOCKED: ModelNodeType.LOCKED}

class JmNode(object):
    __slots__ = ('id', 'x', 'y', 'xLore', 'yLore', 'hasLore', 'price', 'nextNodes',
                 'lockedBy', 'type', 'bonus', 'isExplored', 'path', 'prevNodes',
                 'neighbours', 'lockTokenBonus')

    def __init__(self, nodeId, node, nodePos, lorePos):
        self.id = nodeId
        self.x, self.y = nodePos
        self.hasLore = lorePos is not None
        if self.hasLore:
            self.xLore, self.yLore = lorePos
        self.price = node.get('price', 0)
        self.nextNodes = set(node.get('nodesNext', ()))
        self.lockedBy = set(node.get('lockedBy', ()))
        self.type = _NODE_TYPES_MAP[node.get('nodeType', ServerNodeType.SMALL)]
        self.bonus = node.get('bonus', {})
        self.isExplored = False
        self.prevNodes = set()
        self.neighbours = None
        self.lockTokenBonus = defaultdict(int)
        self.path = JmPath()
        return

    __repr__ = reprSlots


class JmNodesCtrl(object):

    def __init__(self):
        self.__nodes = JmNodes()
        self.__updTypes = set()
        self.__pdataJourneyId = None
        return

    def init(self):
        ctrl = jmCtrl()
        g_playerEvents.onClientUpdated += self.__onClientUpdated
        ctrl.onJmTokensChange += self.__onJmTokensChange
        ctrl.onJmConfigErrors += self.__onJmConfigErrors

    def fini(self):
        ctrl = jmCtrl()
        ctrl.onJmTokensChange -= self.__onJmTokensChange
        ctrl.onJmConfigErrors -= self.__onJmConfigErrors
        g_playerEvents.onClientUpdated -= self.__onClientUpdated
        self.__nodes.fini()
        self.__updTypes.clear()
        self.__pdataJourneyId = None
        return

    def getJmNodes(self):
        self.__nodes.updateJmNodes(self.__updTypes)
        self.__updTypes.clear()
        return self.__nodes

    def invalidateJmNodesConfig(self):
        self.__invalidate({JmNodesUpdType.CONFIG})

    def __onJmTokensChange(self, tokensUpdTypes, _):
        if tokensUpdTypes & JM_TOKENS_CURRENCY_UPDATE_TYPES:
            self.__invalidate({JmNodesUpdType.TOKENS})

    def __invalidate(self, updTypes):
        self.__updTypes |= updTypes
        jmCtrl().onJmNodesChange(frozenset(self.__updTypes))

    def __updateExploredNodes(self, progress, updTypes):
        if Keys.COMPLETED not in progress:
            return
        oldExplored = self.__nodes.getJmExploredNodeIds()
        newExplored = set(progress[Keys.COMPLETED]) | oldExplored
        if newExplored == oldExplored:
            return
        self.__nodes.setJmExploredNodeIds(newExplored)
        updTypes.add(JmNodesUpdType.EXPLORED_NODES)

    def __updateCurrentNode(self, progress, updTypes):
        if Keys.CURRENT not in progress:
            return
        oldCurrent = self.__nodes.getJmCurrNodeId()
        newCurrent = progress[Keys.CURRENT]
        if oldCurrent != newCurrent:
            self.__nodes.setJmCurrNodeId(newCurrent)
            updTypes.add(JmNodesUpdType.CURR_NODE)

    def __onClientUpdated(self, diff, _):
        if Keys.MAIN_SECTION not in diff:
            return
        main = diff[Keys.MAIN_SECTION]
        journeyId = main.get(Keys.JOURNEY_ID) or self.__pdataJourneyId or jmCtrl().jmConfig.getJmJourneyId()
        if journeyId != self.__pdataJourneyId:
            self.__pdataJourneyId = journeyId
        if Keys.PROGRESS_SECTION in main:
            progress = main[Keys.PROGRESS_SECTION]
            if journeyId in progress:
                progress = progress[journeyId]
                updTypes = set()
                self.__updateExploredNodes(progress, updTypes)
                self.__updateCurrentNode(progress, updTypes)
                if updTypes:
                    self.__invalidate(updTypes)

    def __onJmConfigErrors(self):
        self.__nodes.clear()
        self.invalidateJmNodesConfig()


class JmNodes(typing.Dict[(str, JmNode)]):

    def __init__(self):
        super(JmNodes, self).__init__()
        self.__currNodeId = None
        self.__isAllExplored = False
        self.__exploredNodeIds = set()
        return

    def fini(self):
        self.clear()
        self.__currNodeId = None
        self.__isAllExplored = False
        self.__exploredNodeIds.clear()
        return

    def clear(self):
        for nodeId in list(self):
            self.pop(nodeId).path.clear()

    def getJmCurrNodeId(self):
        return self.__currNodeId

    def setJmCurrNodeId(self, currNodeId=None):
        if currNodeId is not None:
            self.__currNodeId = currNodeId
            return
        else:
            if self.__currNodeId is None:
                currNode = findFirst(lambda n: n.type == ModelNodeType.START, self.values())
                self.__currNodeId = '' if currNode is None else currNode.id
            return

    def getJmExploredNodeIds(self):
        return self.__exploredNodeIds

    def setJmExploredNodeIds(self, exploredNodeIds):
        self.__exploredNodeIds = exploredNodeIds

    def getIsAllJmNodesExplored(self):
        return self.__isAllExplored

    def updateJmNodes(self, updTypes):
        if updTypes:
            self.__updateJmNodes(updTypes)

    def __updateJmNodes(self, updTypes):
        if updTypes == {JmNodesUpdType.CURR_NODE}:
            self.__updateExploredPaths(self.__exploredNodeIds, self.__currNodeId)
            return
        ctrl = jmCtrl()
        if JmNodesUpdType.CONFIG in updTypes:
            self.__updateFromConfig(ctrl.jmConfig)
            self.__updateNodePaths(self.__exploredNodeIds, self.__currNodeId, ctrl.jmTokens)
            return
        self.__updateNodePaths(self.__exploredNodeIds, self.__currNodeId, ctrl.jmTokens)

    def __updateFromConfig(self, config):
        self.clear()
        clientConfig = config.getJmClientConfig()
        nodesPos = clientConfig.getJmNodePositions()
        loresPos = clientConfig.getJmLorePositions()
        for nodeId, nodeInfo in config.getJmNodesConfig().items():
            nodePos = nodesPos[nodeId]
            lorePos = loresPos.get(nodeId)
            self[nodeId] = JmNode(nodeId, nodeInfo, nodePos, lorePos)

        self.setJmCurrNodeId()
        for nodeId, node in self.items():
            for nextID in node.nextNodes:
                if nextID in self:
                    self[nextID].prevNodes.add(nodeId)

        for node in self.values():
            node.neighbours = node.prevNodes | node.nextNodes

        lockTokens = jmCtrl().jmTokens.getJmLockTokens()
        for node in self.values():
            if 'tokens' in node.bonus:
                for token, tokenInfo in node.bonus['tokens'].items():
                    if token in lockTokens:
                        node.lockTokenBonus[token] += tokenInfo.get('count', 0)

    def __updateNodePaths(self, exploredNodeIds, currNodeId, jmTokens):
        lockTokenCounts = {token:cnt for token, (_, cnt) in jmTokens.getJmLockTokens().items()}
        _, __, coinTokenCount = jmTokens.getJmCoinToken()
        isAllExplored = True
        for nodeId, node in self.items():
            node.isExplored = nodeId in exploredNodeIds or node.type == ModelNodeType.START
            if not node.isExplored:
                isAllExplored = False

        self.__isAllExplored = isAllExplored
        for node in self.values():
            path = makeJmPathBetweenNodes(self, currNodeId, node.id, lockTokenCounts)
            if path is None:
                node.path.clear()
                _logger.error('Could not find bath between %s -> %s', currNodeId, node.id)
                continue
            pathNodeIds, totalCost = path
            node.path.updateJmPath(self, pathNodeIds, totalCost, lockTokenCounts, coinTokenCount)

        return

    def __updateExploredPaths(self, exploredNodeIds, currNodeId):
        for nodeId in exploredNodeIds:
            node = self[nodeId]
            node.path.clear()
            pathIds = makeJmPathBetweenExploredNodes(self, currNodeId, node.id)
            if pathIds is None:
                _logger.error('Could not find bath between %s -> %s', currNodeId, node.id)
                continue
            node.path[:] = [ self[nodeId] for nodeId in pathIds ]

        return


class JmPath(typing.List[JmNode]):

    def __init__(self):
        super(JmPath, self).__init__()
        self.coinTokenCost = 0
        self.lockTokensCost = {}
        self.totalCost = 0
        self.canAfford = True
        self.canAffordCoins = True
        self.canAffordLocks = True

    def clear(self):
        del self[:]
        self.coinTokenCost = 0
        self.lockTokensCost = {}
        self.totalCost = 0
        self.canAfford = True
        self.canAffordCoins = True
        self.canAffordLocks = True

    def updateJmPath(self, nodes, pathIds, totalCost, lockTokenCounts, coinTokenCount):
        pathNodes = [ nodes[nodeId] for nodeId in pathIds ]
        coinTokenCost = 0
        lockTokensCost = defaultdict(int)
        for node in pathNodes:
            if not node.isExplored:
                coinTokenCost += node.price
                for token in node.lockedBy:
                    lockTokensCost[token] += 1

        canAffordCoins = coinTokenCost <= coinTokenCount
        for token, lockTokenCost in lockTokensCost.items():
            if lockTokenCost > lockTokenCounts.get(token, 0):
                canAffordLocks = False
                break
        else:
            canAffordLocks = True

        self[:] = pathNodes
        self.coinTokenCost = coinTokenCost
        self.lockTokensCost = lockTokensCost
        self.totalCost = totalCost
        self.canAffordCoins = canAffordCoins
        self.canAffordLocks = canAffordLocks
        self.canAfford = canAffordCoins and canAffordLocks

    def __repr__(self):
        lockAmount = sum(self.lockTokensCost.values())
        lockCost = 0 if self.canAffordLocks else self.totalCost - self.coinTokenCost
        return 'JmPath(afford=%s, coinCost=%s, lockCost=%s, totalCost=%s, lockAmount=%s, nodeIds=%s)' % (
         self.canAfford, self.coinTokenCost, lockCost, self.totalCost, lockAmount, [ node.id for node in self ])