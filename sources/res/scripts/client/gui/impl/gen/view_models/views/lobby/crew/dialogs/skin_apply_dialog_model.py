from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel

class SkinApplyDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=2):
        super(SkinApplyDialogModel, self).__init__(properties=properties, commands=commands)

    def getDescription(self):
        return self._getString(6)

    def setDescription(self, value):
        self._setString(6, value)

    def _initialize(self):
        super(SkinApplyDialogModel, self)._initialize()
        self._addStringProperty('description', '')