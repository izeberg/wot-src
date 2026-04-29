from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts, module
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.STORAGE_RESTORE_DEVICE_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, module.RestoreOptDeviceBlockTooltipData(contexts.RestoreCardContext())),)