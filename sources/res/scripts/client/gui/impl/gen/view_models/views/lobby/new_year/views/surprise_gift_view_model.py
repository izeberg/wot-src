from frameworks.wulf import ViewModel

class SurpriseGiftViewModel(ViewModel):
    __slots__ = ('onGoToHangar', 'onGoToAttachments')

    def __init__(self, properties=2, commands=2):
        super(SurpriseGiftViewModel, self).__init__(properties=properties, commands=commands)

    def getDescription(self):
        return self._getString(0)

    def setDescription(self, value):
        self._setString(0, value)

    def getVehicleName(self):
        return self._getString(1)

    def setVehicleName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(SurpriseGiftViewModel, self)._initialize()
        self._addStringProperty('description', '')
        self._addStringProperty('vehicleName', '')
        self.onGoToHangar = self._addCommand('onGoToHangar')
        self.onGoToAttachments = self._addCommand('onGoToAttachments')