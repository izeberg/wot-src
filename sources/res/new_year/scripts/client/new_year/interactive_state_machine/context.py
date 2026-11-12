from new_year.skeletons.i_sm_queue_context import IQueueContext

class QueueContext(IQueueContext):
    __slots__ = ('wasInBattle', 'isLocked', 'firstBattleLatch')

    def __init__(self):
        super(QueueContext, self).__init__()
        self.reset()

    def reset(self):
        self.wasInBattle = False
        self.isLocked = False
        self.firstBattleLatch = False