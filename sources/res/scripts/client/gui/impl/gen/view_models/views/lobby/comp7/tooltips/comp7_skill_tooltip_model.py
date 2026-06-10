from gui.impl.gen.view_models.views.lobby.comp7.skill_model import SkillModel

class Comp7SkillTooltipModel(SkillModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(Comp7SkillTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(Comp7SkillTooltipModel, self)._initialize()