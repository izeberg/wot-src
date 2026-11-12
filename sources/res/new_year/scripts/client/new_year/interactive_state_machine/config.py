from account_helpers import AccountSettings
from new_year.ny_constants import INTERACTIVE_STATE_MACHINE, NEW_YEAR
from new_year_account_settings import getNYSetting

def getSMSetting(name, personaType):
    return getNYSetting(INTERACTIVE_STATE_MACHINE)[personaType][name]


def setSMSetting(name, personaType, value):
    settings = AccountSettings.getSettings(NEW_YEAR)
    settings[INTERACTIVE_STATE_MACHINE][personaType][name] = value
    AccountSettings.setSettings(NEW_YEAR, settings, True)