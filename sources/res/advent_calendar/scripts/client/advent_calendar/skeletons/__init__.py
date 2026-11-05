from __future__ import absolute_import
from advent_calendar.gui.game_control.advent_calendar_controller import AdventCalendarController
from advent_calendar.skeletons.game_controller import IAdventCalendarController
from gui.shared.system_factory import registerGameControllers

def registerAdventCalendarController():
    registerGameControllers([
     (
      IAdventCalendarController, AdventCalendarController, False)])