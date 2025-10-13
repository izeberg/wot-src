from battle_modifiers_common import BattleModifiers
from comp7.gui.impl.lobby.missions.missions_helpers import Comp7MissionsGuiHelper
from comp7.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import Comp7LobbyHeaderHelper
from constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

@dependency.replace_none_kwargs(comp7Controller=IComp7Controller)
def getComp7BattleModifiers(comp7Controller=None):
    return BattleModifiers(comp7Controller.battleModifiers)


class Comp7HangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.COMP7
    _BONUS_TYPES = (ARENA_BONUS_TYPE.COMP7,)
    _LOBBY_HEADER_HELPER = Comp7LobbyHeaderHelper
    _MISSIONS_HELPER = Comp7MissionsGuiHelper
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def getBattleModifiers(self):
        return getComp7BattleModifiers()