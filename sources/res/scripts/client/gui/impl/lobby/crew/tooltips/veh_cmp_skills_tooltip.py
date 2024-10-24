from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.veh_cmp_skills_tooltip_model import VehCmpSkillsTooltipModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.skills_by_role import SkillsByRole
from gui.impl.pub import ViewImpl
from items.components.skills_constants import ALL_SKILLS_BY_ROLE_TYPE

class VehCmpSkillsTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.lobby.crew.tooltips.VehCmpSkillsTooltip())
        settings.model = VehCmpSkillsTooltipModel()
        super(VehCmpSkillsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(VehCmpSkillsTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(VehCmpSkillsTooltip, self)._onLoading()
        with self.viewModel.transaction() as (vm):
            skillsVM = vm.getSkills()
            skillsVM.clear()
            for role, skills in ALL_SKILLS_BY_ROLE_TYPE.iteritems():
                skillsByRole = SkillsByRole()
                skillsByRole.setRole(role)
                skillList = skillsByRole.getSkills()
                skillList.clear()
                for skill in skills:
                    skillList.addString(skill)

                skillsVM.addViewModel(skillsByRole)