from historical_battles_common.hb_constants_extension import QUEUE_TYPE
from gui.hangar_presets.hangar_presets_getters import DefaultPresetsGetter

class HistoricalBattlesPresetsGetter(DefaultPresetsGetter):
    __slots__ = ('__hangarName', )
    _QUEUE_TYPE = None

    def __init__(self, config):
        super(HistoricalBattlesPresetsGetter, self).__init__(config)
        self._presetName, self.__hangarName = config.modes.get(self._QUEUE_TYPE)

    def getHangarName(self):
        return self.__hangarName


class HBOffencePresetsGetter(HistoricalBattlesPresetsGetter):
    _QUEUE_TYPE = QUEUE_TYPE.HB_OFFENCE


class HBDefencePresetsGetter(HistoricalBattlesPresetsGetter):
    _QUEUE_TYPE = QUEUE_TYPE.HB_DEFENCE