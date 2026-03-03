from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading

class FallTanksBattleLoading(BattleLoading):

    def invalidateArenaInfo(self):
        pass

    def _formatTipTitle(self, tipTitleText):
        return ''

    def _formatTipBody(self, tipBody):
        return ''

    def _getBattlesCount(self):
        return 0

    def _getViewSettingByID(self, settingID):
        return {}

    def _makeVisualTipVO(self, arenaDP, tip=None):
        return {}

    def _setTipsInfo(self):
        pass