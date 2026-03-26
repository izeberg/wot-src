from frameworks.wulf import ViewModel

class Constants(ViewModel):
    __slots__ = ()
    NO_SELECTED_VEHICLE_CD = -1
    NO_ANY_SELECTIONS_CD = -2

    def __init__(self, properties=0, commands=0):
        super(Constants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(Constants, self)._initialize()