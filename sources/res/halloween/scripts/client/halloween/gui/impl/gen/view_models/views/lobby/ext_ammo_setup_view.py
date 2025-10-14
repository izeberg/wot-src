from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_setup_view_model import AmmunitionSetupViewModel

class ExtAmmoSetupView(AmmunitionSetupViewModel):
    __slots__ = ('onSwitch', )
    HW_CONSUMABLES = 'hw_consumables'

    def __init__(self, properties=9, commands=5):
        super(ExtAmmoSetupView, self).__init__(properties=properties, commands=commands)

    def getAccelerationKeyName(self):
        return self._getString(8)

    def setAccelerationKeyName(self, value):
        self._setString(8, value)

    def _initialize(self):
        super(ExtAmmoSetupView, self)._initialize()
        self._addStringProperty('accelerationKeyName', '')
        self.onSwitch = self._addCommand('onSwitch')