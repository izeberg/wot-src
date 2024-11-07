import typing
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.battle_hints.queues import BattleHint

class IBattleHintsOverlapController(object):

    def fini(self):
        raise NotImplementedError

    def hintShown(self, battleHInt):
        raise NotImplementedError

    def hintHidden(self):
        raise NotImplementedError