from __future__ import absolute_import
import typing, CGF
from script_component.DynamicScriptComponent import DynamicScriptComponent
from constants import IS_VS_EDITOR
if not IS_VS_EDITOR:
    from WhiteTigerComponents import WTAlwaysVisibleComponent

class WTAlwaysVisible(DynamicScriptComponent):

    def _onAvatarReady(self):
        go = self.__getAppearanceGo()
        if go is not None and not go.hasComponent(WTAlwaysVisibleComponent):
            queue = CGF.CommandQueue(go.spaceID)
            queue.createComponent(go, WTAlwaysVisibleComponent)
        return

    def onDestroy(self):
        go = self.__getAppearanceGo()
        if go is not None:
            go.removeComponent(WTAlwaysVisibleComponent)
        super(WTAlwaysVisible, self).onDestroy()
        return

    def __getAppearanceGo(self):
        appearance = self.entity.appearance
        if appearance is not None:
            return appearance.gameObject
        else:
            return