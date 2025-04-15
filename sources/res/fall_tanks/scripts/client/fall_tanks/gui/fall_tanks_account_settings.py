from account_helpers import AccountSettings
from account_helpers.AccountSettings import KEY_SETTINGS

class AccountSettingsKeys(object):
    FALL_TANKS_HINTS = 'fallTanksHintSection'
    VEHICLE_EVACUATION = 'vehicle_evacuation_hint_section'


ACCOUNT_DEFAULT_SETTINGS = {AccountSettingsKeys.FALL_TANKS_HINTS: {}}

def addFallTanksAccountSettings():
    AccountSettings.overrideDefaultSettings(KEY_SETTINGS, ACCOUNT_DEFAULT_SETTINGS)