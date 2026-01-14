from __future__ import absolute_import
from vehicles.mechanics.mechanic_states import IMechanicState

class ITemperatureComponentParams(object):

    @property
    def coolingPerSec(self):
        raise NotImplementedError

    @property
    def maxTemperature(self):
        raise NotImplementedError


class ITemperatureMechanicState(IMechanicState):

    @property
    def state(self):
        raise NotImplementedError

    @property
    def currentTemperature(self):
        raise NotImplementedError

    @property
    def maxTemperature(self):
        raise NotImplementedError

    @property
    def temperatureProgress(self):
        raise NotImplementedError