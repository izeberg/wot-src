

class IArmorFlashlightBattleController(object):

    def toggle(self):
        raise NotImplementedError

    def addHideReason(self, reason):
        raise NotImplementedError

    def removeHideReason(self, reason):
        raise NotImplementedError