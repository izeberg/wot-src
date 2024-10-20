from skeletons.account_helpers.settings_core import ISettingsCache, ISettingsCore, IBattleCommunicationsSettings

def getSettingsCoreConfig(manager):
    from account_helpers.settings_core.battle_communications_settings import BattleCommunicationSettings
    from account_helpers.settings_core.SettingsCache import SettingsCache
    from account_helpers.settings_core.SettingsCore import SettingsCore
    cache = SettingsCache()
    manager.addInstance(ISettingsCache, cache, finalizer='fini')
    core = SettingsCore()
    manager.addInstance(ISettingsCore, core, finalizer='fini')
    communications = BattleCommunicationSettings()
    manager.addInstance(IBattleCommunicationsSettings, communications, finalizer='fini')
    cache.init()
    core.init()
    communications.init()


def longToInt32(value):
    if 2147483648 <= value <= 4294967295:
        value &= 2147483647
        value = int(value)
        value = ~value
        value ^= 2147483647
    return value