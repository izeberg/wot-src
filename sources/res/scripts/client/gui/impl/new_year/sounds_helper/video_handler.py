import WWISE, Windowing

class VideoStartStopHandler(object):
    _videoStates = None
    _videoSoundEvents = None
    __slots__ = ('__started', '__checkPauseOnStart')

    def __init__(self, checkPauseOnStart=True):
        self.__checkPauseOnStart = checkPauseOnStart
        self.__started = False

    def setIsNeedPause(self, isNeedPause):
        if not self.__started:
            return
        if isNeedPause:
            WWISE.WW_eventGlobal(self._videoSoundEvents.VIDEO_PAUSE)
            WWISE.WW_setState(self._videoStates.GROUP, self._videoStates.DONE)
        else:
            WWISE.WW_eventGlobal(self._videoSoundEvents.VIDEO_RESUME)
            WWISE.WW_setState(self._videoStates.GROUP, self._videoStates.START)

    def onVideoStartEvent(self, eventName):
        WWISE.WW_eventGlobal(eventName)
        WWISE.WW_setState(self._videoStates.GROUP, self._videoStates.START)
        self.__started = True
        if self.__checkPauseOnStart and not Windowing.isWindowAccessible():
            WWISE.WW_eventGlobal(self._videoSoundEvents.VIDEO_PAUSE)

    def onVideoDone(self):
        if self.__started:
            WWISE.WW_eventGlobal(self._videoSoundEvents.VIDEO_DONE)
            WWISE.WW_setState(self._videoStates.GROUP, self._videoStates.DONE)
            self.__started = False