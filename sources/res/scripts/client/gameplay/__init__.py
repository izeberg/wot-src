from __future__ import absolute_import
__all__ = ('getGameplayConfig', )

def getGameplayConfig(manager):
    from gameplay.delegator import GameplayLogic
    from gameplay.machine import create
    from skeletons.gameplay import IGameplayLogic
    manager.addInstance(IGameplayLogic, GameplayLogic(create()), finalizer='stop')