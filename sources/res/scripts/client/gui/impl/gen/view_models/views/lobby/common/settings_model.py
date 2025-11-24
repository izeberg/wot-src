from frameworks.wulf import ViewModel

class SettingsModel(ViewModel):
    __slots__ = ('onUpdateSetting', )

    def __init__(self, properties=1, commands=1):
        super(SettingsModel, self).__init__(properties=properties, commands=commands)

    def getReadOnly(self):
        return self._getBool(0)

    def setReadOnly(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(SettingsModel, self)._initialize()
        self._addBoolProperty('readOnly', False)
        self.onUpdateSetting = self._addCommand('onUpdateSetting')