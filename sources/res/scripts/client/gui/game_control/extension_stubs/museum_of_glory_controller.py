import typing, Event
from skeletons.gui.game_control import IMuseumOfGloryController

class MuseumOfGloryController(IMuseumOfGloryController):
    onConfigUpdate = Event.Event()

    @property
    def isEnabled(self):
        return False

    def getEpochMusics(self, year):
        return {}

    def getVehiclesDto(self):
        return []

    def getBackgroundImage(self, year):
        return ''

    def getMinYear(self):
        return -1