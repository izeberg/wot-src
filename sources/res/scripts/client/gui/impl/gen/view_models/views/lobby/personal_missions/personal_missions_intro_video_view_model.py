from frameworks.wulf import ViewModel

class PersonalMissionsIntroVideoViewModel(ViewModel):
    __slots__ = ('onClose', 'onError', 'onVideoStarted')

    def __init__(self, properties=1, commands=3):
        super(PersonalMissionsIntroVideoViewModel, self).__init__(properties=properties, commands=commands)

    def getIsWindowAccessible(self):
        return self._getBool(0)

    def setIsWindowAccessible(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(PersonalMissionsIntroVideoViewModel, self)._initialize()
        self._addBoolProperty('isWindowAccessible', True)
        self.onClose = self._addCommand('onClose')
        self.onError = self._addCommand('onError')
        self.onVideoStarted = self._addCommand('onVideoStarted')