from gui.impl.gen.view_models.common.marker_model import MarkerModel

class CustomizationSubButtonModel(MarkerModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(CustomizationSubButtonModel, self).__init__(properties=properties, commands=commands)

    def getActionData(self):
        return self._getNumber(6)

    def setActionData(self, value):
        self._setNumber(6, value)

    def getIcon(self):
        return self._getString(7)

    def setIcon(self, value):
        self._setString(7, value)

    def getIsSelected(self):
        return self._getBool(8)

    def setIsSelected(self, value):
        self._setBool(8, value)

    def getPaletteIcon(self):
        return self._getString(9)

    def setPaletteIcon(self, value):
        self._setString(9, value)

    def _initialize(self):
        super(CustomizationSubButtonModel, self)._initialize()
        self._addNumberProperty('actionData', 0)
        self._addStringProperty('icon', '')
        self._addBoolProperty('isSelected', False)
        self._addStringProperty('paletteIcon', '')