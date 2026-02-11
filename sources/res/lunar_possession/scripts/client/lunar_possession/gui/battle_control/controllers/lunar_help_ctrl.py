import typing, CommandMapping
from gui import InputHandler
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController
from lunar_possession.gui.impl.battle.lunar_help_view import LunarHelpWindow
from skeletons.gui.app_loader import IAppLoader
from helpers import dependency
if typing.TYPE_CHECKING:
    from Vehicle import Vehicle

class LunarIngameHelpController(IBattleController):
    __appLoader = dependency.descriptor(IAppLoader)
    __slots__ = ('__window', )

    def __init__(self, setup):
        super(LunarIngameHelpController, self).__init__()
        self.__window = None
        return

    def __handleKeyUpEvent(self, event):
        if CommandMapping.g_instance.isFired(CommandMapping.CMD_SHOW_HELP, event.key):
            self.__closeHelpWindow()

    def __openHelpWindow(self):
        if self.__window is not None:
            return
        else:
            self.__window = LunarHelpWindow()
            self.__window.load()
            return

    def __closeHelpWindow(self):
        if self.__window is None:
            return
        else:
            self.__window.destroy()
            self.__window = None
            return

    def getControllerID(self):
        return BATTLE_CTRL_ID.INGAME_HELP_CTRL

    def startControl(self, *args):
        InputHandler.g_instance.onKeyUp += self.__handleKeyUpEvent

    def stopControl(self):
        InputHandler.g_instance.onKeyUp -= self.__handleKeyUpEvent
        self.__closeHelpWindow()

    def canShow(self):
        battleApp = self.__appLoader.getDefBattleApp()
        if battleApp is None:
            return False
        else:
            return not bool(battleApp.containerManager.getViewByKey(ViewKey(VIEW_ALIAS.INGAME_MENU)))

    def showIngameHelp(self, vehicle):
        self.__openHelpWindow()
        return True