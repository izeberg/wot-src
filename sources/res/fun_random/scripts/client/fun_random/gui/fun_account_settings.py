from typing import TYPE_CHECKING
from account_helpers import AccountSettings
from account_helpers.AccountSettings import KEY_SETTINGS
from fun_random.gui.fun_gui_constants import AccountSettingsKeys, ACCOUNT_DEFAULT_SETTINGS
if TYPE_CHECKING:
    from typing import Any

class FunSubModeAccountSettings(object):

    def __init__(self, subModeKey):
        self.subModeKey = subModeKey

    def getSettings(self, name):
        defaultValue = ACCOUNT_DEFAULT_SETTINGS.get(name)
        settings = AccountSettings.getSettings(AccountSettingsKeys.FUN_KEY) or {}
        return settings.get(self.subModeKey, {}).get(name, defaultValue)

    def setSettings(self, name, value):
        settings = AccountSettings.getSettings(AccountSettingsKeys.FUN_KEY) or {}
        settings.setdefault(self.subModeKey, {})[name] = value
        AccountSettings.setSettings(AccountSettingsKeys.FUN_KEY, settings)

    def isInfoPageViewed(self):
        return self.getSettings(AccountSettingsKeys.INFO_PAGE_VIEWED)

    def setInfoPageViewed(self, status):
        return self.setSettings(AccountSettingsKeys.INFO_PAGE_VIEWED, status)

    def isNew(self):
        return self.getSettings(AccountSettingsKeys.IS_NEW)

    def setIsNew(self, status):
        return self.setSettings(AccountSettingsKeys.IS_NEW, status)


def setSubModeDefaultSettings(subModeKey):
    settings = AccountSettings.getSettingsDefault(AccountSettingsKeys.FUN_KEY) or {}
    settings[subModeKey] = ACCOUNT_DEFAULT_SETTINGS
    AccountSettings.overrideDefaultSettings(KEY_SETTINGS, {AccountSettingsKeys.FUN_KEY: settings})