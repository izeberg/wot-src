from gui.battle_control.controllers.hit_direction_ctrl import HitDirectionController, HitDirectionControllerPlayer
from gui.battle_control.controllers.hit_direction_ctrl.pulls import HitDamagePull

class GrinchHitDamagePull(HitDamagePull):
    _MAX_INDICATORS = 3

    @staticmethod
    def maxIndicators():
        return GrinchHitDamagePull._MAX_INDICATORS


class GrinchHitDirectionController(HitDirectionController):
    _DAMAGE_PULL_CLASS = GrinchHitDamagePull


class GrinchHitDirectionControllerPlayer(HitDirectionControllerPlayer):
    pass