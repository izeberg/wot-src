from __future__ import absolute_import
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from fall_tanks.gui.impl.battle.battle_page.fall_tanks_battle_widget import FallTanksBattleWidgetView

class FallTanksBattleWidgetInject(InjectComponentAdaptor):

    def _makeInjectView(self, *args):
        return FallTanksBattleWidgetView()