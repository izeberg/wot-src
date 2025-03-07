import constants
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags import BattleQuestsFlag
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7QuestsFlag(BattleQuestsFlag):
    __slots__ = ()
    __comp7Controller = dependency.descriptor(IComp7Controller)

    @classmethod
    def _getQuests(cls, vehicle):
        quests = super(cls, Comp7QuestsFlag)._getQuests(vehicle)
        return [ quest for quest in quests if quest.hasBonusType(constants.ARENA_BONUS_TYPE.COMP7) ]