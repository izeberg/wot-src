from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

class LSPlayersPanelMeta(PlayersPanel):

    def onVoiceChatClick(self):
        self._printOverrideError('onVoiceChatClick')

    def onTalkDown(self):
        self._printOverrideError('onTalkDown')

    def onTalkUp(self):
        self._printOverrideError('onTalkUp')

    def as_setPlayerPanelInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelInfo(data)

    def as_setPlayerPanelHpS(self, vehID, hpMax, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelHp(vehID, hpMax, hpCurrent)

    def as_setVoiceChatBindingsS(self, chatBind, talkBind):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatBindings(chatBind, talkBind)

    def as_setVoiceChatActivatedS(self, isActivated):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatActivated(isActivated)

    def as_setVoiceChatAvailableS(self, isAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatAvailable(isAvailable)

    def as_setVoiceChatEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatEnabled(isEnabled)

    def as_setIsTalkS(self, isTalk):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsTalk(isTalk)

    def as_setPlayerDeadS(self, vehID):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerDead(vehID)

    def as_setPostmortemS(self, isPostmortem):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostmortem(isPostmortem)