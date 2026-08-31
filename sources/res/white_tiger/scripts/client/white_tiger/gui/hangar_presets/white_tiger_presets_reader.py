from __future__ import absolute_import
from gui.hangar_presets.obsolete.hangar_presets_reader import DefaultPresetReader

class WhiteTigerPresetsReader(DefaultPresetReader):
    _CONFIG_PATH = 'white_tiger/gui/configs/white_tiger_hangar_gui_presets.xml'

    @staticmethod
    def isDefault():
        return False