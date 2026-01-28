from battle_modifiers.gui.feature.modifiers_data_provider import ModifiersDataProvider
from gui.impl.lobby.stronghold.stronghold_helpers import getBattleModifiersDomain

class BattleModifiersDataProvider(ModifiersDataProvider):

    def _readClientDomain(self, modifier):
        return getBattleModifiersDomain()