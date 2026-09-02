from account_helpers import AccountSettings
from museum_of_glory.museum_of_glory_constants import ACCOUNT_DEFAULT_SETTINGS, MUSEUM_OF_GLORY

def getMuseumOfGlorySetting(name):
    return AccountSettings.getSettings(MUSEUM_OF_GLORY).get(name, ACCOUNT_DEFAULT_SETTINGS[MUSEUM_OF_GLORY][name])


def setMuseumOfGlorySettings(name, value):
    settings = AccountSettings.getSettings(MUSEUM_OF_GLORY)
    settings[name] = value
    AccountSettings.setSettings(MUSEUM_OF_GLORY, settings)