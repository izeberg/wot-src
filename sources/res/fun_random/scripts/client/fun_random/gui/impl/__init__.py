from __future__ import absolute_import
from fun_random.gui.impl.gen.view_models.views.lobby.loadout.fun_random_loadout_constants import FunRandomLoadoutConstants
from gui.impl.lobby.tank_setup.backports.tooltips import ShellTooltipBuilder
from gui.impl.lobby.tank_setup.backports.tooltips import PANEL_SLOT_TOOLTIPS

def registerFunRandomImpl():
    PANEL_SLOT_TOOLTIPS.update({FunRandomLoadoutConstants.FUN_RANDOM_CUSTOM_SHELLS: ShellTooltipBuilder})