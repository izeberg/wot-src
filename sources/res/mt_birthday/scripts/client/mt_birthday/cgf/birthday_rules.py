import CGF
from cgf_script.managers_registrator import registerRule, registerManager, Rule
from mt_birthday.cgf.birthday_components import BirthdayClickManager, BirthdayTooltipManager, EasterEggsManager

@registerRule
class BirthdayHangarRule(Rule):
    category = 'Birthday rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(BirthdayClickManager)
    def reg1(self):
        return

    @registerManager(BirthdayTooltipManager)
    def reg2(self):
        return

    @registerManager(EasterEggsManager)
    def reg3(self):
        return