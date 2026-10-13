from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HWBattleUpgradePanelMeta(BaseDAAPIComponent):

    def onSelectItem(self, itemID):
        self._printOverrideError('onSelectItem')

    def onAppear(self):
        self._printOverrideError('onAppear')

    def onItemHover(self):
        self._printOverrideError('onItemHover')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setAnomaliesMatrixHotkeyS(self, hotKey):
        if self._isDAAPIInited():
            return self.flashObject.as_setAnomaliesMatrixHotkey(hotKey)

    def as_toggleAlertStateS(self, isVisible, alertText=None):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleAlertState(isVisible, alertText)

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)

    def as_showSelectAnimS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectAnim(idx)

    def as_showNotificationAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showNotificationAnim()

    def as_hideNotificationAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideNotificationAnim()