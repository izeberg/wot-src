import BigWorld
from gui.shared.gui_items.processors import Processor
from gui.shared.gui_items.processors.plugins import VehicleValidator

class SetSkillProcessor(Processor):

    def __init__(self, equipmentID, vehicle):
        super(SetSkillProcessor, self).__init__(plugins=[VehicleValidator(vehicle)])
        self.vehicleInvID = vehicle.invID
        self.equipmentID = equipmentID

    def _request(self, callback):
        BigWorld.player().AccountComp7Component.setVehicleSkill(self.vehicleInvID, self.equipmentID, lambda code, errStr: self._response(code, callback, errStr=errStr))