from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS
from gui.shared.system_factory import registerLobbyTooltipsBuilders

def registerAdventCalendarScaleform():
    registerLobbyTooltipsBuilders([
     (
      'advent_calendar.gui.Scaleform.daapi.view.tooltips.lobby_builders', _TOOLTIPS.ADVENT_CALENDAR_SET)])