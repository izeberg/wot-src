from gui.impl.gen.view_models.views.lobby.battle_results.battle_info_model import BattleInfoModel

class FunRandomBattleInfoModel(BattleInfoModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(FunRandomBattleInfoModel, self).__init__(properties=properties, commands=commands)

    def getAssetsPointer(self):
        return self._getString(7)

    def setAssetsPointer(self, value):
        self._setString(7, value)

    def getSubModeAssetsPointer(self):
        return self._getString(8)

    def setSubModeAssetsPointer(self, value):
        self._setString(8, value)

    def _initialize(self):
        super(FunRandomBattleInfoModel, self)._initialize()
        self._addStringProperty('assetsPointer', 'undefined')
        self._addStringProperty('subModeAssetsPointer', 'undefined')