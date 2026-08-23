from __future__ import absolute_import
from helpers import dependency
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE
from white_tiger.skeletons.white_tiger_controller import IWhiteTigerController
from white_tiger.gui.shared.event_dispatcher import showProgressionScreen, showHangar, showBuyLootboxOverlay

class _WTEventHandler(NavigationDisabledActionHandler):
    _wtCtrl = dependency.descriptor(IWhiteTigerController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    def _canNavigate(self):
        result = super(_WTEventHandler, self)._canNavigate()
        return self._wtCtrl.isEnabled() and result


class _OpenWTEventProgressionHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return ('openWTEventCollection', )

    def doAction(self, model, entityID, action):
        self._wtCtrl.selectBattle(showProgressionScreen)


class _OpenWTEventHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return ('openWTEvent', )

    def doAction(self, model, entityID, action):
        self._wtCtrl.selectBattle(showHangar)


class _OpenWTEventQuestsHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return ('openWTEventQuests', )

    def doAction(self, model, entityID, action):
        self._wtCtrl.selectBattle(showProgressionScreen)


class _OpenWTEventTicketPurchasingHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return ('openWTEventTicketPurchasing', )

    def doAction(self, model, entityID, action):
        self._wtCtrl.selectBattle(showBuyLootboxOverlay)