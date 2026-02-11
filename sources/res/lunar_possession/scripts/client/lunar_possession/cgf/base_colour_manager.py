import logging, BigWorld, CGF
from cgf_script.bonus_caps_rules import bonusCapsManager
from cgf_script.managers_registrator import onAddedQuery
from lunar_constants import ARENA_BONUS_TYPE_CAPS
from lunar_possession_common.cgf.general_components import TeamIDComponent
_logger = logging.getLogger(__name__)
ALLY_VISUALS = 'AllyVisuals'
ENEMY_VISUALS = 'EnemyVisuals'

@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.LUNAR_POSSESSION, CGF.DomainOption.DomainClient)
class TeamVisualsManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, TeamIDComponent)
    def onColourComponentAdded(self, go, teamIDComponent):
        player = BigWorld.player()
        if player.followTeamID == teamIDComponent.teamID:
            self.activateVisualGO(go, ALLY_VISUALS)
        else:
            self.activateVisualGO(go, ENEMY_VISUALS)

    def activateVisualGO(self, root, nameOfGameObject):
        hierarchy = CGF.HierarchyManager(self.spaceID)
        if hierarchy is None:
            return
        else:
            visualGO = hierarchy.findFirstNode(root, nameOfGameObject)
            if visualGO is None:
                _logger.debug('[Lunar][TeamVisualsManager] Activating visual: Could not find GO with name %s', nameOfGameObject)
                return
            visualGO.activate()
            return