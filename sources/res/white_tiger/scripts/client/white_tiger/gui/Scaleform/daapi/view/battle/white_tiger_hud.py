from __future__ import absolute_import
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from white_tiger.gui.impl.battle.white_tiger_hud_view import WhiteTigerHudView

class WhiteTigerHud(InjectComponentAdaptor):

    def _makeInjectView(self):
        return WhiteTigerHudView()