from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.customization.attachments_preview.attachment_bonus_model import AttachmentBonusModel

class AttachmentsPreviewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(AttachmentsPreviewModel, self).__init__(properties=properties, commands=commands)

    def getAttachmentSetID(self):
        return self._getString(0)

    def setAttachmentSetID(self, value):
        self._setString(0, value)

    def getAttachments(self):
        return self._getArray(1)

    def setAttachments(self, value):
        self._setArray(1, value)

    @staticmethod
    def getAttachmentsType():
        return AttachmentBonusModel

    def _initialize(self):
        super(AttachmentsPreviewModel, self)._initialize()
        self._addStringProperty('attachmentSetID', '')
        self._addArrayProperty('attachments', Array())