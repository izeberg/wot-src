import SoundGroups
from account_helpers import AccountSettings
from account_helpers.AccountSettings import SPACE_DAY_CONGRATS
from adisp import adisp_process
from gui.impl.gen import R
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager, SoundManagerStates
from gui.impl.lobby.video.video_view import showWebmVideoView
from gui.Scaleform.managers.fade_manager import FadeManager
from gui.shared.event_dispatcher import getParentWindow
from gui.shared.lock_overlays import lockNotificationManager
from helpers import dependency
from helpers.events_handler import EventsHandler
from helpers.time_utils import getTimestampByStrDate, getServerUTCTime
from skeletons.gui.game_control import ISpaceDayController, IOverlayController
from skeletons.gui.shared.utils import IHangarSpace

def lockNotifications():
    lockNotificationManager(lock=True, postponeActive=True, source='SpaceDayCongrats')


def unlockNotifications():
    lockNotificationManager(lock=False, releasePostponed=True, source='SpaceDayCongrats')


class SpaceDayVideoSoundControl(IVideoSoundManager):

    def __init__(self):
        self.__state = None
        return

    def start(self):
        SoundGroups.g_instance.playSound2D('space_day_video_2026_start')
        self.__state = SoundManagerStates.PLAYING

    def stop(self):
        if self.__state != SoundManagerStates.STOPPED:
            SoundGroups.g_instance.playSound2D('space_day_video_2026_stop')
            self.__state = SoundManagerStates.STOPPED

    def pause(self):
        SoundGroups.g_instance.playSound2D('space_day_video_2026_pause')
        self.__state = SoundManagerStates.PAUSE

    def unpause(self):
        SoundGroups.g_instance.playSound2D('space_day_video_2026_resume')
        self.__state = SoundManagerStates.PLAYING


class SpaceDayController(ISpaceDayController, EventsHandler):
    __slots__ = ('__fadeManager', '__isVideoActive')
    _hangarSpace = dependency.descriptor(IHangarSpace)
    _overlay = dependency.descriptor(IOverlayController)
    GREETINGS_START_DATE = getTimestampByStrDate('12.04.2026 00:00')
    GREETINGS_END_DATE = getTimestampByStrDate('16.04.2026 00:00')

    def __init__(self):
        super(SpaceDayController, self).__init__()
        self.__fadeManager = FadeManager()
        self.__isVideoActive = False

    def onConnected(self):
        super(SpaceDayController, self).onConnected()
        self.__activateAction()

    def onDisconnected(self):
        super(SpaceDayController, self).onDisconnected()
        self.__deactivateAction()

    def onAvatarBecomePlayer(self):
        self.__deactivateAction()

    def onAccountBecomePlayer(self):
        self.__activateAction()

    def _getEvents(self):
        return (
         (
          self._hangarSpace.onSpaceCreate, self.__onHangarSpaceCreated),)

    def __onHangarSpaceCreated(self):
        self.__tryStartCongratsVideo()

    def __isCongratsVideoViewed(self):
        return AccountSettings.getSettings(SPACE_DAY_CONGRATS)

    def __shouldPlayGreetingVideo(self):
        return self.GREETINGS_START_DATE <= getServerUTCTime() < self.GREETINGS_END_DATE

    def __tryStartCongratsVideo(self):
        if self.__isCongratsVideoViewed():
            self._unsubscribe()
            return
        if not self.__shouldPlayGreetingVideo():
            return
        self.__isVideoActive = True
        lockNotifications()
        self._overlay.setOverlayState(True)
        showWebmVideoView(videoSource=R.videos.space_day_congrats(), parent=getParentWindow(), onVideoStarted=self.__onCongratsVideoStarted, onVideoClosed=self.__onCongratsVideoDone, soundControl=SpaceDayVideoSoundControl(), isAutoClose=True, canEscape=True, isUIVisible=True, uiShowDelay=1)

    @adisp_process
    def __onCongratsVideoStarted(self):
        AccountSettings.setSettings(SPACE_DAY_CONGRATS, True)
        yield self.__fadeManager.startFade()

    @adisp_process
    def __onCongratsVideoDone(self):
        yield self.__fadeManager.startFade(fadeIn=False)
        self.__clear()

    def __activateAction(self):
        if not self.__isCongratsVideoViewed():
            self._subscribe()
            self.__fadeManager.setup()

    def __deactivateAction(self):
        self.__clear()
        self.__fadeManager.destroy()

    def __clear(self):
        self._unsubscribe()
        if self.__isVideoActive:
            unlockNotifications()
            self._overlay.setOverlayState(False)
            self.__isVideoActive = False