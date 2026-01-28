from gui.Scaleform.daapi.view.battle.shared.base_stats import StatsBase

class EpicFullStatsMeta(StatsBase):

    def as_initializeTextS(self, myLaneText, allLanesText, questsText):
        if self._isDAAPIInited():
            return self.flashObject.as_initializeText(myLaneText, allLanesText, questsText)

    def as_setIsInteractiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsInteractive(value)

    def as_setGeneralBonusS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setGeneralBonus(value)

    def as_toggleQuestsTabS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleQuestsTab(value)