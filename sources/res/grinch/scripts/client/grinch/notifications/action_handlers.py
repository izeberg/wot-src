from helpers import dependency
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE
from grinch.skeletons.battle_controller import IGrinchController

@dependency.replace_none_kwargs(ctrl=IGrinchController)
def _switchGrinch(ctrl=None):
    ctrl.selectMode()


class GrinchSwitchPrbActionHandler(NavigationDisabledActionHandler):

    def doAction(self, model, entityID, action):
        _switchGrinch()

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('grinchSwitchPrb', )