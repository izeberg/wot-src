from gui.battle_control.controllers.hit_direction_ctrl.base import HitType, IHitIndicator
from gui.battle_control.controllers.hit_direction_ctrl.ctrl import HitDirectionControllerPlayer, HitDirectionController, EpicHitDirectionController
__all__ = ('HitType', 'IHitIndicator', 'createHitDirectionController')

def createHitDirectionController(setup):
    if setup.isReplayPlaying:
        return HitDirectionControllerPlayer(setup)
    guiVisitor = setup.arenaVisitor.gui
    if guiVisitor.isInEpicRange():
        return EpicHitDirectionController(setup)
    return HitDirectionController(setup)