from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.sounds.filters import switchVideoOverlaySoundFilter

class BattlePassVideoBrowserView(WebView):

    def _populate(self):
        super(BattlePassVideoBrowserView, self)._populate()
        switchVideoOverlaySoundFilter(on=True)

    def _dispose(self):
        switchVideoOverlaySoundFilter(on=False)
        super(BattlePassVideoBrowserView, self)._dispose()