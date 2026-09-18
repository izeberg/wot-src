from __future__ import absolute_import
from gui.battle_control.controllers.arena_border_ctrl import ArenaBorderController, _DISPLAY_MODE

class HWArenaBorderController(ArenaBorderController):

    def _applySetting(self, showMode, drawType, color):
        if drawType == _DISPLAY_MODE.TYPE_WALL:
            drawType = _DISPLAY_MODE.TYPE_DOTTED
        super(HWArenaBorderController, self)._applySetting(showMode, drawType, color)