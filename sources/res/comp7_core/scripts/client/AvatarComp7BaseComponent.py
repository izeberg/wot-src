from __future__ import absolute_import
from script_component.DynamicScriptComponent import DynamicScriptComponent

class AvatarComp7BaseComponent(DynamicScriptComponent):

    def chooseVehicleForBan(self, vehicleCD):
        self.cell.chooseVehicleForBan(vehicleCD)

    def confirmBanVehicle(self):
        self.cell.confirmBanVehicle()