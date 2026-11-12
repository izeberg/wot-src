

class IFestivityFactory(object):

    def getRequester(self):
        raise NotImplementedError

    def getRaidRequester(self):
        return

    def getProcessor(self):
        raise NotImplementedError

    def getController(self):
        raise NotImplementedError

    def getDataSyncKey(self):
        raise NotImplementedError

    def getChildControllerInterface(self):
        raise NotImplementedError