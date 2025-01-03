from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

class BobPlayersPanelMeta(PlayersPanel):

    def onVoiceChatControlClick(self):
        self._printOverrideError('onVoiceChatControlClick')

    def as_setLeftTeamSkillS(self, iconName, title, description):
        if self._isDAAPIInited():
            return self.flashObject.as_setLeftTeamSkill(iconName, title, description)

    def as_setRightTeamSkillS(self, iconName, title, description):
        if self._isDAAPIInited():
            return self.flashObject.as_setRightTeamSkill(iconName, title, description)

    def as_setBattleStartedS(self, value=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleStarted(value)

    def as_setVoiceChatDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatData(data)

    def as_setVoiceChatControlVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatControlVisible(value)

    def as_setVoiceChatControlSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatControlSelected(value)