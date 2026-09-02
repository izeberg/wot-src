from __future__ import absolute_import

class BasePbhSubSystem(object):

    def __init__(self, readyCallback):
        self._readyCallback = readyCallback

    def subscribe(self):
        raise NotImplementedError

    def unsubscribe(self):
        raise NotImplementedError

    def isReady(self):
        raise NotImplementedError

    def startFlow(self):
        raise NotImplementedError

    def stopFlow(self):
        raise NotImplementedError

    def clear(self):
        self._readyCallback = None
        return