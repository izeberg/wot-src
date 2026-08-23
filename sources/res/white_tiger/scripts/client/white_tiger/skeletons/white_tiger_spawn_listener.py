from __future__ import absolute_import
from enum import IntEnum

class SpawnType(IntEnum):
    DEFAULT = 1
    TELEPORT = 2


class ISpawnListener(object):

    def setSpawnPoints(self, points, pointId=None):
        pass

    def showSpawnPoints(self):
        pass

    def closeSpawnPoints(self):
        pass

    def updatePoint(self, vehicleId, pointId, prevPointId):
        pass

    def updateCloseTime(self, timeLeft, state):
        pass

    def onSelectPoint(self, pointId):
        pass

    def setSpawnType(self, spawnType):
        pass