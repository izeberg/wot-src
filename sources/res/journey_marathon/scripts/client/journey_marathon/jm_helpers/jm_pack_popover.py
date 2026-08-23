from __future__ import absolute_import
import logging
from itertools import chain
import typing
from gui.collection.collections_helpers import composeBonuses
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.server_events.bonuses import getMergedBonusesFromDicts
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_node_popover_model import JmNodePopoverModel
from journey_marathon.gui.shared.bonus_packers import getJMBonusPacker
from journey_marathon.jm_helpers import jmCtrl
from shared_utils import first
if typing.TYPE_CHECKING:
    from typing import Optional, Dict, Union, List
    from frameworks.wulf import Array
    from gui.impl.backport import TooltipData
    from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
    from journey_marathon.gui.game_control.jm_components.jm_nodes import JmPath, JmNodes
    TooltipsData = Dict[(str, Union[(TooltipData, List)])]
_error = logging.getLogger(__name__).error

def packJmPopover(nodeId, model, tooltips):
    nodes = jmCtrl().jmNodes.getJmNodes()
    if nodeId not in nodes:
        _error('Packing popover for invalid node = %s', nodeId)
        return
    popoverNode = nodes[nodeId]
    path = popoverNode.path
    model.setCoinTokenPrice(path.coinTokenCost)
    model.setUnlockTokenPrice(sum(path.lockTokensCost.values()))
    tooltips.clear()
    _packPathBonuses(path, model.getRewards(), tooltips)
    if path.canAffordLocks:
        return
    path = _findPathToLockReward(nodes)
    if not path:
        _error('There is no path to a node with a lock token reward')
        return
    model.setUnlockTokenNodeId(path[(-1)].id)


def _packPathBonuses(path, bonusModels, tooltips):
    rawBonuses = [ node.bonus for node in reversed(path) if node.bonus and not node.isExplored ]
    mergedBonuses = getMergedBonusesFromDicts(rawBonuses)
    splitBonuses = [ {k: v} for k, v in mergedBonuses.items() ]
    order = _determineOrder(rawBonuses)
    sortedBonuses = sorted(splitBonuses, key=lambda bonusDict: order[first(bonusDict)])
    sortedBonuses = _bringSpecialsToTheFront(sortedBonuses)
    composedBonuses = composeBonuses(sortedBonuses)
    bonusModels.clear()
    packBonusModelAndTooltipData(composedBonuses, bonusModels, tooltips, getJMBonusPacker())


def _determineOrder(bonuses):
    order = {}
    priority = 0
    for bonus in bonuses:
        for key in bonus:
            if key not in order:
                order[key] = priority
                priority += 1

    return order


def _bringSpecialsToTheFront(bonuses):
    vehicleBonuses = []
    attachmentBonuses = []
    sortedBonuses = []
    for bonus in bonuses:
        key = first(bonus)
        if key == 'vehicles':
            vehicleBonuses.append(bonus)
            continue
        if key == 'customizations':
            attachments3D = []
            customizations = bonus[key]
            for customization in customizations[:]:
                custType = customization.get('custType')
                if custType == 'attachment':
                    customizations.remove(customization)
                    attachments3D.append(customization)

            if attachments3D:
                attachmentBonuses.append({'customizations': attachments3D})
            if not customizations:
                continue
        sortedBonuses.append(bonus)

    return list(chain(vehicleBonuses, attachmentBonuses, sortedBonuses))


def _findPathToLockReward(nodes):
    minCost, minPath = float('+inf'), None
    for node in nodes.values():
        if node.lockTokenBonus and not node.isExplored and node.path.canAffordLocks and node.path.coinTokenCost < minCost:
            minCost, minPath = node.path.coinTokenCost, node.path

    return minPath