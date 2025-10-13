from gui.shared.tooltips import contexts, advanced
from gui.shared.tooltips.builders import DataBuilder, AdvancedDataBuilder
from halloween.gui.halloween_gui_constants import HALLOWEEN_CAROUSEL_VEHICLE_TOOLTIP, HALLOWEEN_ABILITY_TOOLTIP, HALLOWEEN_MAIN_SHELL
from halloween.gui.scaleform.daapi.view.tooltips import event
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.daapi.view.tooltips.vehicle_items_builders import AdvancedShellBuilder
from halloween.gui.shared.contexts import EventVehicleContext
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(HALLOWEEN_CAROUSEL_VEHICLE_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, event.EventVehicleInfoTooltipData(EventVehicleContext())),
     AdvancedDataBuilder(HALLOWEEN_ABILITY_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, event.EventModuleBlockTooltipData(contexts.HangarContext()), advanced.HangarModuleAdvanced(contexts.HangarContext())),
     AdvancedShellBuilder(HALLOWEEN_MAIN_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, event.EventShellBlockToolTipData(contexts.TechMainContext()), advanced.HangarShellAdvanced(contexts.TechMainContext())))