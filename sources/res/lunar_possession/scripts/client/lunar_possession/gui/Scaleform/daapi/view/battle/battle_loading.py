from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading, _isBattleLoadingShowed, _setBattleLoading
from account_helpers.settings_core.options import BattleLoadingTipSetting
from lunar_possession.helpers.tips import LunarTipsCriteria
from gui.shared.formatters import text_styles
from gui.impl.gen import R
from gui.impl import backport

class LunarPossessionBattleLoading(BattleLoading):

    def _getViewSettingByID(self, settingID):
        result = super(LunarPossessionBattleLoading, self)._getViewSettingByID(settingID)
        result['leftTeamTitleLeft'] = -483
        result['rightTeamTitleLeft'] = 275
        return result

    def _addArenaTypeData(self):
        self.as_setMapIconS(backport.image(R.images.lunar_possession.gui.maps.icons.battleLoading.lunar_event_preview()))

    def _setTipsInfo(self):
        arenaDP = self._battleCtx.getArenaDP()
        if not _isBattleLoadingShowed():
            criteria = LunarTipsCriteria()
            tip = criteria.find()
            translation = self.gui.resourceManager.getTranslatedText
            titleText = translation(tip.status)
            bodyText = translation(tip.body)
            iconPath = self.gui.resourceManager.getImagePath(tip.icon)
            self.as_setTipTitleS(text_styles.highTitle(titleText))
            self.as_setTipS(text_styles.main(bodyText))
            vo = self._makeVisualTipVO(arenaDP, tipIconOverride=iconPath)
            self.as_setVisualTipInfoS(vo)
            _setBattleLoading(True)

    def _formatTipTitle(self, tipTitleText):
        return text_styles.highTitle(tipTitleText)

    def _makeVisualTipVO(self, arenaDP, tipIconOverride=None):
        settingID = BattleLoadingTipSetting.OPTIONS.VISUAL
        vo = self._getViewSettingByID(settingID)
        tipIcon = tipIconOverride or backport.image(R.images.lunar_possession.gui.maps.icons.battleLoading.lunar_hint_art())
        vo.update({'settingID': settingID, 
           'tipIcon': tipIcon, 
           'arenaTypeID': self._arenaVisitor.type.getID(), 
           'minimapTeam': arenaDP.getNumberOfTeam(), 
           'showMinimap': False, 
           'showTipsBackground': True, 
           'showTableBackground': False})
        return vo