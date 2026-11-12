from events_core_client.gui.impl.video_with_controls.video_view import VideoView
from frameworks.wulf import WindowFlags, WindowLayer
from gui.Scaleform.Waiting import Waiting
from gui.impl.gen import R
from gui.impl.pub.lobby_window import LobbyWindow
from helpers import dependency
from new_year.ny_constants import NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY
from skeletons.gui.app_loader import IAppLoader

class _EmbeddedAudioVideoView(VideoView):
    __slots__ = ('__onVideoClosed', '__onVideoStarted', '__app', '__previouslyVisibleLayers',
                 '__layersRestricted', '__notificationsLocked', '__releaseNotificationsLockOnClose')
    __appLoader = dependency.descriptor(IAppLoader)
    VISIBLE_LAYERS = (
     WindowLayer.OVERLAY, WindowLayer.CURSOR, WindowLayer.WAITING, WindowLayer.SERVICE_LAYOUT)

    def __init__(self, layoutID, prerequisites, onClosed=None, onStarted=None, releaseNotificationsLockOnClose=True):
        super(_EmbeddedAudioVideoView, self).__init__(layoutID, prerequisites)
        self.__onVideoClosed = onClosed
        self.__onVideoStarted = onStarted
        self.__app = self.__appLoader.getApp()
        self.__previouslyVisibleLayers = []
        self.__layersRestricted = False
        self.__notificationsLocked = False
        self.__releaseNotificationsLockOnClose = releaseNotificationsLockOnClose

    def _onLoaded(self, *args, **kwargs):
        super(_EmbeddedAudioVideoView, self)._onLoaded(*args, **kwargs)
        Waiting.suspend(id(self))
        startedCallback = self.__onVideoStarted
        self.__onVideoStarted = None
        if startedCallback is not None:
            startedCallback()
        return

    def _initialize(self, *args, **kwargs):
        from new_year.helpers.ny_helpers import lockNyNotifications
        super(_EmbeddedAudioVideoView, self)._initialize(*args, **kwargs)
        self.__restrictVisibleLayers()
        lockNyNotifications(NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY, lock=True)
        self.__notificationsLocked = True

    def clearLifecycleCallbacks(self):
        self.__onVideoClosed = None
        self.__onVideoStarted = None
        return

    def _finalize(self):
        from new_year.helpers.ny_helpers import lockNyNotifications
        Waiting.resume(id(self))
        self.__restoreVisibleLayers()
        if self.__notificationsLocked and self.__releaseNotificationsLockOnClose:
            lockNyNotifications(NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY, lock=False)
            self.__notificationsLocked = False
        callback = self.__onVideoClosed
        self.clearLifecycleCallbacks()
        if callback is not None:
            callback()
        self.__app = None
        self.__previouslyVisibleLayers = None
        super(_EmbeddedAudioVideoView, self)._finalize()
        return

    def __restrictVisibleLayers(self):
        if self.__app is None:
            return
        else:
            containerManager = self.__app.containerManager
            self.__previouslyVisibleLayers = containerManager.getVisibleLayers()
            containerManager.setVisibleLayers(self.VISIBLE_LAYERS)
            self.__layersRestricted = True
            return

    def __restoreVisibleLayers(self):
        if self.__app is not None and self.__layersRestricted:
            self.__app.containerManager.setVisibleLayers(self.__previouslyVisibleLayers)
            self.__layersRestricted = False
        return


class _EmbeddedAudioVideoWindow(LobbyWindow):
    __slots__ = ('__view', )

    def __init__(self, prerequisites, parent=None, onClosed=None, onStarted=None, releaseNotificationsLockOnClose=True):
        self.__view = _EmbeddedAudioVideoView(R.views.lobby.events_core_client.video_view.VideoView(), prerequisites, onClosed=onClosed, onStarted=onStarted, releaseNotificationsLockOnClose=releaseNotificationsLockOnClose)
        super(_EmbeddedAudioVideoWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=self.__view, parent=parent, layer=WindowLayer.OVERLAY)

    def destroyWithoutCallbacks(self):
        if self.__view is not None:
            self.__view.clearLifecycleCallbacks()
            self.__view = None
        self.destroy()
        return