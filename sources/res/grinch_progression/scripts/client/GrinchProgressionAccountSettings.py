from account_helpers import AccountSettings
_GRINCH_PROGRESSION_KEY = 'grinch_progression_key'
PREVIOUS_POINTS_COUNT = 'previous_points_count'
PREVIOUS_TOTAL_POINTS_COUNT = 'previous_total_points_count'
POINTS_SEEN_COUNT = 'points_seen_count'
CLAIMABLE_REWARDS_SEEN_COUNT = 'claimable_rewards_seen_count'
IS_FIRST_ENTRY = 'is_first_entry'
ACCOUNT_DEFAULT_SETTINGS = {_GRINCH_PROGRESSION_KEY: {PREVIOUS_POINTS_COUNT: 0, 
                             PREVIOUS_TOTAL_POINTS_COUNT: 0, 
                             POINTS_SEEN_COUNT: 0, 
                             CLAIMABLE_REWARDS_SEEN_COUNT: 0, 
                             IS_FIRST_ENTRY: True}}

def getSettings(name):
    settings = AccountSettings.getSettings(_GRINCH_PROGRESSION_KEY)
    return settings.get(name, ACCOUNT_DEFAULT_SETTINGS[_GRINCH_PROGRESSION_KEY].get(name))


def setSettings(name, value):
    settings = AccountSettings.getSettings(_GRINCH_PROGRESSION_KEY)
    settings[name] = value
    AccountSettings.setSettings(_GRINCH_PROGRESSION_KEY, settings)