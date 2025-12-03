from account_helpers import AccountSettings
_GRINCH_KEY = 'grinch_key'
BANNER_SEEN = 'bannerSeen'
ACCOUNT_DEFAULT_SETTINGS = {_GRINCH_KEY: {BANNER_SEEN: False}}

def getSettings(name):
    settings = AccountSettings.getSettings(_GRINCH_KEY)
    return settings.get(name, ACCOUNT_DEFAULT_SETTINGS[_GRINCH_KEY].get(name))


def setSettings(name, value):
    settings = AccountSettings.getSettings(_GRINCH_KEY)
    settings[name] = value
    AccountSettings.setSettings(_GRINCH_KEY, settings)


def isBannerSeen():
    return getSettings(BANNER_SEEN)


def setBannerSeen(seen=True):
    return setSettings(BANNER_SEEN, seen)