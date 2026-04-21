from last_stand.gui.scaleform.daapi.view.meta.BattleHintProgressDefenceMeta import BattleHintProgressDefenceMeta

class BattleHintProgressConvoyMeta(BattleHintProgressDefenceMeta):

    def as_setConvoyVehiclesStatusS(self, states):
        if self._isDAAPIInited():
            return self.flashObject.as_setConvoyVehiclesStatus(states)