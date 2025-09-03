

class IPresenterLocationController(object):

    def _initializeLocation(self):
        raise NotImplementedError

    def _finalizeLocation(self):
        raise NotImplementedError