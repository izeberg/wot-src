from frameworks.wulf import WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.pub.lobby_window import LobbyWindow
from events_core_client.gui.impl.video_with_controls.video_view import VideoView, VideoPrerequisites

class WtVideoView(VideoView):
    __slots__ = ('__closedCallback', )

    def __init__(self, layoutID, prerequisites, closedCallback):
        super(WtVideoView, self).__init__(layoutID, prerequisites)
        self.__closedCallback = closedCallback

    def _finalize(self):
        if self.__closedCallback is not None:
            self.__closedCallback()
            self.__closedCallback = None
        super(WtVideoView, self)._finalize()
        return


class WtVideoViewWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self, prerequisites, closedCallback=None):
        super(WtVideoViewWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=WtVideoView(R.views.lobby.events_core_client.video_view.VideoView(), prerequisites, closedCallback), layer=WindowLayer.OVERLAY)