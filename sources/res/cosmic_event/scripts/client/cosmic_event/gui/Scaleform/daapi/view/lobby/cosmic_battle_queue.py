from gui.Scaleform.daapi.view.lobby.battle_queue import RandomQueueProvider

class CosmicEventQueueProvider(RandomQueueProvider):

    def processQueueInfo(self, qInfo):
        self._proxy.setPlayersTypeCDs(qInfo.get('vehTypeCompDescrs', {}))
        self._proxy.setSelectedVehicle()

    def _createCommonPlayerString(self, playerCount):
        pass