from __future__ import absolute_import
from gui.hangar_presets.obsolete.hangar_presets_reader import DefaultPresetReader

class FortRushPresetsReader(DefaultPresetReader):
    _CONFIG_PATH = 'fort_rush/gui/configs/fort_rush_hangar_gui_presets.xml'

    @staticmethod
    def isDefault():
        return False