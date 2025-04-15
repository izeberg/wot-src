from gui.Scaleform.daapi.view.battle.classic.tab_screen import TabScreenComponent

class WinbackFullStatsComponent(TabScreenComponent):

    @staticmethod
    def _buildTabs(builder):
        builder.addStatisticsTab()
        builder.addBoostersTab()
        return builder.getTabs()