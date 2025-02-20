from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap.plugin_items.step_repair_point_entries import StepRepairPointEntriesPlugin

class FunRandomMiniMapComponent(ClassicMinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(FunRandomMiniMapComponent, self)._setupPlugins(arenaVisitor)
        if arenaVisitor.hasStepRepairPoints():
            setup['repairs'] = StepRepairPointEntriesPlugin
        return setup