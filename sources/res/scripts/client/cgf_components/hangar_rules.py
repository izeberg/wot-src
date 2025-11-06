import CGF
from cgf_script.managers_registrator import Rule, registerManager, registerRule
from gui.pet_system.cgf_components.pet_place_component import PetPrefabManager
from hover_component import HoverManager
from highlight_component import HighlightManager
from hover_group_components import HoverGroupManager
from on_click_components import ClickManager

@registerRule
class SelectionRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(HoverManager)
    def reg1(self):
        return

    @registerManager(HighlightManager)
    def reg2(self):
        return

    @registerManager(ClickManager)
    def reg3(self):
        return

    @registerManager(HoverGroupManager)
    def reg4(self):
        return


@registerRule
class PetPlaceRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(PetPrefabManager)
    def reg1(self):
        return