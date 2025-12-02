import BigWorld, CGF
from GenericComponents import EntityGOSync
from cgf_script.managers_registrator import autoregister
from constants import IS_CLIENT
from helpers import dependency

def getCmpByTypeInTopMostParent(spaceID, gameObject, clazz):
    hierarchy = CGF.HierarchyManager(spaceID)
    rootGameObject = hierarchy.getTopMostParent(gameObject)
    return rootGameObject.findComponentByType(clazz)


def getVehicleFromGO(spaceID, gameObject):
    goSyncComponent = getCmpByTypeInTopMostParent(spaceID, gameObject, EntityGOSync)
    if goSyncComponent:
        return goSyncComponent.entity
    else:
        return


def registerComponentOnParams(bonusCap, disabledPerformanceGroup, domain=CGF.DomainOption.DomainAll):

    def predicate(spaceID):
        from Avatar import PlayerAvatar
        from ClientArena import ClientArena
        from grinch.skeletons.performance_analyzer import IPerformanceAnalyzer
        if not IS_CLIENT and not hasattr(BigWorld, 'player'):
            return False
        performanceAnalyzer = dependency.instance(IPerformanceAnalyzer)
        if performanceAnalyzer.getPerformanceGroup() in disabledPerformanceGroup:
            return False
        player = BigWorld.player()
        if spaceID != ClientArena.DEFAULT_ARENA_WORLD_ID and isinstance(player, PlayerAvatar):
            return player.hasBonusCap(bonusCap)
        return False

    return autoregister(presentInAllWorlds=True, creationPredicate=predicate, domain=domain)