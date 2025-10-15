from frameworks.wulf import ViewModel

class PortalWidgetBossDamage(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(PortalWidgetBossDamage, self).__init__(properties=properties, commands=commands)

    def getDamage(self):
        return self._getNumber(0)

    def setDamage(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(PortalWidgetBossDamage, self)._initialize()
        self._addNumberProperty('damage', 0)