from pve_battle_hud import WidgetType
from messenger.gui.Scaleform.view.battle.messenger_view import BattleMessengerView

class PveBattleMessengerView(BattleMessengerView):

    def handleEnterPressed(self):
        settingsCtrl = self.sessionProvider.dynamic.vseHUDSettings
        if settingsCtrl is not None:
            chatSettings = settingsCtrl.getSettings(WidgetType.CHAT)
            if chatSettings is not None and chatSettings.hide:
                return
        super(PveBattleMessengerView, self).handleEnterPressed()
        return