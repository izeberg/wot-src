from gui.Scaleform.daapi.view.meta.EpicMinimapMeta import EpicMinimapMeta

class EpicDeploymentMapMeta(EpicMinimapMeta):

    def as_setMapDimensionsS(self, widthPx, heightPx):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapDimensions(widthPx, heightPx)

    def as_setDirectionS(self, currentDirection, selectedDirection):
        if self._isDAAPIInited():
            return self.flashObject.as_setDirection(currentDirection, selectedDirection)