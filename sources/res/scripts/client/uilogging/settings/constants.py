from enum import Enum
FEATURE = 'settings'
GROUP = 'settings'

class SettingsLogActions(Enum):
    SETTINGS_INITED = 'settings_inited'
    SETTINGS_CHANGED = 'settings_changed'