from frameworks.wulf import ViewModel

class BaseCaptureInfoModel(ViewModel):
    __slots__ = ()
    CAPTURE_POINTS = 'capturePoints'
    DROPPED_CAPTURE_POINTS = 'droppedCapturePoints'

    def __init__(self, properties=2, commands=0):
        super(BaseCaptureInfoModel, self).__init__(properties=properties, commands=commands)

    def getCapturePoints(self):
        return self._getNumber(0)

    def setCapturePoints(self, value):
        self._setNumber(0, value)

    def getDroppedCapturePoints(self):
        return self._getNumber(1)

    def setDroppedCapturePoints(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(BaseCaptureInfoModel, self)._initialize()
        self._addNumberProperty('capturePoints', 0)
        self._addNumberProperty('droppedCapturePoints', 0)