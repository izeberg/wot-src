from __future__ import absolute_import
import logging
from fort_rush.gui.shared.event_dispatcher import showProgressionView
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from helpers import dependency
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE

@dependency.replace_none_kwargs(ctrl=IFortRushBattleController)
def switchToFortRush(ctrl=None):
    ctrl.selectBattle()


class FortRushActionHandler(NavigationDisabledActionHandler):
    _frCtrl = dependency.descriptor(IFortRushBattleController)

    def doAction(self, model, entityID, action):
        logging.debug('[FORT_RUSH] FortRushActionHandler.doAction')
        switchToFortRush()

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('fortRushSwitchPrb', )

    def _canNavigate(self):
        result = super(FortRushActionHandler, self)._canNavigate()
        return self._frCtrl.isAvailable() and result


class _OpenFRProgressionHandler(FortRushActionHandler):

    @classmethod
    def getActions(cls):
        return ('openFRProgression', )

    def doAction(self, model, entityID, action):
        self._frCtrl.selectBattle(showProgressionView)