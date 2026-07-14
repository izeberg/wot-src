from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class ILSVehicleSelectionController(IGameController):

    def activate(self):
        raise NotImplementedError

    def deactivate(self):
        raise NotImplementedError

    def selectModeVehicle(self, vehInvID=0):
        raise NotImplementedError

    def selectVehicle(self, vehInvID):
        raise NotImplementedError