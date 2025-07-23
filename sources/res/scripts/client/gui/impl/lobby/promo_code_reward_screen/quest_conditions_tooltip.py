from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tooltips.quest_conditions_tooltip_model import QuestConditionsTooltipModel
from gui.impl.gen.view_models.views.lobby.tooltips.quest_descr_model import QuestDescrModel
from gui.impl.pub import ViewImpl

class QuestConditionsTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.tooltips.QuestConditionsTooltip(), model=QuestConditionsTooltipModel(), args=args, kwargs=kwargs)
        super(QuestConditionsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(QuestConditionsTooltip, self).getViewModel()

    def _onLoading(self, quests):
        super(QuestConditionsTooltip, self)._onLoading()
        availableQuests = [ q for q in quests if q.isAvailable() ]
        with self.viewModel.transaction() as (model):
            model.setTotalQuests(len(quests))
            questsArr = model.getQuests()
            questsArr.clear()
            for quest in availableQuests:
                questDescr = QuestDescrModel()
                questDescr.setQuestName(quest.getUserName())
                questDescr.setConditions(quest.getDescription())
                questsArr.addViewModel(questDescr)
                questsArr.invalidate()