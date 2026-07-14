from __future__ import absolute_import
from enum import Enum

class LSKeys(Enum):
    VOIP_CONNECTED = 'voipConnected'

    @staticmethod
    def getKeys(static=True):
        if static:
            return [(LSKeys.VOIP_CONNECTED, False)]
        return []

    @staticmethod
    def getSortingKeys(static=True):
        return []