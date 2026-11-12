from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_filter_model import CustomizationResourceFilterModel

class CustomizationResourceFilterPopoverViewModel(ViewModel):
    __slots__ = ('changeFilter', 'clearFilter')

    def __init__(self, properties=1, commands=2):
        super(CustomizationResourceFilterPopoverViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def filterModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getFilterModelType():
        return CustomizationResourceFilterModel

    def _initialize(self):
        super(CustomizationResourceFilterPopoverViewModel, self)._initialize()
        self._addViewModelProperty('filterModel', CustomizationResourceFilterModel())
        self.changeFilter = self._addCommand('changeFilter')
        self.clearFilter = self._addCommand('clearFilter')