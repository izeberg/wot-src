from battle_royale.gui.battle_control.controllers.repository import registerBRBattleRepo
from battle_royale.gui.Scaleform import registerBRBattlePackages, registerBRLobbyPackages, registerBRTooltipsBuilders
from battle_royale.messenger.formatters import service_channel as sc
from battle_royale.gui.battle_control.controllers.equipment_items import registerBREquipmentsItems
from battle_royale.gui.hangar_presets import registerBattleRoyaleHangarPresets
from battle_royale.gui.prb_control import registerBRPrebattles
from chat_shared import SYS_MESSAGE_TYPE
from gui.shared.system_factory import registerMessengerServerFormatter
import gui.customization
from battle_royale.gui.game_control import registerBRGameControllers

def preInit():
    registerMessengerServerFormatter(SYS_MESSAGE_TYPE.battleRoyaleFreeRepair.index(), sc.BattleRoyaletSystemMessageFormatter())
    registerBRBattleRepo()
    registerBRBattlePackages()
    registerBRLobbyPackages()
    registerBRTooltipsBuilders()
    registerBRGameControllers()
    registerBREquipmentsItems()
    registerBRPrebattles()
    registerBattleRoyaleHangarPresets()


def init():
    pass


def start():
    pass


def fini():
    pass