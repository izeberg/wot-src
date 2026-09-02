from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel

class WtQuestModel(DailyQuestModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(WtQuestModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(WtQuestModel, self)._initialize()