from grinch_common.grinch_constants import QUEUE_TYPE
from grinch.gui.hangar_presets.grinch_hangar_presets_reader import GrinchPresetsReader
from grinch.gui.hangar_presets.grinch_hangar_presets_getter import GrinchPresetsGetter
from gui.shared.system_factory import registerHangarPresetsReader, registerHangarPresetGetter

def registerGrinchHangarPresets():
    registerHangarPresetsReader(GrinchPresetsReader)
    registerHangarPresetGetter(QUEUE_TYPE.GRINCH, GrinchPresetsGetter)