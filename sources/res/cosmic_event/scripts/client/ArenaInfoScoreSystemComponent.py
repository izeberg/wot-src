import BigWorld, Event

class ArenaInfoScoreSystemComponent(BigWorld.DynamicScriptComponent):

    def __init__(self, *args):
        self.onArenaScoreUpdated = Event.Event()

    def set_totalScore(self, prev):
        self.onArenaScoreUpdated(self.totalScore)

    def set_revenges(self, prev):
        self.onArenaScoreUpdated(self.totalScore)