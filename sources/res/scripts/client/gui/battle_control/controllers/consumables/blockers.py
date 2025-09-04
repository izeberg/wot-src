import typing
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR

class IShellChangeBlocker(object):
    __slots__ = ()

    def isBlocked(self, code):
        return False


class IShotBlocker(object):
    __slots__ = ()

    def canShoot(self):
        return (
         False, CANT_SHOOT_ERROR.UNDEFINED)