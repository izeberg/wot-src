from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from constants import ARENA_GUI_TYPE

class DamageLogPanelOverride(object):
    __slots__ = ('__usualObject', )
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, usualObject):
        self.__usualObject = usualObject

    def __call__(self):
        if self.sessionProvider.arenaVisitor.getArenaGuiType() in ARENA_GUI_TYPE.EPIC_RANGE:
            from gui.Scaleform.daapi.view.battle.epic.damage_log_panel import EpicDamageLogPanel
            return EpicDamageLogPanel
        return self.__usualObject