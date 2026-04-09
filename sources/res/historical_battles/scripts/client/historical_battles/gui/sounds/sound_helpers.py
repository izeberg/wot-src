import typing, BigWorld
from debug_utils import LOG_WARNING
if typing.TYPE_CHECKING:
    from ArenaPhasesComponent import ArenaPhasesComponent
    from typing import Optional

def getArenaPhasesComponent():
    arenaPhasesComponent = BigWorld.player().arena.arenaInfo.dynamicComponents.get('phasesComponent')
    if not arenaPhasesComponent:
        LOG_WARNING('ArenaPhasesComponent is missing')
        return None
    else:
        return arenaPhasesComponent