import CGF
from cgf_script.managers_registrator import registerRule, registerManager, Rule
from museum_of_glory.cgf.museum_entry_manager import MuseumEntryManager

@registerRule
class MuseumHangarRule(Rule):
    category = 'Museum of Glory rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(MuseumEntryManager)
    def reg1(self):
        return