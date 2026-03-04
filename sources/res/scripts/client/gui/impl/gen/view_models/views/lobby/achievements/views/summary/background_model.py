from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BackgroundModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BackgroundModel, self).__init__(properties=properties, commands=commands)

    def getSlug(self):
        return self._getString(0)

    def setSlug(self, value):
        self._setString(0, value)

    def getImage(self):
        return self._getResource(1)

    def setImage(self, value):
        self._setResource(1, value)

    def getLabel(self):
        return self._getResource(2)

    def setLabel(self, value):
        self._setResource(2, value)

    def _initialize(self):
        super(BackgroundModel, self)._initialize()
        self._addStringProperty('slug', '')
        self._addResourceProperty('image', R.invalid())
        self._addResourceProperty('label', R.invalid())