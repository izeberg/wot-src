from frontline.gui.Scaleform.daapi.view.meta.FrontlineMinimapMeta import FrontlineMinimapMeta

class FrontlineDeploymentMapMeta(FrontlineMinimapMeta):

    def as_setMapDimensionsS(self, widthPx, heightPx):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapDimensions(widthPx, heightPx)