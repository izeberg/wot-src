from gui.shared.events import HasCtxEvent

class PlayerInfoScoreEvent(HasCtxEvent):
    SCORES_CHANGED = 'scores_changed'

    def __init__(self, eventType=None, ctx=None):
        super(PlayerInfoScoreEvent, self).__init__(eventType)
        self.__ctx = ctx

    def getOldScores(self):
        return self.__ctx.get('oldScores', {})

    def getNewScores(self):
        return self.__ctx.get('newScores', {})