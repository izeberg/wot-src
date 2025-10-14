from constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import MapsTrainingLobbyHeaderHelper
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider

class MapsTrainingHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.MAPS_TRAINING
    _BONUS_TYPES = (ARENA_BONUS_TYPE.MAPS_TRAINING,)
    _LOBBY_HEADER_HELPER = MapsTrainingLobbyHeaderHelper