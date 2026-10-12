from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class FunRandomCustomAbilitySlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(FunRandomCustomAbilitySlot, self).__init__(properties=properties, commands=commands)

    def getTooltipAlias(self):
        return self._getString(13)

    def setTooltipAlias(self, value):
        self._setString(13, value)

    def _initialize(self):
        super(FunRandomCustomAbilitySlot, self)._initialize()
        self._addStringProperty('tooltipAlias', '')