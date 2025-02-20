from frameworks.wulf import ViewModel

class VehicleShellTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(VehicleShellTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(VehicleShellTooltipModel, self)._initialize()