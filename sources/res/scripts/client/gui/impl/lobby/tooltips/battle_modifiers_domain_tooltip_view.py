from battle_modifiers.gui.impl.lobby.tooltips.modifiers_domain_tooltip_view import ModifiersDomainTooltipView
from gui.impl.lobby.hangar.battle_modifiers_data_provider import BattleModifiersDataProvider
from gui.impl.lobby.stronghold.stronghold_helpers import getBattleModifiersByPrbEntity
from gui.prb_control.entities.listener import IGlobalListener

class BattleModifiersDomainTooltipView(ModifiersDomainTooltipView, IGlobalListener):

    def getModifiersDataProvider(self):
        modifiers = getBattleModifiersByPrbEntity(self.prbEntity)
        return BattleModifiersDataProvider(modifiers)