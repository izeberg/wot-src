

class IComponentEvents(object):
    onComponentEventsDestroy = None

    def destroy(self):
        pass


class IComponentListener(object):

    def subscribeTo(self, events):
        raise NotImplementedError

    def unsubscribeFrom(self, events):
        raise NotImplementedError