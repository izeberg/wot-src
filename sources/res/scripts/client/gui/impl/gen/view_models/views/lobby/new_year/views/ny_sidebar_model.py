from gui.impl.gen.view_models.views.lobby.new_year.components.ny_trigger_hint_tabs_model import NyTriggerHintTabsModel
from gui.impl.gen.view_models.views.lobby.new_year.views.ny_sidebar_common_model import NySidebarCommonModel

class NySidebarModel(NySidebarCommonModel):
    __slots__ = ()
    VIEW_NAME_GLADE = 'glade'
    VIEW_NAME_FRIEND_GLADE = 'friendGlade'
    VIEW_NAME_CHALLENGE = 'challenge'
    VIEW_NAME_MARKETPLACE = 'marketplace'

    def __init__(self, properties=3, commands=0):
        super(NySidebarModel, self).__init__(properties=properties, commands=commands)

    @property
    def triggerHintTabs(self):
        return self._getViewModel(2)

    @staticmethod
    def getTriggerHintTabsType():
        return NyTriggerHintTabsModel

    def _initialize(self):
        super(NySidebarModel, self)._initialize()
        self._addViewModelProperty('triggerHintTabs', NyTriggerHintTabsModel())