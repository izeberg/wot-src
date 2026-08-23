from __future__ import absolute_import
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider
from white_tiger_common.wt_constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from white_tiger.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import WhiteTigerLobbyHeaderHelper

class WhiteTigerHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.WHITE_TIGER
    _BONUS_TYPES = (ARENA_BONUS_TYPE.WHITE_TIGER,)
    _LOBBY_HEADER_HELPER = WhiteTigerLobbyHeaderHelper