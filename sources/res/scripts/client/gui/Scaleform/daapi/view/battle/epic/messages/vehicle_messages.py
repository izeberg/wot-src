from gui.Scaleform.daapi.view.battle.shared import messages
from supply_shared import Supply

class EpicVehicleMessages(messages.VehicleMessages):

    def _getPlayerInfo(self, playerName, vTypeInfoVO):
        if Supply.isSupply(vTypeInfoVO.tags):
            return vTypeInfoVO.shortNameWithPrefix
        return super(EpicVehicleMessages, self)._getPlayerInfo(playerName, vTypeInfoVO)