from grinch_common.grinch_constants import Teams
from grinch.gui.impl.gen.view_models.views.battle.grinch_marker_model import MarkerTypeEnum
from grinch.gui.impl.gen.view_models.views.battle.team_score_model import TeamColorEnum

def getTeamColorModelData(team):
    if team == Teams.CYAN:
        return TeamColorEnum.BLUE
    if team == Teams.YELL:
        return TeamColorEnum.YELLOW
    if team == Teams.MGNT:
        return TeamColorEnum.MAGENTA
    return TeamColorEnum.NEUTRAL


def getMarkerTypeModelData(team):
    if team == Teams.CYAN:
        return MarkerTypeEnum.BLUE
    if team == Teams.YELL:
        return MarkerTypeEnum.YELLOW
    if team == Teams.MGNT:
        return MarkerTypeEnum.MAGENTA
    if team == Teams.BOTS:
        return MarkerTypeEnum.CENTRAL
    return MarkerTypeEnum.NONE