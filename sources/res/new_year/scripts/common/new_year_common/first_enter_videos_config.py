from new_year_common.settings import FirstEnterVideosConsts

class FirstEnterVideoConfigItem(object):
    __slots__ = ('_data', )

    def __init__(self, data):
        self._data = data or {}

    @property
    def id(self):
        return self._data.get(FirstEnterVideosConsts.VIDEO_ID, '')

    @property
    def priority(self):
        return self._data.get(FirstEnterVideosConsts.PRIORITY, FirstEnterVideosConsts.PRIORITY_WEEKLY_REPORT)

    @property
    def videoName(self):
        return self._data.get(FirstEnterVideosConsts.VIDEO_NAME, '')

    @property
    def startDate(self):
        return self._data.get(FirstEnterVideosConsts.START_DATE)

    @property
    def endDate(self):
        return self._data.get(FirstEnterVideosConsts.END_DATE)

    @property
    def visible(self):
        return self._data.get(FirstEnterVideosConsts.VISIBLE, False)

    @property
    def canEscape(self):
        return self._data.get(FirstEnterVideosConsts.CAN_ESCAPE, True)

    @property
    def utc(self):
        return self._data.get(FirstEnterVideosConsts.UTC, False)


class FirstEnterVideosConfig(object):
    __slots__ = ('_videos', )

    def __init__(self, config=None):
        rawVideos = (config or {}).get(FirstEnterVideosConsts.VIDEOS, ())
        self._videos = tuple(FirstEnterVideoConfigItem(item) for item in rawVideos)

    def getVideos(self):
        return self._videos