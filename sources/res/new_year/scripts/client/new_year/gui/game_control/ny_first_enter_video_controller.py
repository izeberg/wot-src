from new_year.ny_constants import NY_FIRST_ENTER_VIDEOS_SEEN, NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY
from new_year.helpers.server_settings import getNewYearFirstEnterVideosConfig
from new_year.skeletons.i_sm_queue import IStateMachineQueue
from new_year.skeletons.new_year import INewYearController, INewYearFirstEnterVideoController
from new_year_common.settings import FirstEnterVideosConsts
from helpers.time_utils import getCurrentTimestamp, getDateTimeInLocal, getDateTimeInUTC, getServerUTCTime
from new_year_account_settings import getNYSetting, setNYSettings
from gui.Scaleform.managers.fade_manager import FadeManager
from new_year.helpers.ny_helpers import showEmbeddedAudioVideoView, lockNyNotifications
from skeletons.gui.game_control import IOverlayController
from gui.shared.utils import isPopupsWindowsOpenDisabled
from gui.shared.event_dispatcher import getParentWindow
from skeletons.gui.shared.utils import IHangarSpace
from helpers.events_handler import EventsHandler
from debug_utils import LOG_ERROR
from Event import EventManager, Event
from adisp import adisp_process
from helpers import dependency
from gui.impl.gen import R

def _resolveFirstEnterVideoSource(videoName):
    accessor = getattr(R.videos.new_year.greetings, videoName, None)
    if accessor is None:
        LOG_ERROR(('[NewYearFirstEnterVideo] Unknown video resource in greetings: "{}"').format(videoName))
        return
    else:
        return accessor()


def _clockTime(video):
    if video.utc:
        return getDateTimeInUTC(getServerUTCTime())
    return getDateTimeInLocal(getCurrentTimestamp())


class NewYearFirstEnterVideoController(INewYearFirstEnterVideoController, EventsHandler):
    __slots__ = ('__fadeManager', '__video', '__isIntroActive', '__hasPlayedVideoThisSession',
                 '__hangarReadyOnce', '__em')
    _hangarSpace = dependency.descriptor(IHangarSpace)
    _nyController = dependency.descriptor(INewYearController)
    _overlay = dependency.descriptor(IOverlayController)
    _stateMachineQueue = dependency.descriptor(IStateMachineQueue)

    def __init__(self):
        super(NewYearFirstEnterVideoController, self).__init__()
        self.__fadeManager = FadeManager()
        self.__video = None
        self.__isIntroActive = False
        self.__hasPlayedVideoThisSession = False
        self.__hangarReadyOnce = False
        self.__em = EventManager()
        self.onIntroComplete = Event(self.__em)
        return

    def fini(self):
        self.__deactivateAction()
        self.__em.clear()
        super(NewYearFirstEnterVideoController, self).fini()

    def onDisconnected(self):
        super(NewYearFirstEnterVideoController, self).onDisconnected()
        self.__hangarReadyOnce = False
        self.__deactivateAction()

    def onAvatarBecomePlayer(self):
        self.__deactivateAction()

    def onLobbyInited(self, _=None):
        self.__activateAction()
        self.tryStartIntro()

    @property
    def isActive(self):
        return self.__isIntroActive

    def shouldStartIntro(self):
        if isPopupsWindowsOpenDisabled():
            return False
        else:
            if self.isActive:
                return True
            return self.__selectVideo() is not None

    def tryStartIntro(self):
        if isPopupsWindowsOpenDisabled() or self.isActive:
            return
        if not self._hangarSpace.spaceInited:
            return
        else:
            video = self.__selectVideo()
            self.__hangarReadyOnce = True
            if video is None:
                if not self.__hasPendingVideos():
                    self._unsubscribe()
                return
            videoSource = _resolveFirstEnterVideoSource(video.videoName)
            if videoSource is None:
                self.__markVideoViewed(video.id)
                return
            self.__isIntroActive = True
            self.__hasPlayedVideoThisSession = True
            self.__markVideoViewed(video.id)
            self._overlay.setOverlayState(True)
            self.__showVideo(videoSource, canEscape=video.canEscape)
            return

    def _getEvents(self):
        return ((self._hangarSpace.onSpaceCreate, self.tryStartIntro),
         (
          self._nyController.onStateChanged, self.tryStartIntro),
         (
          self._nyController.onNySettingsChanged, self.__onNySettingsChanged))

    def __activateAction(self):
        if not self.__hasPendingVideos():
            return
        self._subscribe()
        self.__fadeManager.setup()

    def __onNySettingsChanged(self):
        if not self.__hasPendingVideos() and not self.isActive:
            self._unsubscribe()

    def __deactivateAction(self):
        self.__stopVideo(destroy=True)
        self.__clear()
        self.__fadeManager.destroy()
        self._stateMachineQueue.release()

    def __selectVideo(self):
        if not self._nyController.isEnabled():
            return None
        else:
            eligible = [ video for video in getNewYearFirstEnterVideosConfig().getVideos() if self.__isVideoEligible(video) and self.__canPlayInCurrentSession(video) ]
            if not eligible:
                return None
            return min(eligible, key=lambda item: (item.priority, item.id))

    def __canPlayInCurrentSession(self, video):
        if video.priority == FirstEnterVideosConsts.PRIORITY_GREETING:
            return True
        return not self.__hasPlayedVideoThisSession and not self.__hangarReadyOnce

    def __hasPendingVideos(self):
        return any(video.visible and video.startDate is not None and not self.__isVideoViewed(video.id) and not self.__isVideoExpired(video, _clockTime(video)) for video in getNewYearFirstEnterVideosConfig().getVideos())

    def __isVideoEligible(self, video):
        if not video.visible or video.startDate is None or self.__isVideoViewed(video.id):
            return False
        now = _clockTime(video)
        return not self.__isVideoExpired(video, now) and now >= getDateTimeInUTC(video.startDate)

    @staticmethod
    def __isVideoExpired(video, now):
        return video.endDate is not None and now >= getDateTimeInUTC(video.endDate)

    def __isVideoViewed(self, videoId):
        seen = getNYSetting(NY_FIRST_ENTER_VIDEOS_SEEN) or set()
        return videoId in seen

    def __markVideoViewed(self, videoId):
        seen = set(getNYSetting(NY_FIRST_ENTER_VIDEOS_SEEN) or set())
        seen.add(videoId)
        setNYSettings(NY_FIRST_ENTER_VIDEOS_SEEN, seen)

    def __showVideo(self, videoSource, canEscape):
        self.__video = showEmbeddedAudioVideoView(videoSource=videoSource, parent=getParentWindow(), onVideoStarted=self.__onVideoStarted, onVideoClosed=self.__onVideoDone, isControlsVisible=False, releaseNotificationsLockOnClose=False, canEscape=canEscape)

    def __stopVideo(self, destroy=False):
        video = self.__video
        self.__video = None
        if destroy and video is not None:
            video.destroyWithoutCallbacks()
        return

    @adisp_process
    def __onVideoStarted(self):
        if not self.__isIntroActive:
            return
        self._stateMachineQueue.lock()
        yield self.__fadeManager.startFade()

    @adisp_process
    def __onVideoDone(self):
        self.__stopVideo()
        self._stateMachineQueue.release()
        if not self.__isIntroActive:
            return
        yield self.__fadeManager.startFade(fadeIn=False)
        if not self.__isIntroActive:
            return
        self.__clear()
        self.onIntroComplete()

    def __clear(self):
        self._unsubscribe()
        if self.isActive:
            lockNyNotifications(NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY, lock=False)
            self._overlay.setOverlayState(False)
            self.__isIntroActive = False