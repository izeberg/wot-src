from gui.battle_results.reusable.common import CommonInfo

class Comp7CommonInfo(CommonInfo):
    __slots__ = ('__bannedVehicles', )

    def __init__(self, *args, **kwargs):
        super(Comp7CommonInfo, self).__init__(*args, **kwargs)
        self.__bannedVehicles = kwargs.get('comp7BannedVehicles', {})

    @property
    def bannedVehicles(self):
        return self.__bannedVehicles