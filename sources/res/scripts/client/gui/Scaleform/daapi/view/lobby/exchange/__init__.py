from frameworks.wulf import WindowLayer
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import ShowDialogEvent
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.exchange.ConfirmExchangeDialog import ConfirmExchangeDialog
    return (
     GroupedViewSettings(VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG, ConfirmExchangeDialog, 'confirmExchangeDialog.swf', WindowLayer.WINDOW, 'confirmExchangeDialog', None, ScopeTemplates.LOBBY_SUB_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG_MODAL, ConfirmExchangeDialog, 'confirmExchangeDialog.swf', WindowLayer.TOP_WINDOW, 'confirmExchangeDialog', None, ScopeTemplates.LOBBY_SUB_SCOPE, isModal=True))


def getBusinessHandlers():
    return (
     _ExchangeDialogBusinessHandler(),
     _ExchangeDialogModalBusinessHandler())


class _ExchangeDialogBusinessHandler(PackageBusinessHandler):
    _ALIAS = VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG
    _EVENT = ShowDialogEvent.SHOW_EXCHANGE_DIALOG
    _LAYER = WindowLayer.WINDOW

    def __init__(self):
        listeners = (
         (
          self._EVENT, self._exchangeDialogHandler),)
        super(_ExchangeDialogBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.DEFAULT)

    def _exchangeDialogHandler(self, event):
        name = 'exchange' + event.meta.getType()
        self.__loadOrUpdateDialog(name, self._ALIAS, event.meta, event.handler)

    def __loadOrUpdateDialog(self, name, alias, meta, handler):
        window = self.findViewByName(self._LAYER, name)
        if window is not None:
            window.updateDialog(meta, handler)
            self.bringViewToFront(name)
        else:
            self.loadViewWithDefName(alias, name, None, meta, handler)
        return


class _ExchangeDialogModalBusinessHandler(_ExchangeDialogBusinessHandler):
    _ALIAS = VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG_MODAL
    _EVENT = ShowDialogEvent.SHOW_EXCHANGE_DIALOG_MODAL
    _LAYER = WindowLayer.TOP_WINDOW