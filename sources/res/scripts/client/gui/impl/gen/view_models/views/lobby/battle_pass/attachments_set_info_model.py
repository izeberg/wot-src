from frameworks.wulf import ViewModel

class AttachmentsSetInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(AttachmentsSetInfoModel, self).__init__(properties=properties, commands=commands)

    def getAttachmentsSetName(self):
        return self._getString(0)

    def setAttachmentsSetName(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(AttachmentsSetInfoModel, self)._initialize()
        self._addStringProperty('attachmentsSetName', '')