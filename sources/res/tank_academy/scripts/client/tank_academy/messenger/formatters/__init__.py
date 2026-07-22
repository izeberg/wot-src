from tank_academy.gui import gui_constants
from tank_academy.messenger.formatters.service_channel import TankAcademyTokenAward
from tank_academy.messenger.formatters.token_quest_subformatters import TankAcademyClientAwardsFormatter, TankAcademyAwardsFormatter
from gui.shared.system_factory import registerMessengerClientFormatter, registerTokenQuestsSubFormatters
clientFormatters = {gui_constants.SCH_CLIENT_MSG_TYPE.TANK_ACADEMY_TOKEN_AWARD: TankAcademyTokenAward(), 
   gui_constants.SCH_CLIENT_MSG_TYPE.TANK_ACADEMY_BATTLE_AWARD: TankAcademyClientAwardsFormatter()}

def registerMessengerClientFormatters():
    for sysMsgType, formatter in clientFormatters.iteritems():
        registerMessengerClientFormatter(sysMsgType, formatter)


def registerTankAcademyTokenQuestsSubFormatters():
    registerTokenQuestsSubFormatters((
     TankAcademyAwardsFormatter(),))