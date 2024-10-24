from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from shared_utils import BoundMethodWeakref
from .hangar_space_listener import HangarSpaceListener

class HangarCameraSettingsListener(HangarSpaceListener):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(HangarCameraSettingsListener, self).__init__()
        self.__settingHandlers = {}

    def destroy(self):
        super(HangarCameraSettingsListener, self).destroy()
        self.__settingHandlers.clear()

    def registerSettingHandler(self, setting, handler):
        if setting in self.__settingHandlers:
            return False
        self.__settingHandlers[setting] = BoundMethodWeakref(handler)
        return True

    def unregisterSettingsHandler(self, setting):
        if setting not in self.__settingHandlers:
            return False
        del self.__settingHandlers[setting]
        return True

    def _activate(self):
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged

    def _deactivate(self, inited):
        if inited:
            self.settingsCore.onSettingsChanged -= self.__onSettingsChanged

    def __onSettingsChanged(self, diff):
        for setting, handler in self.__settingHandlers.iteritems():
            if setting in diff:
                handler()