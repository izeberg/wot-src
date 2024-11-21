from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from new_year.gui.impl.lobby.new_year.quests.ny_quest_entry_point_view import NYQuestEntryPointView

class NYQuestEntryPoint(InjectComponentAdaptor):

    def _makeInjectView(self):
        return NYQuestEntryPointView()