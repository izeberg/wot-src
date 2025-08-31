from battle_modifiers.gui.feature.modifiers_data_provider import ModifiersDataProvider
from battle_modifiers_ext.constants_ext import GameplayImpact
from battle_modifiers.gui.impl.lobby.tooltips.modifiers_domain_tooltip_view import ModifiersDomainTooltipView
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController
COMP7_LIGHT_SEASON_MODIFIERS_DOMAIN = 'comp7LightSeasonModifiers'

class Comp7LightModifiersDomainTooltipView(ModifiersDomainTooltipView):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    def getModifiersDataProvider(self):
        return Comp7LightModifiersDataProvider(self.__comp7LightController.battleModifiers)


class Comp7LightModifiersDataProvider(ModifiersDataProvider):

    @classmethod
    def isHiddenModifier(cls, mod):
        return mod.gameplayImpact == GameplayImpact.HIDDEN

    def _readClientDomain(self, modifier):
        return COMP7_LIGHT_SEASON_MODIFIERS_DOMAIN