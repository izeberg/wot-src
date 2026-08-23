from __future__ import absolute_import
from collections import deque
from heapq import heappush, heappop
import logging, typing
if typing.TYPE_CHECKING:
    from typing import Dict, Optional, List, Tuple
    from journey_marathon.gui.game_control.jm_components import JmNode
_logger = logging.getLogger(__name__)
_LOCK_TO_COIN_CONVERSION_NOT_IN_INVENTORY = 65536

def makeJmPathBetweenNodes(nodes, startId, finishId, lockTokenCounts):
    if not nodes or startId not in nodes or finishId not in nodes:
        _logger.error('Function called with invalid args: %s', locals())
        return
    else:
        inf = float('+inf')
        heap = [(0, startId, lockTokenCounts.copy(), [startId])]
        startState = (startId, _sortedPathInventory(lockTokenCounts))
        bestPath = {startState: 0}
        while heap:
            totalCost, nodeId, pathInventory, pathNodeIds = heappop(heap)
            state = (
             nodeId, _sortedPathInventory(pathInventory))
            if totalCost > bestPath.get(state, inf):
                continue
            if nodeId == finishId:
                return (pathNodeIds, totalCost)
            for neighbourId in nodes[nodeId].neighbours:
                if neighbourId in pathNodeIds:
                    continue
                neighbourNode = nodes[neighbourId]
                newPathInventory = pathInventory.copy()
                if neighbourNode.isExplored:
                    newCost = totalCost
                else:
                    newCost = totalCost + neighbourNode.price
                    if neighbourNode.lockedBy:
                        for lockToken in neighbourNode.lockedBy:
                            if newPathInventory.get(lockToken, 0) > 0:
                                newPathInventory[lockToken] -= 1
                                break
                        else:
                            newCost += _LOCK_TO_COIN_CONVERSION_NOT_IN_INVENTORY

                state = (
                 neighbourId, _sortedPathInventory(newPathInventory))
                if newCost < bestPath.get(state, inf):
                    bestPath[state] = newCost
                    heappush(heap, (
                     newCost, neighbourId, newPathInventory, pathNodeIds + [neighbourId]))

        return


def _sortedPathInventory(pathInventory):
    return tuple(sorted(pathInventory.items()))


def makeJmPathBetweenExploredNodes(nodes, startId, finishId):
    queue = deque([(startId, [startId])])
    visited = {startId}
    while queue:
        nodeId, path = queue.popleft()
        if nodeId == finishId:
            return path
        for neighbourId in nodes[nodeId].neighbours:
            if neighbourId in visited:
                continue
            neighbourNode = nodes[neighbourId]
            if not neighbourNode.isExplored:
                continue
            visited.add(neighbourId)
            queue.append((neighbourId, path + [neighbourId]))

    return