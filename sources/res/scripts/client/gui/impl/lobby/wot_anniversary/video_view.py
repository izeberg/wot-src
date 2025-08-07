from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.impl.lobby.wot_anniversary.sound_helper import getVideoViewSoundSpace

class WotAnniversaryVideoView(WebView):
    _COMMON_SOUND_SPACE = getVideoViewSoundSpace()