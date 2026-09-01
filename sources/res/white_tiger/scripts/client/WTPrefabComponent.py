from __future__ import absolute_import
from white_tiger.helpers.prefab_helpers import PrefabHandlerComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent

class WTPrefabComponent(PrefabHandlerComponent, DynamicScriptComponent):

    def _onAvatarReady(self):
        self.createGameObject()

    def createGameObject(self):
        parent = self.entity.entityGameObject
        if parent is not None:
            self.loadGameObject(self.entity, self.prefab, parent, self.matrix)
        return

    def onDestroy(self):
        self.destroyGameObject()
        super(WTPrefabComponent, self).onDestroy()