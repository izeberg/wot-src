from gui_lootboxes.gui.impl.lobby.gui_lootboxes import LootBoxTooltipBaseHandler

class NyDecorationTooltipHandler(LootBoxTooltipBaseHandler):

    def __call__(self, event):
        view = self.view
        return view(event.getArgument('toyID'))