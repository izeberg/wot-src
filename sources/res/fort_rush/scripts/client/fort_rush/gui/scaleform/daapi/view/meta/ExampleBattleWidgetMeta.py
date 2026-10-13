from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ExampleBattleWidgetMeta(BaseDAAPIComponent):

    def as_showSomeDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showSomeData(data)