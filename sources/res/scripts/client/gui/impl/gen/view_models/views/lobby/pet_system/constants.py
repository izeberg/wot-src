from enum import Enum
from frameworks.wulf import ViewModel

class PetState(Enum):
    UNDEFINED = 'undefined'
    PROMO = 'Promo'


class Constants(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(Constants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(Constants, self)._initialize()