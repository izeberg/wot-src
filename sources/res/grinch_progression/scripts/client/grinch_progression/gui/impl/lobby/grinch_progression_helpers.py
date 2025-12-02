import logging
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared.event_dispatcher import showBrowserOverlayView
_logger = logging.getLogger(__name__)

def showInfoVideo():
    url = GUI_SETTINGS.grinchProgressionInfo.get('baseURL')
    if url is None:
        _logger.error('grinchProgressionInfo.baseURL is missed')
    showBrowserOverlayView(url, alias=VIEW_ALIAS.WEB_VIEW_TRANSPARENT)
    return