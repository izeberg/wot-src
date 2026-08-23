from __future__ import absolute_import

class IBustleFeedEventsLogic(object):
    onReloadTriggered = None

    def processReloadTriggered(self, shell, side, duration):
        raise NotImplementedError


class IBustleFeedListenerLogic(object):

    def onReloadTriggered(self, shell, side, duration):
        pass