from frameworks.wulf import ViewModel

class FunRandomLoadoutConstants(ViewModel):
    __slots__ = ()
    FUN_RANDOM_CUSTOM_SHELLS = 'funRandomCustomShells'
    FUN_RANDOM_CUSTOM_ABILITIES = 'funRandomCustomAbilities'
    BATTLE_ABILITIES_GROUP = 3

    def __init__(self, properties=0, commands=0):
        super(FunRandomLoadoutConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FunRandomLoadoutConstants, self)._initialize()