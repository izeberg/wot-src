from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class WhiteTigerBossTeleportViewMeta(BaseDAAPIComponent):

    def onTeleportPointClick(self, id):
        self._printOverrideError('onTeleportPointClick')

    def onCancel(self):
        self._printOverrideError('onCancel')