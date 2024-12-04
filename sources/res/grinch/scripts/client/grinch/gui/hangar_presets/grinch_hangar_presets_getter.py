from grinch_common.grinch_constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.hangar_presets.hangar_presets_getters import DefaultPresetsGetter
from grinch.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import GrinchLobbyHeaderHelper

class GrinchPresetsGetter(DefaultPresetsGetter):
    __slots__ = ()
    _QUEUE_TYPE = QUEUE_TYPE.GRINCH
    _BONUS_TYPES = (ARENA_BONUS_TYPE.GRINCH,)
    _LOBBY_HEADER_HELPER = GrinchLobbyHeaderHelper