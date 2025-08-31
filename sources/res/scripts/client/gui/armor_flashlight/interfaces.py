import typing
if typing.TYPE_CHECKING:
    from Math import Vector3
    from ProjectileMover import EntityCollisionData

class IArmorFlashlightBattleController(object):
    __slots__ = ()

    def updateVisibilityState(self, markerType, hitPoint, direction, collision, gunAimingCircleSize):
        raise NotImplementedError

    def hide(self):
        raise NotImplementedError

    def toggle(self):
        raise NotImplementedError