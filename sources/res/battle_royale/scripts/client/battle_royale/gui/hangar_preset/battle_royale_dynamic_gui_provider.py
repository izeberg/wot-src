from constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider
from helpers import dependency
from skeletons.gui.game_control import IPlatoonController
from battle_royale.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import BattleRoyaleLobbyHeaderHelper

class BattleRoyaleHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    __slots__ = ()
    _QUEUE_TYPE = QUEUE_TYPE.BATTLE_ROYALE
    _BONUS_TYPES = (ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO, ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD)
    _LOBBY_HEADER_HELPER = BattleRoyaleLobbyHeaderHelper
    _platoonCtrl = dependency.descriptor(IPlatoonController)

    def getSuggestedBonusType(self):
        if self._platoonCtrl.isInPlatoon():
            return ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD
        return ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO