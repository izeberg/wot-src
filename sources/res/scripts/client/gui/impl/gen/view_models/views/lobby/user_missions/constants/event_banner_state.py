from frameworks.wulf import ViewModel

class EventBannerState(ViewModel):
    __slots__ = ()
    ANNOUNCE = 'announce'
    INTRO = 'intro'
    IN_PROGRESS = 'inProgress'
    INACTIVE = 'inactive'
    FINISHED = 'finished'

    def __init__(self, properties=0, commands=0):
        super(EventBannerState, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(EventBannerState, self)._initialize()