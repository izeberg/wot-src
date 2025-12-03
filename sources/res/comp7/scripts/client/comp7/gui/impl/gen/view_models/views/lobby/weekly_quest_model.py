from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel

class WeeklyQuestModel(WidgetQuestModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(WeeklyQuestModel, self).__init__(properties=properties, commands=commands)

    def getQuestNumber(self):
        return self._getNumber(15)

    def setQuestNumber(self, value):
        self._setNumber(15, value)

    def _initialize(self):
        super(WeeklyQuestModel, self)._initialize()
        self._addNumberProperty('questNumber', 0)