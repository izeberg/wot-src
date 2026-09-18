from __future__ import absolute_import
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_base_capture_indicator_model import FortRushBaseCaptureTeam
from fort_rush_common.fort_rush_constants import CAPTURE_POINT_NO_TEAM
from gui.battle_control import avatar_getter

def getTeamValue(ownersTeamId):
    if ownersTeamId == CAPTURE_POINT_NO_TEAM:
        return FortRushBaseCaptureTeam.NEUTRAL
    if avatar_getter.getPlayerTeam() == ownersTeamId:
        return FortRushBaseCaptureTeam.ALLY
    return FortRushBaseCaptureTeam.ENEMY