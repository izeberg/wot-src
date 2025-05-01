from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HBSPGPanelMeta(BaseDAAPIComponent):

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()

    def as_setSPGListS(self, spgList):
        if self._isDAAPIInited():
            return self.flashObject.as_setSPGList(spgList)

    def as_setSPGHpS(self, vehID, hpMax, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_setSPGHp(vehID, hpMax, hpCurrent)

    def as_hideTitleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideTitle()