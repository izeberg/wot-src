from __future__ import absolute_import
import typing

class IClientEventsContainer(object):
    onEventsContainerDestroy = None

    @property
    def hasListeners(self):
        raise NotImplementedError

    def destroy(self):
        pass

    def attachCFGEvents(self):
        pass

    def debugEvents(self):
        pass

    def lateSubscribe(self, listener):
        listener.subscribeTo(self)

    def unsubscribe(self, listener):
        listener.unsubscribeFrom(self)


class IClientEventsContainerListener(object):

    def subscribeTo(self, events):
        raise NotImplementedError

    def unsubscribeFrom(self, events):
        raise NotImplementedError

    def lateSubscribeTo(self, events):
        raise NotImplementedError