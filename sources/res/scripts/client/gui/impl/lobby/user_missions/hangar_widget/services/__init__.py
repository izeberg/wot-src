import Event
from gui.prb_control.entities.listener import IGlobalListener

class IBattlePassService(IGlobalListener):
    onBattlePassChanged = Event.Event()

    def startListening(self):
        raise NotImplementedError

    def stopListening(self):
        raise NotImplementedError

    def isVisible(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError


class IEventsService(IGlobalListener):
    onEventsListChanged = Event.Event()

    def startListening(self):
        raise NotImplementedError

    def stopListening(self):
        raise NotImplementedError

    def getEntries(self):
        raise NotImplementedError

    def updateEntries(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError

    @property
    def isAvailable(self):
        raise NotImplementedError


class IMissionsService(IGlobalListener):
    onMissionsChanged = Event.Event()

    def startListening(self):
        raise NotImplementedError

    def stopListening(self):
        raise NotImplementedError

    def isVisible(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError


class ICampaignService(IGlobalListener):
    onEventsListChanged = Event.Event()

    def startListening(self):
        raise NotImplementedError

    def stopListening(self):
        raise NotImplementedError

    def getEntries(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError