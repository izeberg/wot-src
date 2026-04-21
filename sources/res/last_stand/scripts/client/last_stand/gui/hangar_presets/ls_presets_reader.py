from __future__ import absolute_import
from gui.hangar_presets.obsolete.hangar_presets_reader import DefaultPresetReader

class LSPresetsReader(DefaultPresetReader):
    _CONFIG_PATH = 'last_stand/gui/configs/ls_hangar_gui_presets.xml'

    @staticmethod
    def isDefault():
        return False