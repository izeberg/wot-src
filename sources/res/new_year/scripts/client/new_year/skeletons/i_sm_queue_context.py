

class IQueueContext(object):
    wasInBattle = False
    isLocked = False
    firstBattleLatch = False

    def reset(self):
        raise NotImplementedError