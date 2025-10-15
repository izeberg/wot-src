from gui.hangar_presets import DefaultPresetReader

class PortalHangarPresetsReader(DefaultPresetReader):
    _CONFIG_PATH = 'portal/gui/portal_hangar_gui_presets.xml'

    @staticmethod
    def isDefault():
        return False