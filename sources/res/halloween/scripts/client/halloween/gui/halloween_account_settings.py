from copy import deepcopy
from account_helpers import AccountSettings
from halloween.gui.halloween_gui_constants import DifficultyLevel

class AccountSettingsKeys(object):
    EVENT_KEY = 'hw24_keys'
    SELECTED_LEVEL = 'selected_level'
    UNLOCK_LEVELS = 'unlock_levels'
    AWARD_UNLOCK_LEVELS = 'award_unlock_level'
    META_INTRO_VIEW_SHOWED = 'meta_into_view_showed'
    FAVORITES_VEHICLE = 'favorites'
    DEFENCE_FAVORITES_VEHICLE = 'defence_favorites'
    SOUND = 'sound'
    CHAT_FIRST_SEEN = 'chat_first_seen'
    ARTEFACT_VOICEOVER_MUTED = 'artefact_voiceover_muted'
    PROMO_SCREEN_SHOWED = 'promo_screen_showed'
    CAROUSEL_FILTER_DEF = 'carousel_filter_def'


ACCOUNT_DEFAULT_SETTINGS = {AccountSettingsKeys.EVENT_KEY: {AccountSettingsKeys.SELECTED_LEVEL: DifficultyLevel.EASY.value, 
                                   AccountSettingsKeys.UNLOCK_LEVELS: {}, AccountSettingsKeys.AWARD_UNLOCK_LEVELS: [], AccountSettingsKeys.META_INTRO_VIEW_SHOWED: False, 
                                   AccountSettingsKeys.FAVORITES_VEHICLE: 0, 
                                   AccountSettingsKeys.DEFENCE_FAVORITES_VEHICLE: 0, 
                                   AccountSettingsKeys.SOUND: {}, AccountSettingsKeys.CHAT_FIRST_SEEN: False, 
                                   AccountSettingsKeys.ARTEFACT_VOICEOVER_MUTED: False, 
                                   AccountSettingsKeys.PROMO_SCREEN_SHOWED: False, 
                                   AccountSettingsKeys.CAROUSEL_FILTER_DEF: {}}}

def getSettings(name):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    return settings.get(name, deepcopy(AccountSettings.getSettingsDefault(AccountSettingsKeys.EVENT_KEY)[name]))


def setSettings(name, value):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    settings[name] = value
    AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)


def isSoundPlayed(name, difficultyLevel):
    soundsSettings = getSettings(AccountSettingsKeys.SOUND)
    soundsByDifficultyLevel = soundsSettings.get(difficultyLevel.value)
    if soundsByDifficultyLevel:
        return name in soundsByDifficultyLevel
    return False


def setSoundPlayed(name, difficultyLevel):
    soundsSettings = getSettings(AccountSettingsKeys.SOUND)
    soundsByDifficultyLevel = soundsSettings.setdefault(difficultyLevel.value, set())
    soundsByDifficultyLevel.add(name)
    setSettings(AccountSettingsKeys.SOUND, soundsSettings)


def setAwardUnlockedLevel(level):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    unlockedLevels = settings[AccountSettingsKeys.AWARD_UNLOCK_LEVELS]
    if level.value not in unlockedLevels:
        unlockedLevels.append(level.value)
        settings[AccountSettingsKeys.AWARD_UNLOCK_LEVELS] = unlockedLevels
        AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)


def setNewStatusUnlockLevel(level, status):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    unlockedLevels = settings[AccountSettingsKeys.UNLOCK_LEVELS]
    unlockedLevels[level.value] = {'isNew': status}
    settings[AccountSettingsKeys.UNLOCK_LEVELS] = unlockedLevels
    AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)