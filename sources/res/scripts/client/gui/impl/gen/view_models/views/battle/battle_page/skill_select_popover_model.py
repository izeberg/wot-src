from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.comp7.skill_model import SkillModel

class SkillSelectPopoverModel(ViewModel):
    __slots__ = ('onEquip', 'onClose')

    def __init__(self, properties=1, commands=2):
        super(SkillSelectPopoverModel, self).__init__(properties=properties, commands=commands)

    @property
    def skills(self):
        return self._getViewModel(0)

    @staticmethod
    def getSkillsType():
        return SkillModel

    def _initialize(self):
        super(SkillSelectPopoverModel, self)._initialize()
        self._addViewModelProperty('skills', UserListModel())
        self.onEquip = self._addCommand('onEquip')
        self.onClose = self._addCommand('onClose')