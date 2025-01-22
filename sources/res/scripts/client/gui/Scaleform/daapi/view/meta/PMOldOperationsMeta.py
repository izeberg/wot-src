from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PMOldOperationsMeta(BaseDAAPIComponent):

    def onOperationClick(self, pmType, operationID):
        self._printOverrideError('onOperationClick')

    def showInfo(self):
        self._printOverrideError('showInfo')

    def as_setOperationsS(self, operations):
        if self._isDAAPIInited():
            return self.flashObject.as_setOperations(operations)

    def as_setTitleS(self, titleVO):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(titleVO)