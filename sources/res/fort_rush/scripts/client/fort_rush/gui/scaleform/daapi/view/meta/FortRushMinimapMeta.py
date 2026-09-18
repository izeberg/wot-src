from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent

class FortRushMinimapMeta(ClassicMinimapComponent):

    def onZoneClicked(self, zoneName):
        self._printOverrideError('onZoneClicked')

    def as_showZonePingS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_showZonePing(zoneName)

    def as_showZoneCommitS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_showZoneCommit(zoneName)

    def as_clearZonePingS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_clearZonePing(zoneName)

    def as_updateZoneCaptureStateS(self, zoneName, ownerTeam, progressTeam, captureActive, isContested, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateZoneCaptureState(zoneName, ownerTeam, progressTeam, captureActive, isContested, progress)