from white_tiger_common.wt_constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.hangar_presets.hangar_presets_getters import DefaultPresetsGetter
from helpers import dependency
from white_tiger.skeletons.white_tiger_controller import IWhiteTigerController
from white_tiger.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import WhiteTigerLobbyHeaderHelper

class WhiteTigerPresetsGetter(DefaultPresetsGetter):
    __slots__ = ()
    _QUEUE_TYPE = QUEUE_TYPE.WHITE_TIGER
    _BONUS_TYPES = (ARENA_BONUS_TYPE.WHITE_TIGER,)
    _LOBBY_HEADER_HELPER = WhiteTigerLobbyHeaderHelper
    __wtController = dependency.descriptor(IWhiteTigerController)

    def getHangarAlertBlock(self):
        self.__wtController.getAlertBlock()