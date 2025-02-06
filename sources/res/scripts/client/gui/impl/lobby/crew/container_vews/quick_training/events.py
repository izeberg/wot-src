from gui.impl.lobby.container_views.base.events import ComponentEventsBase

class QuickTrainingViewEvents(ComponentEventsBase):

    def __init__(self):
        super(QuickTrainingViewEvents, self).__init__()
        self.onFreeXpMouseEnter = self._createEvent()
        self.onFreeXpSelected = self._createEvent()
        self.onFreeXpUpdated = self._createEvent()
        self.onFreeXpManualInput = self._createEvent()
        self.onBookMouseEnter = self._createEvent()
        self.onBookSelected = self._createEvent()
        self.onBuyBook = self._createEvent()
        self.onPostProgressionOpen = self._createEvent()
        self.onLearn = self._createEvent()
        self.onCancel = self._createEvent()
        self.onMentoringClick = self._createEvent()