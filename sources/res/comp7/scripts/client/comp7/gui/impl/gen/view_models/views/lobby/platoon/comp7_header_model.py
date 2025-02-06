from gui.impl.gen.view_models.views.lobby.platoon.member_count_dropdown import MemberCountDropdown
from gui.impl.gen.view_models.views.lobby.platoon.window_header_model import WindowHeaderModel

class Comp7HeaderModel(WindowHeaderModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(Comp7HeaderModel, self).__init__(properties=properties, commands=commands)

    @property
    def memberCountDropdown(self):
        return self._getViewModel(7)

    @staticmethod
    def getMemberCountDropdownType():
        return MemberCountDropdown

    def _initialize(self):
        super(Comp7HeaderModel, self)._initialize()
        self._addViewModelProperty('memberCountDropdown', MemberCountDropdown())