from frameworks.wulf import ViewModel

class CustomizationCloseConfirmationDialogModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(CustomizationCloseConfirmationDialogModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CustomizationCloseConfirmationDialogModel, self)._initialize()